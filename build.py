"""Genera las 4 páginas del prototipo.

Las tres páginas de grupo salen de la MISMA plantilla: lo único que cambia
es el puntaje de seguridad (1, 2,5 o 5). Así el prototipo garantiza que la
variable independiente es la única diferencia entre condiciones.

Uso: python3 build.py
"""
from pathlib import Path

OUT = Path(__file__).parent

GRUPOS = {
    "a": {"label": "A", "nombre": "Reseñas negativas", "score": 1.0, "color": "var(--grp-a)",
          "desc": "Ve una calificación de seguridad de 1 sobre 5."},
    "b": {"label": "B", "nombre": "Reseñas positivas", "score": 5.0, "color": "var(--grp-b)",
          "desc": "Ve una calificación de seguridad de 5 sobre 5."},
    "c": {"label": "C", "nombre": "Control (neutral)", "score": 2.5, "color": "var(--grp-c)",
          "desc": "Ve una calificación de seguridad de 2,5 sobre 5."},
}

STAR_PATH = "M12 2.6l2.85 6.06 6.65.78-4.92 4.55 1.31 6.57L12 17.27l-5.89 3.29 1.31-6.57L2.5 9.44l6.65-.78z"


def stars(score):
    out = []
    for i in range(5):
        fill = max(0.0, min(1.0, score - i))
        pct = int(round(fill * 100))
        out.append(
            f'<span class="star"><svg class="off" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="{STAR_PATH}"/></svg>'
            f'<svg class="on" viewBox="0 0 24 24" aria-hidden="true" style="clip-path: inset(0 {100 - pct}% 0 0)"><path fill="currentColor" d="{STAR_PATH}"/></svg></span>'
        )
    return f'<div class="stars" role="img" aria-label="{fmt(score)} de 5 estrellas">' + "".join(out) + "</div>"


def fmt(score):
    return ("%g" % score).replace(".", ",")


def head(title, desc):
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700;800&family=Fraunces:ital,opsz,wght@0,9..144,600;1,9..144,600&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%231f4fd8'/%3E%3Ctext x='16' y='22' font-size='16' text-anchor='middle' fill='white' font-family='Arial' font-weight='700'%3ETC%3C/text%3E%3C/svg%3E">
</head>
"""


def rbar(current):
    tabs = [("index", "index.html", "Portada", "")]
    for k, g in GRUPOS.items():
        tabs.append((k, f"grupo-{k}.html", f"Grupo {g['label']}", f'<span class="dot dot--{k}"></span>'))
    cur = ' aria-current="page"'
    links = "".join(
        f'<a class="rbar__tab" href="{href}"{cur if key == current else ""}>{dot}{text}</a>'
        for key, href, text, dot in tabs
    )
    toggle = '<button class="rbar__toggle" type="button" data-toggle-view aria-pressed="false">Ver como participante</button>' if current != "index" else ""
    return f"""<nav class="rbar" aria-label="Navegación del prototipo">
  <div class="rbar__in">
    <span class="rbar__tag">Prototipo · TIF C094</span>
    <div class="rbar__tabs">{links}</div>
    {toggle}
  </div>
</nav>
"""


SHIELD = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>'

HEADPHONES = """<svg viewBox="0 0 200 200" aria-hidden="true">
  <path d="M40 112 C40 58 72 30 100 30 C128 30 160 58 160 112" fill="none" stroke="#1d2433" stroke-width="12" stroke-linecap="round"/>
  <path d="M46 108 C46 64 74 40 100 40 C126 40 154 64 154 108" fill="none" stroke="#3a4560" stroke-width="3" stroke-linecap="round" opacity=".6"/>
  <rect x="24" y="100" width="40" height="64" rx="18" fill="#1d2433"/>
  <rect x="136" y="100" width="40" height="64" rx="18" fill="#1d2433"/>
  <rect x="34" y="110" width="20" height="44" rx="10" fill="#2f3a55"/>
  <rect x="146" y="110" width="20" height="44" rx="10" fill="#2f3a55"/>
  <circle cx="160" cy="118" r="3" fill="#1f4fd8"/>
</svg>"""


def grupo_page(key):
    g = GRUPOS[key]
    s = g["score"]
    return head(
        f"Grupo {g['label']} · Tienda Campus",
        f"Prototipo del experimento: condición del grupo {g['label']} ({g['nombre'].lower()}).",
    ) + f"""<body data-grupo-label="{g['label']}">
{rbar(key)}
<div class="rnote" role="note"><div class="rnote__in">
  <strong>Grupo {g['label']} · {g['nombre']}.</strong> {g['desc']} Todo lo demás (producto, precio, diseño, método de pago, ubicación y tamaño de la calificación) es idéntico en los tres grupos.
</div></div>

<header class="shop-head">
  <div class="shop-head__in">
    <a class="logo" href="#" aria-label="Tienda Campus"><span class="logo__mark">TC</span>Tienda Campus</a>
    <div class="steps" aria-label="Pasos de la compra"><span>Carrito</span><i></i><span>Envío</span><i></i><b>Pago</b></div>
  </div>
</header>

<main class="shop">
  <h1>Finalizá tu compra</h1>
  <div class="grid">
    <div>
      <section class="card" aria-labelledby="prod-t">
        <div class="product">
          <div class="product__img">{HEADPHONES}</div>
          <div class="product__meta">
            <div class="product__sku">Artículo 1 de 1</div>
            <h2 id="prod-t">Auriculares inalámbricos Sonaro Air 2</h2>
            <ul class="product__list">
              <li>Bluetooth 5.3, hasta 30 h de batería</li>
              <li>Cancelación de ruido para estudiar en la biblioteca</li>
              <li>Color negro, incluye cable USB-C</li>
            </ul>
            <div class="qty">Cantidad <span>1</span></div>
          </div>
        </div>
        <p class="illus-note">Producto de ejemplo: ilustra el "producto X" que los participantes eligieron en la encuesta previa. La marca es ficticia.</p>
        <div style="height:18px"></div>
      </section>

      <section class="card ship" aria-label="Entrega">
        <div class="ship__ico"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></div>
        <div>
          <h3>Retiro sin cargo en el campus</h3>
          <p>Lo retirás en 3 días hábiles. Envío a domicilio no disponible en esta prueba.</p>
        </div>
      </section>
    </div>

    <aside class="card summary" aria-labelledby="sum-t">
      <h2 id="sum-t">Resumen</h2>
      <div class="row"><span>Sonaro Air 2 × 1</span><span>$45.000</span></div>
      <div class="row"><span>Retiro en el campus</span><span>Gratis</span></div>
      <div class="row row--total"><span>Total</span><span>$45.000</span></div>

      <div class="pay">
        <div class="pay__label">Método de pago</div>
        <div class="pay__method">
          <span class="nexo" aria-hidden="true">N</span>
          <div><b>Billetera Nexo</b><span>Pago digital integrado</span></div>
          <span class="pay__check" aria-hidden="true"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5L20 7"/></svg></span>
        </div>

        <section class="sec" aria-labelledby="sec-t">
          <h3 class="sec__title" id="sec-t">{SHIELD}Calificación de seguridad del método de pago digital</h3>
          <div class="sec__score">
            <div class="sec__num">{fmt(s)}<small> / 5</small></div>
            {stars(s)}
          </div>
        </section>
      </div>

      <div class="actions">
        <button class="btn btn--buy" type="button" data-buy>Confirmar compra</button>
        <button class="btn btn--leave" type="button" data-leave>Abandonar compra</button>
        <p class="safe-note">Compra simulada: no se cobra nada ni se piden datos bancarios.</p>
      </div>
    </aside>
  </div>
</main>

<div class="modal" id="resultado" role="dialog" aria-modal="true" aria-labelledby="res-t">
  <div class="modal__box">
    <h2 id="res-t" data-titulo></h2>
    <p data-texto></p>
    <div class="reg" data-reg aria-label="Dato que registraría la plataforma"></div>
    <p>Al terminar, a cada participante se le explica que la calificación fue armada para el experimento.</p>
    <button class="btn btn--buy" type="button" data-close>Cerrar</button>
  </div>
</div>

<footer class="foot">Tienda Campus y Billetera Nexo son ficticias. Prototipo de un trabajo práctico de la Universidad de San Andrés (C094, primavera 2026).</footer>
<script src="script.js"></script>
</body>
</html>
"""


def index_page():
    cards = ""
    for k, g in GRUPOS.items():
        cards += f"""<a class="gcard" href="grupo-{k}.html" style="--c:{g['color']}">
      <span class="gcard__tag">Grupo {g['label']}</span>
      <h3>{g['nombre']}</h3>
      {stars(g['score'])}
      <p>{g['desc']}</p>
      <span class="gcard__go">Ver la página de este grupo →</span>
    </a>
    """
    return head(
        "Seguridad percibida y compra online",
        "Prototipo de la plataforma de compra para el experimento sobre seguridad percibida de medios de pago digitales.",
    ) + f"""<body>
{rbar("index")}
<header class="hero">
  <div class="kicker">TIF · Introducción a las Ciencias · UdeSA · Primavera 2026</div>
  <h1>¿Una calificación de seguridad <em>cambia</em> la decisión de comprar?</h1>
  <p class="lead">Este es el prototipo de la tienda ficticia donde haríamos el experimento. Los tres grupos ven la misma página, con el mismo producto, el mismo precio y el mismo método de pago. Lo único que cambia es el puntaje de seguridad que aparece junto al botón de confirmar.</p>
  <p class="team">Aguilar Quesada, Camila · Andersson, Franco · Delfino Chevallier, Constanza · Son, Micaela</p>
</header>

<main class="wrap">
  <section class="sect" aria-labelledby="g-t">
    <h2 id="g-t">Las tres condiciones</h2>
    <p>Cada participante entra a una sola de estas páginas, asignado al azar. Ninguno ve las de los otros grupos.</p>
    <div class="groups">
    {cards}</div>
  </section>

  <section class="sect" aria-labelledby="v-t">
    <h2 id="v-t">Qué medimos</h2>
    <p>Pregunta de investigación: ¿cómo influye la información sobre la seguridad del método de pago digital en el porcentaje de estudiantes de 18 a 25 años de UdeSA que finalizan una compra?</p>
    <div class="vars">
      <div class="vbox">
        <h3>Variable independiente</h3>
        <strong>Calificación de seguridad del pago</strong>
        <p>1, 2,5 o 5 estrellas sobre 5, según el grupo. Está siempre en el mismo lugar, con el mismo tamaño, y aclara que califica el pago y no el producto ni la tienda.</p>
      </div>
      <div class="vbox">
        <h3>Variable dependiente</h3>
        <strong>Decisión de finalizar la compra</strong>
        <p>Dicotómica: 1 si el participante toca "Confirmar compra", 0 si toca "Abandonar compra". Después se calcula el porcentaje de compras finalizadas por grupo.</p>
      </div>
    </div>
  </section>

  <section class="sect" aria-labelledby="f-t">
    <h2 id="f-t">Cómo lo recorre un participante</h2>
    <p>Una sola sesión (diseño transversal), en laboratorio, con las mismas instrucciones para todos.</p>
    <ol class="flow">
      <li><b>Encuesta previa</b>Solo entran quienes dijeron que querían comprar el producto X.</li>
      <li><b>Asignación al azar</b>Unas 150 personas, repartidas en tres grupos de 50.</li>
      <li><b>La tienda</b>Ve la página de su grupo, con el producto ya en el carrito.</li>
      <li><b>La decisión</b>Confirma o abandona. La plataforma registra grupo y decisión.</li>
      <li><b>Cierre</b>Se le explica que la calificación fue diseñada para el experimento.</li>
    </ol>
  </section>

  <section class="sect" aria-labelledby="c-t">
    <h2 id="c-t">Qué queda fijo y qué cambia</h2>
    <p>Controlar la página entera nos deja atribuir una diferencia entre grupos a la calificación y no a otra cosa (validez interna).</p>
    <div class="tablewrap">
    <table class="ctable">
      <thead><tr><th>Elemento</th><th>Grupo A</th><th>Grupo B</th><th>Grupo C</th></tr></thead>
      <tbody>
        <tr><td>Producto</td><td colspan="3">Auriculares Sonaro Air 2 (ejemplo del producto X)</td></tr>
        <tr><td>Precio</td><td colspan="3">$45.000</td></tr>
        <tr><td>Método de pago</td><td colspan="3">Billetera Nexo (ficticia, para que nadie llegue con una opinión previa)</td></tr>
        <tr><td>Diseño, ubicación y tamaño de la calificación</td><td colspan="3">Idénticos</td></tr>
        <tr class="var"><td>Calificación de seguridad</td><td>1 / 5</td><td>5 / 5</td><td>2,5 / 5</td></tr>
      </tbody>
    </table>
    </div>
  </section>

  <section class="sect" aria-labelledby="p-t">
    <h2 id="p-t">Lo que esperamos ver</h2>
    <p>Si la hipótesis es correcta, el porcentaje de compras finalizadas debería ordenarse B &gt; C &gt; A. Si los porcentajes son parecidos o el orden se invierte, la hipótesis se debilita.</p>
    <div class="pred" role="img" aria-label="Predicción ilustrativa: grupo B el más alto, C intermedio, A el más bajo">
      <div class="pred__col"><div class="pred__bar" style="height:28%;--c:var(--grp-a)"></div><span class="pred__lab">A · 1★</span></div>
      <div class="pred__col"><div class="pred__bar" style="height:92%;--c:var(--grp-b)"></div><span class="pred__lab">B · 5★</span></div>
      <div class="pred__col"><div class="pred__bar" style="height:58%;--c:var(--grp-c)"></div><span class="pred__lab">C · 2,5★</span></div>
    </div>
    <p class="pred-note">Las alturas son ilustrativas: muestran el orden esperado, no resultados.</p>
  </section>

  <footer class="closing">Prototipo sin base de datos: las decisiones que se tomen acá no se guardan. Tienda Campus, Sonaro y Billetera Nexo son marcas inventadas para el estudio.</footer>
</main>
</body>
</html>
"""


if __name__ == "__main__":
    (OUT / "index.html").write_text(index_page(), encoding="utf-8")
    for k in GRUPOS:
        (OUT / f"grupo-{k}.html").write_text(grupo_page(k), encoding="utf-8")
    print("ok")
