// Summary pages – enhanced interactions
(function () {
  // Q&A toggle with smooth animation
  document.querySelectorAll('.qa-question').forEach(function (q) {
    var block = q.closest('.qa-block');
    var answer = q.nextElementSibling;
    if (!answer || !answer.classList.contains('qa-answer')) return;

    q.addEventListener('click', function () {
      var isOpen = block.classList.contains('open');
      block.classList.toggle('open', !isOpen);
      answer.classList.toggle('open', !isOpen);
      var icon = q.querySelector('.qa-toggle');
      if (icon) icon.textContent = isOpen ? '+' : '\u2212';
    });
  });

  // Expand-all / Collapse-all button
  var expandBtn = document.querySelector('.expand-all-btn');
  if (expandBtn) {
    expandBtn.addEventListener('click', function () {
      var blocks = document.querySelectorAll('.qa-block');
      var anyCollapsed = false;
      blocks.forEach(function (b) { if (!b.classList.contains('open')) anyCollapsed = true; });
      blocks.forEach(function (b) {
        var ans = b.querySelector('.qa-answer');
        var icon = b.querySelector('.qa-toggle');
        if (anyCollapsed) {
          b.classList.add('open');
          if (ans) ans.classList.add('open');
          if (icon) icon.textContent = '\u2212';
        } else {
          b.classList.remove('open');
          if (ans) ans.classList.remove('open');
          if (icon) icon.textContent = '+';
        }
      });
      expandBtn.textContent = anyCollapsed ? 'Collapse All' : 'Expand All';
    });
  }

  // Index page: filter buttons
  document.querySelectorAll('.filter-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var filter = btn.dataset.filter;
      document.querySelectorAll('.filter-btn').forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      document.querySelectorAll('.chapter-card').forEach(function (card) {
        if (filter === 'all' || card.dataset.priority === filter) {
          card.style.display = '';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });

  // Animate stat cards on scroll
  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) {
        e.target.style.opacity = '1';
        e.target.style.transform = 'translateY(0)';
      }
    });
  }, { threshold: 0.2 });
  document.querySelectorAll('.stat-card, .chapter-card').forEach(function (el) {
    el.style.opacity = '0';
    el.style.transform = 'translateY(16px)';
    el.style.transition = 'opacity .5s, transform .5s';
    observer.observe(el);
  });
})();
