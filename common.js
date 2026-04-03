/* ============================================================
   Common utilities: Dark Mode + Annotate/Draw
   Auto-injects ONLY if not already present on the page.
   ============================================================ */
(function () {
  'use strict';

  /* ═══════════════════════════════════════════════
     1. DARK MODE TOGGLE (skip if already present)
     ═══════════════════════════════════════════════ */
  if (!document.querySelector('.dm-toggle') && !document.getElementById('themeToggle')) {
    // Inject dark-mode CSS
    var dmCSS = document.createElement('style');
    dmCSS.id = 'common-dark-mode';
    dmCSS.textContent =
      '.cm-dm-toggle{position:fixed;top:16px;right:16px;z-index:99999;width:44px;height:44px;' +
      'border-radius:50%;border:1.5px solid #d4cfc5;background:#fdfbf7;color:#2c2c2c;' +
      'cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:20px;' +
      'box-shadow:0 2px 8px rgba(0,0,0,.08);transition:all .3s cubic-bezier(.4,0,.2,1)}' +
      '.cm-dm-toggle:hover{transform:rotate(30deg) scale(1.1);background:#1a3c5e;color:#fff;border-color:#1a3c5e}' +
      '[data-theme="dark"] .cm-dm-toggle{border-color:#3a3d44;background:#1a1d23;color:#e0ddd5}' +
      '[data-theme="dark"] .cm-dm-toggle:hover{background:#5ea3e0;color:#fff;border-color:#5ea3e0}' +
      /* Core dark overrides */
      '[data-theme="dark"]{color-scheme:dark}' +
      '[data-theme="dark"] body{background:#141720!important;color:#d8d5cd!important}' +
      '[data-theme="dark"] body div,[data-theme="dark"] body p,' +
      '[data-theme="dark"] body span,[data-theme="dark"] body li,' +
      '[data-theme="dark"] body td,[data-theme="dark"] body th,' +
      '[data-theme="dark"] body label,[data-theme="dark"] body dt,' +
      '[data-theme="dark"] body dd,[data-theme="dark"] body blockquote,' +
      '[data-theme="dark"] body figcaption,[data-theme="dark"] body small,' +
      '[data-theme="dark"] body em,[data-theme="dark"] body i,' +
      '[data-theme="dark"] body summary,[data-theme="dark"] body legend,' +
      '[data-theme="dark"] body details,[data-theme="dark"] body a,' +
      '[data-theme="dark"] body strong,[data-theme="dark"] body b{' +
      'color:#d8d5cd!important;background-color:transparent!important}' +
      '[data-theme="dark"] h1,[data-theme="dark"] h2,[data-theme="dark"] h3,' +
      '[data-theme="dark"] h4,[data-theme="dark"] h5,[data-theme="dark"] h6{' +
      'color:#e8e5dd!important;background-color:transparent!important}' +
      '[data-theme="dark"] table{background:#1e2128!important;border-color:#3a3d44!important}' +
      '[data-theme="dark"] th{background:#2a3a50!important;color:#e0ddd5!important}' +
      '[data-theme="dark"] td{background:#1e2128!important;border-color:#3a3d44!important}' +
      '[data-theme="dark"] pre,[data-theme="dark"] code{background:#22262e!important;color:#d8d5cd!important}' +
      '[data-theme="dark"] .exam-note,[data-theme="dark"] .study-note,' +
      '[data-theme="dark"] .callout{background:#22262e!important;border-color:#3a3d44!important}' +
      '[data-theme="dark"] .figure-container,[data-theme="dark"] figure{background:#1e2128!important;border-color:#3a3d44!important}' +
      '[data-theme="dark"] hr{border-color:#3a3d44!important}' +
      '[data-theme="dark"] .print-btn{background:#22262e!important;color:#d8d5cd!important;border-color:#3a3d44!important}' +
      '[data-theme="dark"] svg text{fill:#d8d5cd}' +
      '[data-theme="dark"] input,[data-theme="dark"] textarea,[data-theme="dark"] select{background:#22262e!important;color:#d8d5cd!important;border-color:#3a3d44!important}' +
      '@media print{.cm-dm-toggle{display:none!important}}';
    document.head.appendChild(dmCSS);

    // Create toggle button
    var dmBtn = document.createElement('button');
    dmBtn.className = 'cm-dm-toggle';
    dmBtn.setAttribute('aria-label', 'Toggle dark mode');
    var html = document.documentElement;
    var saved = localStorage.getItem('theme');
    if (saved) html.setAttribute('data-theme', saved);
    dmBtn.innerHTML = html.getAttribute('data-theme') === 'dark' ? '&#9788;' : '&#9790;';
    document.body.appendChild(dmBtn);

    dmBtn.addEventListener('click', function () {
      var next = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      html.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
      dmBtn.innerHTML = next === 'dark' ? '&#9788;' : '&#9790;';
    });
  } else {
    // Ensure saved theme is applied even if toggle already exists
    var html = document.documentElement;
    var saved = localStorage.getItem('theme');
    if (saved && !html.getAttribute('data-theme')) html.setAttribute('data-theme', saved);
  }

  /* ═══════════════════════════════════════════════
     2. ANNOTATE / DRAW (skip if already present)
     ═══════════════════════════════════════════════ */
  if (document.querySelector('.dw-btn') || document.querySelector('.dw-cv')) return;

  var on = false, drawing = false, erasing = false;
  var COLORS = ['#e63946','#1a365d','#2d6a4f','#e67e22','#7c3aed','#000'];
  var color = COLORS[0], penW = 3;
  var strokes = [];
  var pts = [];
  var drawn = 0;
  var raf = 0;

  var st = document.createElement('style');
  st.textContent =
    '.dw-btn{position:fixed;bottom:70px;right:24px;z-index:10010;width:46px;height:46px;border-radius:50%;border:none;background:#1a365d;color:#fff;font-size:21px;cursor:pointer;box-shadow:0 2px 8px rgba(0,0,0,.3);display:flex;align-items:center;justify-content:center;transition:background .15s,transform .15s}.dw-btn:hover{transform:scale(1.08)}.dw-btn.on{background:#c9a84c;color:#1a365d}' +
    '.dw-tb{position:fixed;bottom:124px;right:24px;z-index:10010;background:#fff;border-radius:10px;padding:8px;box-shadow:0 4px 14px rgba(0,0,0,.22);display:none;flex-direction:column;gap:5px;align-items:center;font:12px/1 sans-serif;pointer-events:auto}.dw-tb.show{display:flex}' +
    '.dw-dot{width:20px;height:20px;border-radius:50%;border:2px solid transparent;cursor:pointer;transition:.12s}.dw-dot:hover,.dw-dot.on{border-color:#222;transform:scale(1.12)}' +
    '.dw-b{background:#f0f0f0;border:1px solid #ccc;border-radius:5px;padding:3px 8px;cursor:pointer;text-align:center;width:100%}.dw-b:hover{background:#e0e0e0}.dw-b.on{background:#1a365d;color:#fff;border-color:#1a365d}' +
    '.dw-cv{position:fixed;top:0;left:0;width:100%;height:100%;z-index:10000;pointer-events:none;touch-action:none}.dw-cv.on{pointer-events:auto;cursor:crosshair}' +
    '@media print{.dw-btn,.dw-tb,.dw-cv{display:none!important}}';
  document.head.appendChild(st);

  var cv = document.createElement('canvas');
  cv.className = 'dw-cv';
  document.body.appendChild(cv);
  cv.addEventListener('wheel', function (e) { window.scrollBy(0, e.deltaY); paint(); }, { passive: true });
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

  function paint() {
    var sx = window.scrollX, sy = window.scrollY;
    cx.clearRect(0, 0, cv.width, cv.height);
    for (var s = 0; s < strokes.length; s++) {
      var sk = strokes[s], p = sk.p;
      if (p.length < 4) continue;
      cx.globalCompositeOperation = sk.er ? 'destination-out' : 'source-over';
      cx.strokeStyle = sk.c;
      cx.lineWidth = sk.er ? sk.w * 4 : sk.w;
      cx.lineCap = 'round'; cx.lineJoin = 'round';
      cx.beginPath();
      cx.moveTo(p[0] - sx, p[1] - sy);
      for (var i = 2; i < p.length; i += 2) cx.lineTo(p[i] - sx, p[i + 1] - sy);
      cx.stroke();
    }
  }
  window.addEventListener('scroll', paint);

  var btn = document.createElement('button');
  btn.className = 'dw-btn'; btn.title = 'Annotate / Draw'; btn.innerHTML = '&#9998;';
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

  function tick() {
    if (!drawing) { raf = 0; return; }
    var n = pts.length;
    if (drawn < n) {
      var sx = window.scrollX, sy = window.scrollY;
      if (drawn === 0) { cx.beginPath(); cx.moveTo(pts[0] - sx, pts[1] - sy); drawn = 2; }
      for (var i = drawn; i < n; i += 2) cx.lineTo(pts[i] - sx, pts[i + 1] - sy);
      cx.stroke();
      drawn = n;
    }
    raf = requestAnimationFrame(tick);
  }

  cv.addEventListener('pointerdown', function (e) {
    if (!on || e.button !== 0 || e.target !== cv) return;
    e.preventDefault();
    cv.setPointerCapture(e.pointerId);
    drawing = true;
    var dx = e.clientX + window.scrollX, dy = e.clientY + window.scrollY;
    pts = [dx, dy]; drawn = 0;
    cx.globalCompositeOperation = erasing ? 'destination-out' : 'source-over';
    cx.strokeStyle = color;
    cx.lineWidth = erasing ? penW * 4 : penW;
    cx.lineCap = 'round'; cx.lineJoin = 'round';
    if (!raf) raf = requestAnimationFrame(tick);
  });

  cv.addEventListener('pointermove', function (e) {
    if (!drawing) return;
    pts.push(e.clientX + window.scrollX, e.clientY + window.scrollY);
  });

  function stop() {
    if (!drawing) return;
    drawing = false;
    if (pts.length >= 4) strokes.push({ c: color, w: penW, er: erasing, p: pts.slice() });
    pts = []; drawn = 0;
    paint();
  }
  cv.addEventListener('pointerup', stop);
  cv.addEventListener('pointercancel', stop);
})();
