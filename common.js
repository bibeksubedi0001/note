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
     2. NAVIGATION BAR (back + prev/next arrows)
     ═══════════════════════════════════════════════ */
  if (!document.querySelector('.cm-nav-bar')) {
    var path = window.location.pathname.replace(/\\/g, '/');
    var file = path.split('/').pop() || '';
    var dir = '';
    var m = path.match(/\/(gis|TES|gw\/Theory|gw\/Numerical|Structure)\//i);
    if (m) dir = m[1].replace(/\\/g, '/');

    var NAV = {
      'gis': {
        index: 'index.html',
        label: 'GIS & Remote Sensing',
        chapters: [
          { f: 'chapter1.html',  t: 'Ch 1: Introduction & Overview' },
          { f: 'chapter2.html',  t: 'Ch 2: GIS and Maps' },
          { f: 'chapter3.html',  t: 'Ch 3: Spatial Data Models' },
          { f: 'chapter4.html',  t: 'Ch 4: Data Sources' },
          { f: 'chapter5.html',  t: 'Ch 5: Database Concepts' },
          { f: 'chapter6.html',  t: 'Ch 6: Vector Analysis' },
          { f: 'chapter7.html',  t: 'Ch 7: Spatial Analysis' },
          { f: 'chapter8.html',  t: 'Ch 8: Surface Model' },
          { f: 'chapter9.html',  t: 'Ch 9: River Network Generation' },
          { f: 'chapter10.html', t: 'Ch 10: GPS' },
          { f: 'chapter11.html', t: 'Ch 11: Remote Sensing' },
          { f: 'chapter12.html', t: 'Ch 12: Making Maps' },
          { f: 'exam-answers.html', t: 'Exam Answers' }
        ]
      },
      'TES': {
        index: 'index_tes.html',
        label: 'TES',
        chapters: [
          { f: 'chapter1_updated.html', t: 'Ch 1: Technology' },
          { f: 'chapter2.html',         t: 'Ch 2: Development Approach' },
          { f: 'chapter3.html',         t: 'Ch 3: History of Civilization' },
          { f: 'chapter4.html',         t: 'Ch 4: Environment' },
          { f: 'chapter5.html',         t: 'Ch 5: Water & Air Pollution' },
          { f: 'chapter6.html',         t: 'Ch 6: Climate Change' }
        ]
      },
      'gw/Theory': {
        index: '../index.html',
        label: 'Groundwater Theory',
        chapters: [
          { f: 'chapter1_groundwater_old.html',       t: 'Ch 1: Introduction' },
          { f: 'chapter2_groundwater_motion_old.html', t: 'Ch 2: Groundwater Motion' },
          { f: 'chapter3_flow_theory_old.html',        t: 'Ch 3: Flow Theory' },
          { f: 'chapter4_well_hydraulics_old.html', t: 'Ch 4: Well Hydraulics' },
          { f: 'chapter5_pumping_test.html',       t: 'Ch 5: Pumping Test' },
          { f: 'chapter6_groundwater_exploration.html', t: 'Ch 6: GW Exploration' },
          { f: 'chapter7_water_well_design.html',  t: 'Ch 7: Water Well Design' },
          { f: 'chapter8_pumps.html',              t: 'Ch 8: Pumps' },
          { f: 'chapter9_groundwater_nepal.html',  t: 'Ch 9: GW in Nepal' },
          { f: 'groundwater_questions_by_chapter.html', t: 'Questions by Chapter' },
          { f: 'numericals_solved.html',           t: 'Solved Numericals' }
        ]
      },
      'gw/Numerical': {
        index: 'index.html',
        label: 'Groundwater Numericals',
        chapters: [
          { f: 'chapter2.html', t: 'Ch 2' },
          { f: 'chapter3.html', t: 'Ch 3' },
          { f: 'chapter4.html', t: 'Ch 4' },
          { f: 'chapter5.html', t: 'Ch 5' },
          { f: 'chapter7.html', t: 'Ch 7' },
          { f: 'chapter9.html', t: 'Ch 9' }
        ]
      },
      'Structure': {
        index: 'index.html',
        label: 'Structural Analysis & FEM',
        chapters: [
          { f: 'chapter1_the.html',  t: 'Ch 1: Computational Techniques' },
          { f: 'chapter2.html',      t: 'Ch 2: Linear Equations' },
          { f: 'chapter3thr.html',   t: 'Ch 3: Elasticity in Solids' },
          { f: 'chapter4the.html',   t: 'Ch 4: FEM Theory' },
          { f: '4.1_Introduction-_FEM.html', t: '4.1: FEM Introduction' },
          { f: '4.2_Bar_Element.html',       t: '4.2: Bar Element' },
          { f: '4.3_Truss_Element.html',     t: '4.3: Truss Element' },
          { f: '4.4_Shape_Functions.html',   t: '4.4: Shape Functions' },
          { f: '4.4_Shape_Functions_Solved_Questions_backup.html', t: '4.4: Shape Functions (Solved)' },
          { f: '4.5_Beam_Element.html',      t: '4.5: Beam Element' },
          { f: '4.5_Beam_Element_Solved_Questions.html', t: '4.5: Beam Element (Solved)' },
          { f: '4.6_CST_Element.html',       t: '4.6: CST Element' },
          { f: '4.6_CST_Element_Solved_Questions.html', t: '4.6: CST Element (Solved)' }
        ]
      },
      'Water': {
        index: 'index.html',
        label: 'Computational Technique (Water)',
        chapters: [
          { f: 'chapter 5.html',  t: 'Ch 5: Numerical Methods' },
          { f: 'chapter6.html',   t: 'Ch 6: Method of Characteristics' },
          { f: 'chapter7.html',   t: 'Ch 7: Groundwater Flow' },
          { f: 'dam.html',        t: 'Exam Question Bank' },
          { f: 'rk_assignment.html', t: 'Runge-Kutta Assignment' },
          { f: '5.4.3 Stability of Numerical Solution of Kinematic Wave Model.html', t: '5.4.3: Kinematic Wave Stability' },
          { f: '5.5.2 Solution by Explicit Scheme .html', t: '5.5.2: Explicit Scheme' },
          { f: 'Linear Scheme.html', t: 'Linear Scheme' }
        ]
      }
    };

    var subj = NAV[dir];
    if (subj && file && file !== 'index.html' && file !== 'index_tes.html') {
      var idx = -1;
      for (var i = 0; i < subj.chapters.length; i++) {
        if (subj.chapters[i].f === file) { idx = i; break; }
      }
      if (idx >= 0) {
        // Inject nav CSS
        var navCSS = document.createElement('style');
        navCSS.textContent =
          '.cm-nav-bar{position:fixed;top:0;left:0;right:0;z-index:9990;background:#fff;border-bottom:1px solid #d0d0d0;display:flex;align-items:center;justify-content:space-between;padding:6px 16px;font-family:system-ui,-apple-system,sans-serif;font-size:13px}' +
          '.cm-nav-bar a{text-decoration:none;color:#111;display:flex;align-items:center;gap:4px;padding:4px 8px;border-radius:4px;transition:background .15s}' +
          '.cm-nav-bar a:hover{background:#f0f0f0}' +
          '.cm-nav-back{font-weight:600}' +
          '.cm-nav-arrows{display:flex;gap:2px}' +
          '.cm-nav-arrows a{min-width:32px;justify-content:center}' +
          '.cm-nav-arrows .disabled{color:#ccc;pointer-events:none}' +
          '.cm-nav-title{color:#666;max-width:40vw;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}' +
          '[data-theme="dark"] .cm-nav-bar{background:#1a1d23;border-color:#3a3d44}' +
          '[data-theme="dark"] .cm-nav-bar a{color:#d8d5cd}' +
          '[data-theme="dark"] .cm-nav-bar a:hover{background:#2a2d33}' +
          '[data-theme="dark"] .cm-nav-arrows .disabled{color:#444}' +
          '[data-theme="dark"] .cm-nav-title{color:#888}' +
          '@media print{.cm-nav-bar{display:none!important}}' +
          'body{padding-top:42px!important}';
        document.head.appendChild(navCSS);

        var bar = document.createElement('nav');
        bar.className = 'cm-nav-bar';

        var prev = idx > 0 ? subj.chapters[idx - 1] : null;
        var next = idx < subj.chapters.length - 1 ? subj.chapters[idx + 1] : null;

        bar.innerHTML =
          '<a href="' + subj.index + '" class="cm-nav-back">' +
          '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg> ' +
          subj.label + '</a>' +
          '<span class="cm-nav-title">' + subj.chapters[idx].t + '</span>' +
          '<span class="cm-nav-arrows">' +
          (prev ? '<a href="' + prev.f + '" title="' + prev.t + '">' : '<span class="disabled">') +
          '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 18l-6-6 6-6"/></svg>' +
          (prev ? '</a>' : '</span>') +
          (next ? '<a href="' + next.f + '" title="' + next.t + '">' : '<span class="disabled">') +
          '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>' +
          (next ? '</a>' : '</span>') +
          '</span>';

        document.body.insertBefore(bar, document.body.firstChild);
      }
    }
  }

  /* ═══════════════════════════════════════════════
     3. ANNOTATE / DRAW (skip if already present)
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
