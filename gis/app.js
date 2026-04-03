/* ============================================================
   GIS & Remote Sensing Study Guide – Shared Interactivity
   ============================================================ */

(function () {
  'use strict';

  // ---- Chapter data for navigation ----
  var chapters = [
    { file: 'chapter1.html',  title: 'Introduction and Overview of GIS and Software' },
    { file: 'chapter2.html',  title: 'GIS and Maps' },
    { file: 'chapter3.html',  title: 'Spatial Data Models' },
    { file: 'chapter4.html',  title: 'Data Sources' },
    { file: 'chapter5.html',  title: 'Database Concepts' },
    { file: 'chapter6.html',  title: 'Vector Analysis' },
    { file: 'chapter7.html',  title: 'Spatial Analysis' },
    { file: 'chapter8.html',  title: 'Surface Model' },
    { file: 'chapter9.html',  title: 'River Network Generation' },
    { file: 'chapter10.html', title: 'Global Positioning System (GPS)' },
    { file: 'chapter11.html', title: 'Introduction to Remote Sensing' },
    { file: 'chapter12.html', title: 'Making Maps' }
  ];

  // ---- Theme Toggle ----
  var toggle = document.getElementById('themeToggle');
  var html = document.documentElement;
  var saved = localStorage.getItem('theme');
  if (saved) html.setAttribute('data-theme', saved);
  if (toggle) {
    toggle.textContent = html.getAttribute('data-theme') === 'dark' ? '\u2600' : '\u263E';
    toggle.addEventListener('click', function () {
      var next = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      html.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
      toggle.textContent = next === 'dark' ? '\u2600' : '\u263E';
    });
  }

  // ---- Scroll Progress Bar ----
  var bar = document.getElementById('scrollProgress');
  if (bar) {
    window.addEventListener('scroll', function () {
      var h = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.width = h > 0 ? (window.scrollY / h * 100) + '%' : '0%';
    });
  }

  // ---- Reading Position Save & Restore ----
  // Saves scroll position per chapter so you resume where you left off
  if (currentFile && currentFile !== 'index.html') {
    var posKey = 'readPos_' + currentFile;
    var restored = false;
    // Restore on load
    var savedPos = sessionStorage.getItem(posKey);
    if (savedPos) {
      var pos = parseInt(savedPos, 10);
      if (pos > 100) {
        window.scrollTo(0, pos);
        restored = true;
      }
    }
    // Save on scroll (debounced)
    var saveTimer;
    window.addEventListener('scroll', function () {
      clearTimeout(saveTimer);
      saveTimer = setTimeout(function () {
        sessionStorage.setItem(posKey, String(window.scrollY));
      }, 300);
    });
  }

  // ---- Scroll to Top ----
  var topBtn = document.getElementById('scrollTop');
  if (topBtn) {
    window.addEventListener('scroll', function () {
      topBtn.classList.toggle('visible', window.scrollY > 300);
    });
    topBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // ---- Assign IDs to chapter h2 headings ----
  var headings = document.querySelectorAll('main h2');
  headings.forEach(function (h, i) {
    if (!h.id) h.id = 'section-' + i;
  });

  // ---- Chapter Navigation (Prev/Next) ----
  var currentFile = window.location.pathname.split('/').pop() || '';
  var idx = -1;
  for (var i = 0; i < chapters.length; i++) {
    if (chapters[i].file === currentFile) { idx = i; break; }
  }
  if (idx >= 0) {
    var footerNote = document.querySelector('.footer-note');
    if (footerNote) {
      var nav = document.createElement('div');
      nav.className = 'chapter-nav';

      if (idx > 0) {
        var prev = chapters[idx - 1];
        nav.innerHTML += '<a href="' + prev.file + '" class="nav-prev">' +
          '<span>\u2190</span><div><span class="nav-label">Previous</span>' +
          '<span class="nav-title">' + prev.title + '</span></div></a>';
      }
      if (idx < chapters.length - 1) {
        var next = chapters[idx + 1];
        nav.innerHTML += '<a href="' + next.file + '" class="nav-next">' +
          '<div><span class="nav-label">Next</span>' +
          '<span class="nav-title">' + next.title + '</span></div><span>\u2192</span></a>';
      }

      footerNote.parentNode.insertBefore(nav, footerNote);
    }
  }

  // ---- Reveal animations on scroll ----
  var reveals = document.querySelectorAll('.figure, .callout, .exam-box, .formula, .table-wrap');
  if ('IntersectionObserver' in window && reveals.length) {
    var revObs = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('visible');
          revObs.unobserve(e.target);
        }
      });
    }, { threshold: 0.1 });
    reveals.forEach(function (el) {
      el.classList.add('reveal');
      revObs.observe(el);
    });
  }

  // ---- Keyboard shortcuts ----
  document.addEventListener('keydown', function (e) {
    // Left arrow = previous chapter, Right arrow = next chapter
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
    if (idx >= 0) {
      if (e.key === 'ArrowLeft' && idx > 0) {
        window.location.href = chapters[idx - 1].file;
      } else if (e.key === 'ArrowRight' && idx < chapters.length - 1) {
        window.location.href = chapters[idx + 1].file;
      }
    }
    // 'T' to toggle theme
    if (e.key === 't' || e.key === 'T') {
      if (toggle) toggle.click();
    }
  });

  // ---- Track last-visited chapter & highlight on index ----
  if (idx >= 0) {
    // On a chapter page → save it
    localStorage.setItem('lastChapter', currentFile);
  }
  // On the index page → highlight the last-visited card
  if (currentFile === 'index.html' || currentFile === '' || currentFile === '/') {
    var lastCh = localStorage.getItem('lastChapter');
    if (lastCh) {
      var allCards = document.querySelectorAll('.chapter-card');
      allCards.forEach(function (card) {
        var link = card.querySelector('a');
        if (link && link.getAttribute('href') === lastCh) {
          card.classList.add('last-visited');
        }
      });
    }
  }

})();
