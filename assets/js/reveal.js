(function () {
  if (!("IntersectionObserver" in window)) return;
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

  var selectors = [
    ".post-header",
    ".post article > .profile",
    ".post article > .clearfix > *",
    ".post article > h2",
    ".post article > .news",
    ".post article > .visitor-map",
    ".post article > .social",
    ".publications h1",
    ".publications h2.year",
    ".projects h2.project-section",
    ".life h2.project-section",
    ".life-gallery figure",
    ".publications ol.bibliography > li",
    ".project-card",
    ".project-page > *",
    ".cv .card",
  ];
  var elements = document.querySelectorAll(selectors.join(","));
  if (!elements.length) {
    document.documentElement.classList.remove("reveal-pending");
    return;
  }

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

  // Above-the-fold content gets a quick, unstaggered fade so navigation feels instant.
  elements.forEach(function (el) {
    el.classList.add("reveal");
    if (el.getBoundingClientRect().top < window.innerHeight) {
      el.classList.add("reveal-initial", "is-visible");
    } else {
      observer.observe(el);
    }
  });
  document.documentElement.classList.remove("reveal-pending");
})();
