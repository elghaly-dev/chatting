(function () {
  var STORAGE_KEY = "chatting-lang";
  var buttons = document.querySelectorAll(".lang-btn[data-lang]");
  var panels = document.querySelectorAll("[data-lang-panel]");

  function setLang(code) {
    var html = document.documentElement;
    html.lang = code === "zh" ? "zh-Hans" : code;
    html.dir = code === "ar" ? "rtl" : "ltr";
    panels.forEach(function (panel) {
      panel.hidden = panel.getAttribute("data-lang-panel") !== code;
    });
    buttons.forEach(function (btn) {
      btn.setAttribute("aria-pressed", btn.getAttribute("data-lang") === code ? "true" : "false");
    });
    try {
      localStorage.setItem(STORAGE_KEY, code);
    } catch (e) {
      /* ignore */
    }
  }

  buttons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      setLang(btn.getAttribute("data-lang"));
    });
  });

  var initial = "en";
  try {
    var saved = localStorage.getItem(STORAGE_KEY);
    if (saved && document.querySelector('[data-lang-panel="' + saved + '"]')) {
      initial = saved;
    }
  } catch (e2) {
    /* ignore */
  }
  setLang(initial);
})();
