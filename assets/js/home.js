const cardTargets = document.querySelectorAll(".game-card[data-href]");

function markReady() {
  if (window.ChronohazeLoader) {
    window.ChronohazeLoader.ready();
    return;
  }
  requestAnimationFrame(() => {
    document.body.classList.remove("is-loading");
    document.body.classList.add("is-ready");
  });
}

function navigate(href, source) {
  if (window.ChronohazeLoader && window.ChronohazeLoader.go(href, source)) return;
  window.location.href = href;
}

for (const card of cardTargets) {
  const href = card.dataset.href;
  if (!href) continue;

  card.addEventListener("click", (event) => {
    if (event.target.closest("button, a")) return;
    navigate(href, card);
  });

  card.addEventListener("keydown", (event) => {
    if (event.key !== "Enter" && event.key !== " ") return;
    event.preventDefault();
    navigate(href, card);
  });
}

window.addEventListener("load", markReady, { once: true });
