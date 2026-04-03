/* ============================================================
   TES Study Guide – Shared Interactivity
   ============================================================ */

(function () {
  'use strict';

  // ---- Chapter data for navigation ----
  var chapters = [
    { file: 'chapter1_updated.html', title: 'Technology' },
    { file: 'chapter2.html',         title: 'Development Approach' },
    { file: 'chapter3.html',         title: 'Brief History of Human Civilization' },
    { file: 'chapter4.html',         title: 'Environment' },
    { file: 'chapter5.html',         title: 'Water and Air Pollution' },
    { file: 'chapter6.html',         title: 'Climate Change' }
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

  // ---- Mnemonics / Personal Notes (persisted via localStorage) ----
  // Adds an editable notebook area to each chapter page
  if (currentFile && currentFile !== 'index.html' && currentFile !== 'index_tes.html' && currentFile !== '') {
    var mnKey = 'mnemonics_' + currentFile;

    // Find each h2 section and add a mini-note area
    var allH2 = document.querySelectorAll('main h2');
    allH2.forEach(function (h2, si) {
      var noteKey = mnKey + '_s' + si;
      var saved = localStorage.getItem(noteKey) || '';

      var wrapper = document.createElement('div');
      wrapper.className = 'mnemonic-block';

      var toggleBtn = document.createElement('button');
      toggleBtn.className = 'mnemonic-toggle';
      toggleBtn.innerHTML = '&#x1F4DD; My Notes';
      toggleBtn.setAttribute('aria-label', 'Toggle notes for this section');

      var editor = document.createElement('div');
      editor.className = 'mnemonic-editor';
      editor.style.display = 'none';

      var label = document.createElement('div');
      label.className = 'mnemonic-label';
      label.textContent = 'Your mnemonics & notes (auto-saved)';

      var textarea = document.createElement('textarea');
      textarea.className = 'mnemonic-textarea';
      textarea.placeholder = 'Type your mnemonics, tricks, or notes here... They will persist across page reloads.';
      textarea.value = saved;
      textarea.rows = 4;

      // Auto-save on input
      var saveTimer;
      textarea.addEventListener('input', function () {
        clearTimeout(saveTimer);
        saveTimer = setTimeout(function () {
          localStorage.setItem(noteKey, textarea.value);
          indicator.textContent = 'Saved!';
          indicator.style.opacity = '1';
          setTimeout(function () { indicator.style.opacity = '0'; }, 1500);
        }, 400);
      });

      var indicator = document.createElement('span');
      indicator.className = 'mnemonic-saved';
      indicator.textContent = 'Saved!';
      indicator.style.opacity = '0';

      // If there's saved content, show it by default
      if (saved) {
        editor.style.display = 'block';
        toggleBtn.classList.add('active');
      }

      toggleBtn.addEventListener('click', function () {
        var open = editor.style.display === 'block';
        editor.style.display = open ? 'none' : 'block';
        toggleBtn.classList.toggle('active', !open);
      });

      editor.appendChild(label);
      editor.appendChild(textarea);
      editor.appendChild(indicator);
      wrapper.appendChild(toggleBtn);
      wrapper.appendChild(editor);

      // Insert at the end of this section (before next h2 or at end of main)
      var nextH2 = allH2[si + 1];
      if (nextH2) {
        nextH2.parentNode.insertBefore(wrapper, nextH2);
      } else {
        var mainEl = document.querySelector('main');
        if (mainEl) mainEl.appendChild(wrapper);
      }
    });

    // Also add a chapter-wide notes area at the top
    var mainEl = document.querySelector('main');
    if (mainEl) {
      var chapterNoteKey = mnKey + '_chapter';
      var chapterSaved = localStorage.getItem(chapterNoteKey) || '';
      var chBlock = document.createElement('div');
      chBlock.className = 'mnemonic-block mnemonic-chapter';

      var chToggle = document.createElement('button');
      chToggle.className = 'mnemonic-toggle chapter-level';
      chToggle.innerHTML = '&#x1F4D3; Chapter Notes & Mnemonics';

      var chEditor = document.createElement('div');
      chEditor.className = 'mnemonic-editor';
      chEditor.style.display = chapterSaved ? 'block' : 'none';
      if (chapterSaved) chToggle.classList.add('active');

      var chLabel = document.createElement('div');
      chLabel.className = 'mnemonic-label';
      chLabel.textContent = 'Your chapter-wide notes, mnemonics & memory aids';

      var chTextarea = document.createElement('textarea');
      chTextarea.className = 'mnemonic-textarea chapter-textarea';
      chTextarea.placeholder = 'Write chapter-wide mnemonics, key formulas, acronyms, tricks to remember...';
      chTextarea.value = chapterSaved;
      chTextarea.rows = 6;

      var chIndicator = document.createElement('span');
      chIndicator.className = 'mnemonic-saved';
      chIndicator.textContent = 'Saved!';
      chIndicator.style.opacity = '0';

      var chSaveTimer;
      chTextarea.addEventListener('input', function () {
        clearTimeout(chSaveTimer);
        chSaveTimer = setTimeout(function () {
          localStorage.setItem(chapterNoteKey, chTextarea.value);
          chIndicator.textContent = 'Saved!';
          chIndicator.style.opacity = '1';
          setTimeout(function () { chIndicator.style.opacity = '0'; }, 1500);
        }, 400);
      });

      chToggle.addEventListener('click', function () {
        var open = chEditor.style.display === 'block';
        chEditor.style.display = open ? 'none' : 'block';
        chToggle.classList.toggle('active', !open);
      });

      chEditor.appendChild(chLabel);
      chEditor.appendChild(chTextarea);
      chEditor.appendChild(chIndicator);
      chBlock.appendChild(chToggle);
      chBlock.appendChild(chEditor);

      mainEl.insertBefore(chBlock, mainEl.firstChild);
    }
  }

})();
