/* ============================================================
   Common utilities: Dark Mode + Nav + Annotate/Draw + Extras
   Auto-injects ONLY if not already present on the page.
   ============================================================ */
(function () {
  'use strict';

  /* ═══════════════════════════════════════════════
     0. MATHJAX INLINE FIX + SCROLL PROGRESS BAR
     ═══════════════════════════════════════════════ */
  /* Fix MathJax inline math rendering as block */
  var mjxFix = document.createElement('style');
  mjxFix.textContent =
    'mjx-container[jax="CHTML"]:not([display="true"]){display:inline!important;overflow-x:visible!important}' +
    'mjx-container[jax="SVG"]:not([display="true"]){display:inline!important}' +
    '.MathJax:not(.MathJax_Display){display:inline!important}';
  document.head.appendChild(mjxFix);

  if (!document.querySelector('.cm-scroll-progress')) {
    var progCSS = document.createElement('style');
    progCSS.textContent =
      '.cm-scroll-progress{position:fixed;top:0;left:0;height:3px;z-index:99998;border-radius:0 2px 2px 0;' +
      'background:linear-gradient(90deg,#667eea,#764ba2,#f093fb,#f5576c);background-size:300% 100%;' +
      'animation:cm-grad-shift 3s ease infinite;width:0;transition:width .15s linear}' +
      '@keyframes cm-grad-shift{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}' +
      '[data-theme="dark"] .cm-scroll-progress{background:linear-gradient(90deg,#818cf8,#a78bfa,#c084fc,#e879f9);background-size:300% 100%;' +
      'animation:cm-grad-shift 3s ease infinite}' +
      /* scroll percentage badge */
      '.cm-scroll-pct{position:fixed;top:10px;left:16px;z-index:99999;' +
      'font:600 12px/1 system-ui,sans-serif;padding:4px 10px;border-radius:12px;' +
      'background:rgba(30,30,30,.75);color:#fff;backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);' +
      'opacity:0;transition:opacity .3s ease;pointer-events:none;letter-spacing:.3px}' +
      '.cm-scroll-pct.visible{opacity:1}' +
      '[data-theme="dark"] .cm-scroll-pct{background:rgba(255,255,255,.15);color:#e5e7eb}' +
      '@media print{.cm-scroll-progress,.cm-scroll-pct{display:none!important}}';
    document.head.appendChild(progCSS);

    var progBar = document.createElement('div');
    progBar.className = 'cm-scroll-progress';
    document.body.appendChild(progBar);

    var pctBadge = document.createElement('div');
    pctBadge.className = 'cm-scroll-pct';
    pctBadge.textContent = '0%';
    document.body.appendChild(pctBadge);

    var hideTimer = null;
    function updateProgress() {
      var scrollTop = window.scrollY || document.documentElement.scrollTop;
      var docHeight = document.documentElement.scrollHeight - window.innerHeight;
      var pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
      progBar.style.width = pct + '%';
      pctBadge.textContent = Math.round(pct) + '%';
      pctBadge.classList.add('visible');
      clearTimeout(hideTimer);
      hideTimer = setTimeout(function () { pctBadge.classList.remove('visible'); }, 1500);
    }
    window.addEventListener('scroll', updateProgress, { passive: true });
    updateProgress();
  }

  /* ═══════════════════════════════════════════════
     1. DARK MODE
     Toggle button + fixInline always injected.
     Dark content CSS only for pages without #dark-mode-styles.
     ═══════════════════════════════════════════════ */
  var html = document.documentElement;
  var saved = localStorage.getItem('theme');
  if (saved) html.setAttribute('data-theme', saved);

  // Toggle button styles (always needed)
  var btnCSS = document.createElement('style');
  btnCSS.textContent =
    '.cm-dm-toggle{position:fixed;top:16px;right:16px;z-index:99999;width:44px;height:44px;' +
    'border-radius:14px;border:1px solid rgba(0,0,0,.08);' +
    'background:rgba(255,255,255,.8);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);' +
    'color:#374151;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:20px;' +
    'box-shadow:0 4px 12px rgba(0,0,0,.06);transition:all .35s cubic-bezier(.4,0,.2,1)}' +
    '.cm-dm-toggle:hover{transform:scale(1.1) rotate(15deg);box-shadow:0 6px 20px rgba(0,0,0,.12)}' +
    '.cm-dm-toggle:active{transform:scale(.95)}' +
    '[data-theme="dark"] .cm-dm-toggle{border-color:rgba(255,255,255,.08);background:rgba(30,30,40,.8);color:#e5e7eb;' +
    'box-shadow:0 4px 12px rgba(0,0,0,.3)}' +
    '[data-theme="dark"] .cm-dm-toggle:hover{box-shadow:0 6px 20px rgba(99,102,241,.3)}' +
    '@media print{.cm-dm-toggle{display:none!important}}';
  document.head.appendChild(btnCSS);

  // Dark content CSS — only if page doesn't have its own comprehensive dark styles
  if (!document.getElementById('dark-mode-styles')) {
    var dmCSS = document.createElement('style');
    dmCSS.id = 'common-dark-mode';
    dmCSS.textContent =
      '[data-theme="dark"]{color-scheme:dark}' +
      '[data-theme="dark"] body{background:#0f0f13!important;color:#d8d5cd!important}' +
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
      '[data-theme="dark"] h1,[data-theme="dark"] h4,[data-theme="dark"] h5,[data-theme="dark"] h6{' +
      'color:#e8e5dd!important;background-color:transparent!important}' +
      '[data-theme="dark"] main h2,[data-theme="dark"] main h3{' +
      'color:#e8805a!important;font-style:italic!important;background-color:transparent!important}' +
      '[data-theme="dark"] h2:not(main h2),[data-theme="dark"] h3:not(main h3){' +
      'color:#e8e5dd!important;background-color:transparent!important}' +
      '[data-theme="dark"] table{background:#1a1a22!important;border-color:#2a2a35!important}' +
      '[data-theme="dark"] th{background:#1f1f2a!important;color:#e0ddd5!important}' +
      '[data-theme="dark"] td{background:#1a1a22!important;border-color:#2a2a35!important}' +
      '[data-theme="dark"] pre,[data-theme="dark"] code{background:#1a1a22!important;color:#d8d5cd!important}' +
      '[data-theme="dark"] .exam-note,[data-theme="dark"] .study-note,' +
      '[data-theme="dark"] .callout{background:#1f1f2a!important;border-color:#2a2a35!important}' +
      '[data-theme="dark"] .figure-container,[data-theme="dark"] figure{background:#1a1a22!important;border-color:#2a2a35!important}' +
      '[data-theme="dark"] hr{border-color:#2a2a35!important}' +
      '[data-theme="dark"] .print-btn{background:#1f1f2a!important;color:#d8d5cd!important;border-color:#2a2a35!important}' +
      '[data-theme="dark"] svg text{fill:#d8d5cd}' +
      '[data-theme="dark"] input,[data-theme="dark"] textarea,[data-theme="dark"] select{background:#1a1a22!important;color:#d8d5cd!important;border-color:#2a2a35!important}';
    document.head.appendChild(dmCSS);
  }

  // Always inject toggle button
  var dmBtn = document.createElement('button');
  dmBtn.className = 'cm-dm-toggle';
  dmBtn.setAttribute('aria-label', 'Toggle dark mode');
  dmBtn.innerHTML = html.getAttribute('data-theme') === 'dark' ? '&#9788;' : '&#9790;';
  document.body.appendChild(dmBtn);

  dmBtn.addEventListener('click', function () {
    var next = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    dmBtn.innerHTML = next === 'dark' ? '&#9788;' : '&#9790;';
    cmFixInline(next === 'dark');
  });

  /* fixInline — flip inline style="color/background" for dark mode */
  function cmLum(c) {
    if (!c) return -1;
    c = c.trim().toLowerCase();
    if (c === 'white' || c === '#fff' || c === '#ffffff') return 255;
    if (c === 'black' || c === '#000' || c === '#000000') return 0;
    var m = c.match(/rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)/);
    if (m) return (+m[1] + +m[2] + +m[3]) / 3;
    var hx = c.match(/^#([0-9a-f]{3,8})$/);
    if (hx) { var x = hx[1]; if (x.length === 3) x = x[0]+x[0]+x[1]+x[1]+x[2]+x[2];
      return (parseInt(x.substr(0,2),16)+parseInt(x.substr(2,2),16)+parseInt(x.substr(4,2),16))/3; }
    return -1;
  }
  function cmFixInline(dark) {
    var els = document.querySelectorAll('[style]');
    for (var i = 0; i < els.length; i++) {
      var el = els[i];
      if (el.namespaceURI && el.namespaceURI.indexOf('svg') !== -1) continue;
      if (el.closest && el.closest('svg')) continue;
      var st = el.style;
      if (dark) {
        if (st.backgroundColor && !el.getAttribute('data-dm-bg')) {
          el.setAttribute('data-dm-bg', st.backgroundColor);
          if (cmLum(st.backgroundColor) > 160) st.backgroundColor = '#1e222a';
        }
        if (st.background && !el.getAttribute('data-dm-bgf')) {
          el.setAttribute('data-dm-bgf', st.background);
          if (cmLum(st.background) > 160) st.background = '#1e222a';
        }
        if (st.color && !el.getAttribute('data-dm-fg')) {
          el.setAttribute('data-dm-fg', st.color);
          if (cmLum(st.color) < 100) st.color = '#d0cdc5';
        }
      } else {
        if (el.getAttribute('data-dm-bg')) { st.backgroundColor = el.getAttribute('data-dm-bg'); el.removeAttribute('data-dm-bg'); }
        if (el.getAttribute('data-dm-bgf')) { st.background = el.getAttribute('data-dm-bgf'); el.removeAttribute('data-dm-bgf'); }
        if (el.getAttribute('data-dm-fg')) { st.color = el.getAttribute('data-dm-fg'); el.removeAttribute('data-dm-fg'); }
      }
    }
  }
  /* Run fixInline on load if dark */
  if (html.getAttribute('data-theme') === 'dark') {
    if (document.readyState === 'loading')
      document.addEventListener('DOMContentLoaded', function () { cmFixInline(true); });
    else cmFixInline(true);
  }
  /* Watch for theme changes */
  if (typeof MutationObserver !== 'undefined') {
    new MutationObserver(function (muts) {
      for (var i = 0; i < muts.length; i++) {
        if (muts[i].attributeName === 'data-theme') {
          cmFixInline(html.getAttribute('data-theme') === 'dark');
            break;
          }
        }
      }).observe(html, { attributes: true, attributeFilter: ['data-theme'] });
  }

  /* ═══════════════════════════════════════════════
     2. NAVIGATION BAR (back + prev/next arrows)
     ═══════════════════════════════════════════════ */
  if (!document.querySelector('.cm-nav-bar')) {
    var path = window.location.pathname.replace(/\\/g, '/');
    var file = decodeURIComponent(path.split('/').pop() || '');
    var dir = '';
    var m = path.match(/\/(gis|TES|gw\/Theory|gw\/Numerical|Structure|Water)\//i);
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
        label: 'Groundwater Engineering',
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
      'gw/Summary_Note': {
        index: 'index.html',
        label: 'GW Summary Notes',
        chapters: [
          { f: 'chapter1.html', t: 'Ch 1: Occurrence of Groundwater' },
          { f: 'chapter2.html', t: 'Ch 1–2: Numericals (Properties & Darcy)' },
          { f: 'chapter3.html', t: 'Ch 3: Flow Theory & Numericals' },
          { f: 'chapter4.html', t: 'Ch 4: Well Hydraulics' },
          { f: 'chapter5.html', t: 'Ch 5: Pumping Test' },
          { f: 'chapter6.html', t: 'Ch 6–7: Exploration & Well Design' },
          { f: 'chapter7.html', t: 'Ch 8–9: Pumps & GW in Nepal' }
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
        if (subj.chapters[i].f === file || encodeURIComponent(subj.chapters[i].f) === file) { idx = i; break; }
      }
      if (idx >= 0) {
        // Inject nav CSS
        var navCSS = document.createElement('style');
        navCSS.textContent =
          '.cm-nav-bar{position:fixed;top:0;left:0;right:0;z-index:9990;' +
          'background:rgba(255,255,255,.75);backdrop-filter:blur(16px) saturate(180%);-webkit-backdrop-filter:blur(16px) saturate(180%);' +
          'border-bottom:1px solid rgba(0,0,0,.06);display:flex;align-items:center;justify-content:space-between;' +
          'padding:8px 20px;font-family:"Inter",system-ui,-apple-system,sans-serif;font-size:13px;' +
          'transition:background .3s,border-color .3s}' +
          '.cm-nav-bar a{text-decoration:none;color:#374151;display:flex;align-items:center;gap:6px;' +
          'padding:6px 12px;border-radius:10px;transition:all .2s cubic-bezier(.4,0,.2,1);font-weight:500}' +
          '.cm-nav-bar a:hover{background:rgba(99,102,241,.08);color:#6366f1}' +
          '.cm-nav-back{font-weight:600}' +
          '.cm-nav-arrows{display:flex;gap:4px}' +
          '.cm-nav-arrows a{min-width:36px;height:36px;justify-content:center;border-radius:10px;padding:0}' +
          '.cm-nav-arrows a:hover{background:rgba(99,102,241,.1);color:#6366f1;transform:scale(1.05)}' +
          '.cm-nav-arrows .disabled{color:#ccc;pointer-events:none}' +
          '.cm-nav-title{color:#6b7280;max-width:40vw;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-size:12px}' +
          '[data-theme="dark"] .cm-nav-bar{background:rgba(15,15,19,.75);border-color:rgba(255,255,255,.05)}' +
          '[data-theme="dark"] .cm-nav-bar a{color:#d1d5db}' +
          '[data-theme="dark"] .cm-nav-bar a:hover{background:rgba(129,140,248,.1);color:#818cf8}' +
          '[data-theme="dark"] .cm-nav-arrows .disabled{color:#333}' +
          '[data-theme="dark"] .cm-nav-title{color:#6b7280}' +
          '@media print{.cm-nav-bar{display:none!important}}' +
          'body{padding-top:50px!important}';
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
  var COLORS = ['#e63946','#1a365d','#2d6a4f','#e67e22','#7c3aed','#000000','#ffffff','#f0f8ff','#0ea5e9','#ec4899','#14b8a6','#d97706','#dc2626','#059669','#4f46e5','#f43f5e','#84cc16','#c0c0c0','#fffffe','#fff8dc','#b9f2ff','#ffd700'];
  var GLOW_COLORS = {'#b9f2ff':true,'#ffd700':true};
  var color = COLORS[0], penW = 3;
  var strokes = [];
  var pts = [];
  var drawn = 0;
  var raf = 0;

  var st = document.createElement('style');
  st.textContent =
    '.dw-btn{position:fixed;bottom:70px;right:24px;z-index:10010;width:46px;height:46px;border-radius:14px;border:none;' +
    'background:rgba(99,102,241,.9);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);' +
    'color:#fff;font-size:21px;cursor:pointer;box-shadow:0 4px 14px rgba(99,102,241,.35);' +
    'display:flex;align-items:center;justify-content:center;transition:all .3s cubic-bezier(.34,1.56,.64,1)}' +
    '.dw-btn:hover{transform:scale(1.12);box-shadow:0 6px 20px rgba(99,102,241,.45)}' +
    '.dw-btn:active{transform:scale(.95)}' +
    '.dw-btn.on{background:rgba(234,179,8,.9);color:#1a1a2e;box-shadow:0 4px 14px rgba(234,179,8,.35)}' +
    '[data-theme="dark"] .dw-btn{background:rgba(129,140,248,.85);box-shadow:0 4px 14px rgba(129,140,248,.3)}' +
    '[data-theme="dark"] .dw-btn.on{background:rgba(250,204,21,.85);color:#1a1a2e}' +
    '.dw-tb{position:fixed;bottom:124px;right:24px;z-index:10010;' +
    'background:rgba(255,255,255,.9);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);' +
    'border:1px solid rgba(0,0,0,.06);border-radius:16px;padding:12px;' +
    'box-shadow:0 8px 30px rgba(0,0,0,.12);display:none;flex-direction:column;gap:6px;align-items:center;' +
    'font:12px/1 "Inter",system-ui,sans-serif;pointer-events:auto;transition:all .2s}' +
    '.dw-tb.show{display:flex}' +
    '[data-theme="dark"] .dw-tb{background:rgba(20,20,30,.9);border-color:rgba(255,255,255,.06);box-shadow:0 8px 30px rgba(0,0,0,.4)}' +
    '.dw-palette{display:flex;flex-wrap:wrap;gap:4px;width:92px;justify-content:center}'+
    '.dw-dot{width:16px;height:16px;border-radius:50%;border:2px solid transparent;cursor:pointer;transition:.2s cubic-bezier(.34,1.56,.64,1)}' +
    '.dw-dot:hover,.dw-dot.on{border-color:var(--accent,#6366f1);transform:scale(1.2);box-shadow:0 2px 8px rgba(0,0,0,.15)}' +
    '.dw-dot.glow-diamond{animation:glowDiamond 1.6s ease-in-out infinite alternate;box-shadow:0 0 6px 2px rgba(185,242,255,.7)}' +
    '.dw-dot.glow-golden{animation:glowGolden 1.6s ease-in-out infinite alternate;box-shadow:0 0 6px 2px rgba(255,215,0,.7)}' +
    '@keyframes glowDiamond{0%{box-shadow:0 0 4px 1px rgba(185,242,255,.5)}100%{box-shadow:0 0 12px 4px rgba(185,242,255,.9)}}' +
    '@keyframes glowGolden{0%{box-shadow:0 0 4px 1px rgba(255,215,0,.5)}100%{box-shadow:0 0 12px 4px rgba(255,215,0,.9)}}' +
    '.dw-b{background:rgba(0,0,0,.04);border:1px solid rgba(0,0,0,.08);border-radius:8px;padding:5px 10px;cursor:pointer;text-align:center;width:100%;' +
    'font-weight:500;transition:all .15s}' +
    '.dw-b:hover{background:rgba(99,102,241,.08);border-color:rgba(99,102,241,.2);color:#6366f1}' +
    '.dw-b.on{background:#6366f1;color:#fff;border-color:#6366f1}' +
    '[data-theme="dark"] .dw-b{background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.08);color:#d1d5db}' +
    '[data-theme="dark"] .dw-b:hover{background:rgba(129,140,248,.15);border-color:rgba(129,140,248,.3);color:#818cf8}' +
    '[data-theme="dark"] .dw-b.on{background:#818cf8;color:#fff;border-color:#818cf8}' +
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
      if (!sk.er && GLOW_COLORS[sk.c]) { cx.shadowColor = sk.c; cx.shadowBlur = 10; } else { cx.shadowColor = 'transparent'; cx.shadowBlur = 0; }
      cx.beginPath();
      cx.moveTo(p[0] - sx, p[1] - sy);
      for (var i = 2; i < p.length; i += 2) cx.lineTo(p[i] - sx, p[i + 1] - sy);
      cx.stroke();
      cx.shadowColor = 'transparent'; cx.shadowBlur = 0;
    }
  }
  window.addEventListener('scroll', paint);

  var btn = document.createElement('button');
  btn.className = 'dw-btn'; btn.title = 'Annotate / Draw'; btn.innerHTML = '&#9998;';
  document.body.appendChild(btn);

  var tb = document.createElement('div'); tb.className = 'dw-tb';
  var pal = document.createElement('div');
  pal.className = 'dw-palette';
  COLORS.forEach(function (c) {
    var d = document.createElement('div');
    d.className = 'dw-dot' + (c === color ? ' on' : '') + (c === '#b9f2ff' ? ' glow-diamond' : '') + (c === '#ffd700' ? ' glow-golden' : '');
    d.style.background = c;
    if (c === '#fffffe') d.style.border = '2px solid #ccc';
    d.onclick = function () {
      color = c; erasing = false; erBtn.classList.remove('on');
      pal.querySelectorAll('.dw-dot').forEach(function (x) { x.classList.remove('on'); });
      d.classList.add('on');
    };
    pal.appendChild(d);
  });
  tb.appendChild(pal);
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
    if (!erasing && GLOW_COLORS[color]) { cx.shadowColor = color; cx.shadowBlur = 10; } else { cx.shadowColor = 'transparent'; cx.shadowBlur = 0; }
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

  /* Keyboard shortcut: C to clear annotations (works anytime, any page) */
  document.addEventListener('keydown', function (e) {
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.tagName === 'SELECT' || e.target.isContentEditable) return;
    if ((e.key === 'c' || e.key === 'C') && !e.ctrlKey && !e.metaKey && !e.altKey) {
      if (strokes.length) { strokes.length = 0; paint(); }
    }
  });

  /* ═══════════════════════════════════════════════
     4. SCROLL-TO-TOP BUTTON
     ═══════════════════════════════════════════════ */
  if (!document.querySelector('.cm-scroll-top')) {
    var stCSS = document.createElement('style');
    stCSS.textContent =
      '.cm-scroll-top{position:fixed;bottom:20px;right:24px;z-index:10005;width:42px;height:42px;border-radius:12px;border:none;' +
      'background:rgba(255,255,255,.8);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);' +
      'color:#374151;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:18px;' +
      'box-shadow:0 2px 10px rgba(0,0,0,.08);opacity:0;transform:translateY(10px);' +
      'transition:all .3s cubic-bezier(.4,0,.2,1);pointer-events:none}' +
      '.cm-scroll-top.visible{opacity:1;transform:translateY(0);pointer-events:auto}' +
      '.cm-scroll-top:hover{transform:translateY(-2px);box-shadow:0 4px 16px rgba(0,0,0,.12)}' +
      '.cm-scroll-top:active{transform:scale(.95)}' +
      '[data-theme="dark"] .cm-scroll-top{background:rgba(20,20,30,.8);color:#d1d5db;' +
      'box-shadow:0 2px 10px rgba(0,0,0,.3);border:1px solid rgba(255,255,255,.06)}' +
      '@media print{.cm-scroll-top{display:none!important}}';
    document.head.appendChild(stCSS);

    var stBtn = document.createElement('button');
    stBtn.className = 'cm-scroll-top';
    stBtn.setAttribute('aria-label', 'Scroll to top');
    stBtn.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M18 15l-6-6-6 6"/></svg>';
    document.body.appendChild(stBtn);

    stBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    window.addEventListener('scroll', function () {
      if (window.scrollY > 400) stBtn.classList.add('visible');
      else stBtn.classList.remove('visible');
    }, { passive: true });
  }

  /* ═══════════════════════════════════════════════
     5. SMOOTH ENTRANCE ANIMATION FOR CONTENT
     ═══════════════════════════════════════════════ */
  if ('IntersectionObserver' in window) {
    var revealCSS = document.createElement('style');
    revealCSS.textContent =
      '.cm-reveal{opacity:0;transform:translateY(16px);transition:opacity .5s cubic-bezier(.4,0,.2,1),transform .5s cubic-bezier(.4,0,.2,1)}' +
      '.cm-reveal.cm-visible{opacity:1;transform:translateY(0)}';
    document.head.appendChild(revealCSS);

    function initReveal() {
      var items = document.querySelectorAll('h2, h3, .figure, figure, .exam-note, .study-note, .callout, table, blockquote');
      var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('cm-visible');
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

      items.forEach(function (el) {
        if (!el.closest('.cm-nav-bar') && !el.closest('.dw-tb')) {
          el.classList.add('cm-reveal');
          observer.observe(el);
        }
      });
    }
    if (document.readyState === 'loading')
      document.addEventListener('DOMContentLoaded', initReveal);
    else
      setTimeout(initReveal, 100);
  }

})();
