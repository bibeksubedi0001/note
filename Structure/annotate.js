/* Draw Anywhere – session-only, zero persistence */
(function () {
  'use strict';
  var on = false, drawing = false, erasing = false;
  var COLORS = ['#e63946','#1a365d','#2d6a4f','#e67e22','#7c3aed','#000'];
  var color = COLORS[0], penW = 3;
  var strokes = [];  // finished: [{c,w,er,p:[x,y,x,y,...]}]
  var pts = [];      // current stroke points (flat: x,y,x,y,...)
  var drawn = 0;     // how many points already rendered
  var raf = 0;

  /* --- CSS --- */
  var st = document.createElement('style');
  st.textContent =
    '.dw-btn{position:fixed;bottom:70px;right:24px;z-index:10010;width:46px;height:46px;border-radius:50%;border:none;background:#1a365d;color:#fff;font-size:21px;cursor:pointer;box-shadow:0 2px 8px rgba(0,0,0,.3);display:flex;align-items:center;justify-content:center;transition:background .15s,transform .15s}.dw-btn:hover{transform:scale(1.08)}.dw-btn.on{background:#c9a84c;color:#1a365d}' +
    '.dw-tb{position:fixed;bottom:124px;right:24px;z-index:10010;background:#fff;border-radius:10px;padding:8px;box-shadow:0 4px 14px rgba(0,0,0,.22);display:none;flex-direction:column;gap:5px;align-items:center;font:12px/1 sans-serif;pointer-events:auto}.dw-tb.show{display:flex}' +
    '.dw-dot{width:20px;height:20px;border-radius:50%;border:2px solid transparent;cursor:pointer;transition:.12s}.dw-dot:hover,.dw-dot.on{border-color:#222;transform:scale(1.12)}' +
    '.dw-b{background:#f0f0f0;border:1px solid #ccc;border-radius:5px;padding:3px 8px;cursor:pointer;text-align:center;width:100%}.dw-b:hover{background:#e0e0e0}.dw-b.on{background:#1a365d;color:#fff;border-color:#1a365d}' +
    '.dw-cv{position:fixed;top:0;left:0;width:100%;height:100%;z-index:10000;pointer-events:none;touch-action:none}.dw-cv.on{pointer-events:auto;cursor:crosshair}';
  document.head.appendChild(st);

  /* --- fixed viewport canvas (small and fast) --- */
  var cv = document.createElement('canvas');
  cv.className = 'dw-cv';
  document.body.appendChild(cv);

  // allow mouse wheel to scroll through the canvas
  cv.addEventListener('wheel', function (e) {
    window.scrollBy(0, e.deltaY);
    paint();
  }, { passive: true });
  var cx = cv.getContext('2d');

  function sized() {
    var dpr = window.devicePixelRatio || 1;
    var w = window.innerWidth, h = window.innerHeight;
    cv.width = w * dpr; cv.height = h * dpr;
    cv.style.width = w + 'px'; cv.style.height = h + 'px';
    cx.setTransform(dpr, 0, 0, dpr, 0, 0);
    paint();
  }
  sized();
  window.addEventListener('resize', sized);

  /* --- full repaint (scroll-aware): only on scroll/resize/undo --- */
  function paint() {
    var sx = window.scrollX, sy = window.scrollY;
    cx.clearRect(0, 0, cv.width, cv.height);
    for (var s = 0; s < strokes.length; s++) {
      var sk = strokes[s], p = sk.p;
      if (p.length < 4) continue;
      cx.globalCompositeOperation = sk.er ? 'destination-out' : 'source-over';
      cx.strokeStyle = sk.c;
      cx.lineWidth = sk.er ? sk.w * 4 : sk.w;
      cx.lineCap = 'round';
      cx.lineJoin = 'round';
      cx.beginPath();
      cx.moveTo(p[0] - sx, p[1] - sy);
      for (var i = 2; i < p.length; i += 2) cx.lineTo(p[i] - sx, p[i + 1] - sy);
      cx.stroke();
    }
  }
  window.addEventListener('scroll', paint);

  /* --- UI --- */
  var btn = document.createElement('button');
  btn.className = 'dw-btn'; btn.title = 'Draw'; btn.innerHTML = '&#9998;';
  document.body.appendChild(btn);

  var tb = document.createElement('div'); tb.className = 'dw-tb';
  COLORS.forEach(function (c) {
    var d = document.createElement('div');
    d.className = 'dw-dot' + (c === color ? ' on' : '');
    d.style.background = c;
    d.onclick = function () {
      color = c; erasing = false; erBtn.classList.remove('on');
      tb.querySelectorAll('.dw-dot').forEach(function (x) { x.classList.remove('on'); });
      d.classList.add('on');
    };
    tb.appendChild(d);
  });
  var lbl = document.createElement('label'); lbl.textContent = 'Size'; lbl.style.cssText = 'color:#666;margin-top:2px';
  tb.appendChild(lbl);
  var sl = document.createElement('input');
  sl.type = 'range'; sl.min = '1'; sl.max = '12'; sl.value = String(penW); sl.style.width = '76px';
  sl.oninput = function () { penW = +sl.value; };
  tb.appendChild(sl);

  var erBtn = document.createElement('button'); erBtn.className = 'dw-b'; erBtn.textContent = 'Eraser';
  erBtn.onclick = function () { erasing = !erasing; erBtn.classList.toggle('on', erasing); if (erasing) tb.querySelectorAll('.dw-dot').forEach(function (x) { x.classList.remove('on'); }); };
  tb.appendChild(erBtn);

  var unBtn = document.createElement('button'); unBtn.className = 'dw-b'; unBtn.textContent = 'Undo';
  unBtn.onclick = function () { if (strokes.length) { strokes.pop(); paint(); } };
  tb.appendChild(unBtn);

  var clBtn = document.createElement('button'); clBtn.className = 'dw-b'; clBtn.textContent = 'Clear';
  clBtn.onclick = function () { strokes.length = 0; paint(); };
  tb.appendChild(clBtn);

  document.body.appendChild(tb);

  // stop toolbar clicks from reaching canvas
  ['pointerdown','pointerup','pointermove'].forEach(function (ev) {
    tb.addEventListener(ev, function (e) { e.stopPropagation(); });
    btn.addEventListener(ev, function (e) { e.stopPropagation(); });
  });

  btn.onclick = function () {
    on = !on;
    btn.classList.toggle('on', on);
    tb.classList.toggle('show', on);
    cv.classList.toggle('on', on);
  };

  /* --- rAF render loop: draws only NEW points, never redraws old ones --- */
  function tick() {
    if (!drawing) { raf = 0; return; }
    var n = pts.length;
    if (drawn < n) {
      var sx = window.scrollX, sy = window.scrollY;
      // continue the existing path from last drawn point
      if (drawn === 0) {
        cx.beginPath();
        cx.moveTo(pts[0] - sx, pts[1] - sy);
        drawn = 2;
      }
      for (var i = drawn; i < n; i += 2) {
        cx.lineTo(pts[i] - sx, pts[i + 1] - sy);
      }
      cx.stroke();
      // continue the SAME path (no beginPath) — keeps it connected
      drawn = n;
    }
    raf = requestAnimationFrame(tick);
  }

  /* --- pointer handlers --- */
  cv.addEventListener('pointerdown', function (e) {
    if (!on || e.button !== 0 || e.target !== cv) return;
    e.preventDefault();
    cv.setPointerCapture(e.pointerId);
    drawing = true;
    // store document coords
    var dx = e.clientX + window.scrollX, dy = e.clientY + window.scrollY;
    pts = [dx, dy];
    drawn = 0;
    // set style once for whole stroke
    cx.globalCompositeOperation = erasing ? 'destination-out' : 'source-over';
    cx.strokeStyle = color;
    cx.lineWidth = erasing ? penW * 4 : penW;
    cx.lineCap = 'round';
    cx.lineJoin = 'round';
    // start rAF loop
    if (!raf) raf = requestAnimationFrame(tick);
  });

  cv.addEventListener('pointermove', function (e) {
    if (!drawing) return;
    // just push coords — rAF will render them
    pts.push(e.clientX + window.scrollX, e.clientY + window.scrollY);
  });

  function stop() {
    if (!drawing) return;
    drawing = false;
    if (pts.length >= 4) {
      strokes.push({ c: color, w: penW, er: erasing, p: pts.slice() });
    }
    pts = []; drawn = 0;
    // full repaint to clean up
    paint();
  }
  cv.addEventListener('pointerup', stop);
  cv.addEventListener('pointercancel', stop);
})();
