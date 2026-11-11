(function () {
  // Vista participante: oculta la barra del investigador (se recuerda solo en este navegador)
  var KEY = "tif-vista-participante";
  var body = document.body;
  var toggle = document.querySelector("[data-toggle-view]");
  function apply(on) {
    body.classList.toggle("participante", on);
    if (toggle) {
      toggle.textContent = on ? "Volver a vista investigador" : "Ver como participante";
      toggle.setAttribute("aria-pressed", on ? "true" : "false");
    }
  }
  var saved = false;
  try { saved = localStorage.getItem(KEY) === "1"; } catch (e) {}
  if (toggle) {
    apply(saved);
    toggle.addEventListener("click", function () {
      var on = !body.classList.contains("participante");
      apply(on);
      try { localStorage.setItem(KEY, on ? "1" : "0"); } catch (e) {}
    });
  }

  // Decisión de compra: no se guarda nada, solo se muestra qué se registraría
  var modal = document.getElementById("resultado");
  if (!modal) return;
  var grupo = body.getAttribute("data-grupo-label");
  var titulo = modal.querySelector("[data-titulo]");
  var texto = modal.querySelector("[data-texto]");
  var reg = modal.querySelector("[data-reg]");
  var last = null;

  function open(compra) {
    last = document.activeElement;
    titulo.textContent = compra ? "Compra confirmada (simulada)" : "Compra abandonada";
    texto.textContent = compra
      ? "No se cobró nada ni se pidieron datos bancarios. En el experimento real, acá termina la tarea del participante."
      : "El participante decidió no finalizar la compra. En el experimento real, acá termina su tarea.";
    reg.innerHTML =
      "<span>grupo:</span> " + grupo + "<br>" +
      "<span>decision_compra:</span> " + (compra ? "1" : "0") + "<br>" +
      "<span>guardado:</span> no (prototipo)";
    modal.classList.add("open");
    modal.querySelector("[data-close]").focus();
  }
  function close() {
    modal.classList.remove("open");
    if (last) last.focus();
  }
  document.querySelector("[data-buy]").addEventListener("click", function () { open(true); });
  document.querySelector("[data-leave]").addEventListener("click", function () { open(false); });
  modal.querySelector("[data-close]").addEventListener("click", close);
  modal.addEventListener("click", function (e) { if (e.target === modal) close(); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && modal.classList.contains("open")) close(); });
})();
