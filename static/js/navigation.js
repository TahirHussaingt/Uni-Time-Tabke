(() => {
  const toggle = document.querySelector("[data-menu-toggle]");
  const closeTarget = document.querySelector("[data-sidebar-close]");
  const closeMenu = () => {
    document.body.classList.remove("nav-open");
    toggle?.setAttribute("aria-expanded", "false");
    if (closeTarget) closeTarget.hidden = true;
  };
  const openMenu = () => {
    document.body.classList.add("nav-open");
    toggle?.setAttribute("aria-expanded", "true");
    if (closeTarget) closeTarget.hidden = false;
  };
  toggle?.addEventListener("click", () => document.body.classList.contains("nav-open") ? closeMenu() : openMenu());
  closeTarget?.addEventListener("click", closeMenu);
  document.addEventListener("keydown", (event) => { if (event.key === "Escape") closeMenu(); });
})();
