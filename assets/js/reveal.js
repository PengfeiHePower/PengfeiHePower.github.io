(function () {
  if (!("IntersectionObserver" in window)) return;
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

  var selectors = [
    ".post-header",
    ".post article > .profile",
    ".post article > .clearfix > *",
    ".post article > h2",
    ".post article > .news",
    ".post article > .social",
    ".publications h1",
    ".publications h2.year",
    ".projects h2.project-section",
    ".publications ol.bibliography > li",
    ".project-card",
    ".project-page > *",
    ".cv .card",
  ];
  var elements = document.querySelectorAll(selectors.join(","));
  if (!elements.length) return;

  function show(el, index) {
    el.style.animationDelay = Math.min(index * 60, 360) + "ms";
    el.classList.add("is-visible");
  }

  var observer = new IntersectionObserver(
    function (entries) {
      var batch = 0;
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        show(entry.target, batch++);
        observer.unobserve(entry.target);
      });
    },
    { rootMargin: "0px 0px -40px 0px" }
  );

  // Above-the-fold content is revealed right away so it never waits on the observer.
  var initial = 0;
  elements.forEach(function (el) {
    el.classList.add("reveal");
    if (el.getBoundingClientRect().top < window.innerHeight) {
      show(el, initial++);
    } else {
      observer.observe(el);
    }
  });
})();
