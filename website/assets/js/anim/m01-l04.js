// Animationen für Lektion 1.4 – Ableitungen & Gradienten
(function () {
  const { Plot, UI, stepper } = ML;

  // ---------- Von der Sekante zur Tangente ----------
  ANIMS["tangente"] = function (el) {
    UI.head(el, "Ableitung = Steigung im Punkt", "Ziehe den Punkt auf der Kurve. Verkleinere h: Die Sekante wird zur Tangente.");
    const f = x => 0.15 * x ** 3 - 0.9 * x + 1, df = x => 0.45 * x * x - 0.9;
    const p = new Plot(el, { height: 340, xmin: -4, xmax: 4, ymin: -3, ymax: 5 });
    const P = { x: 1.2, y: f(1.2) };
    let h = 1.5;
    const out = UI.readout(el);
    p.onDraw = (c, col) => {
      p.grid();
      p.fn(f, col.text2, 2);
      const x0 = P.x, y0 = f(x0), x1 = x0 + h, y1 = f(x1);
      const sec = (y1 - y0) / h, tan = df(x0);
      p.fn(x => y0 + sec * (x - x0), col.s2, 2);
      p.fn(x => y0 + tan * (x - x0), col.s1, 1.5);
      p.line(x0, y0, x1, y0, col.axis, 1, [4, 4]); p.line(x1, y0, x1, y1, col.axis, 1, [4, 4]);
      p.text("h", (x0 + x1) / 2, y0, col.text2, "center", 12, 0, 16);
      p.dot(x1, y1, col.s2, 6);
      p.dot(x0, y0, col.text, 8);
      out.innerHTML = `Sekantensteigung (f(x+h) − f(x)) / h = <b>${sec.toFixed(3)}</b> &nbsp;→&nbsp; Ableitung f'(${x0.toFixed(2)}) = <b>${tan.toFixed(3)}</b>`;
    };
    p.draggable(() => [P], (i, x) => { P.x = Math.max(-3.8, Math.min(3.8, x)); P.y = f(P.x); });
    const ctrl = UI.controls(el);
    UI.slider(ctrl, "h =", 0.01, 2.5, 0.01, h, v => { h = v; p.draw(); }, v => v.toFixed(2));
    UI.legend(el, [["--series-2", "Sekante durch x und x+h"], ["--series-1", "Tangente (Ableitung)"]]);
    p.draw();
  };

  // ---------- Gradient auf einer Höhenkarte ----------
  ANIMS["gradient-feld"] = function (el) {
    UI.head(el, "Der Gradient zeigt bergauf", "Höhenkarte von f(x, y). Ziehe den Punkt: Der Pfeil ist ∇f, er steht senkrecht auf den Höhenlinien.");
    const f = (x, y) => 0.5 * x * x + 1.2 * y * y + 0.4 * x * y + 0.6 * Math.sin(x);
    const grad = (x, y) => [x + 0.4 * y + 0.6 * Math.cos(x), 2.4 * y + 0.4 * x];
    const p = new Plot(el, { height: 380, pad: 20 });
    const P = { x: 1.8, y: 1.2 };
    let showField = false;
    const levels = Array.from({ length: 14 }, (_, i) => -0.5 + 0.5 * i * i * 0.18 + i * 0.3);
    const out = UI.readout(el);
    p.onDraw = (c, col) => {
      const aspect = (p.W - 40) / (p.H - 40); p.setRange(-3 * aspect, 3 * aspect, -3, 3);
      p.contour(f, levels, col.s1);
      if (showField) {
        for (let x = Math.ceil(p.opts.xmin); x <= p.opts.xmax; x += 0.75) for (let y = -2.5; y <= 2.5; y += 0.75) {
          const [gx, gy] = grad(x, y), L = Math.hypot(gx, gy) || 1, s = 0.3;
          p.arrow(x, y, x + gx / L * s, y + gy / L * s, col.axis, 1.2);
        }
      }
      const [gx, gy] = grad(P.x, P.y), sc = 0.35;
      p.arrow(P.x, P.y, P.x + gx * sc, P.y + gy * sc, col.s2, 3);
      p.arrow(P.x, P.y, P.x - gx * sc, P.y - gy * sc, col.s3, 3);
      p.dot(P.x, P.y, col.text, 8);
      out.innerHTML = `f(${P.x.toFixed(2)}, ${P.y.toFixed(2)}) = ${f(P.x, P.y).toFixed(2)} &nbsp;|&nbsp; ∇f = (∂f/∂x, ∂f/∂y) = (<b>${gx.toFixed(2)}</b>, <b>${gy.toFixed(2)}</b>) &nbsp;|&nbsp; ‖∇f‖ = ${Math.hypot(gx, gy).toFixed(2)}`;
    };
    p.draggable(() => [P], (i, x, y) => { P.x = x; P.y = y; });
    const ctrl = UI.controls(el);
    const b = UI.button(ctrl, "Gradientenfeld zeigen", () => { showField = !showField; b.textContent = showField ? "Gradientenfeld ausblenden" : "Gradientenfeld zeigen"; p.draw(); }, true);
    UI.legend(el, [["--series-2", "∇f (steilster Anstieg)"], ["--series-3", "−∇f (steilster Abstieg)"], ["--series-1", "kräftiger = höher"]]);
    p.draw();
  };

  // ---------- Kettenregel als Rechengraph ----------
  ANIMS["kettenregel"] = function (el) {
    UI.head(el, "Die Kettenregel im Rechengraphen", "f(x) = (3x + 1)², ausgewertet bei x = 2 – genau so rechnet später Backpropagation.");
    const p = new Plot(el, { height: 260, xmin: 0, xmax: 12, ymin: 0, ymax: 5, pad: 10 });
    function node(p, x, y, label, value, color) {
      const c = p.ctx; c.beginPath(); c.arc(p.sx(x), p.sy(y), 30, 0, 2 * Math.PI);
      c.fillStyle = p.color.bg; c.fill(); c.lineWidth = 2.5; c.strokeStyle = color; c.stroke();
      p.text(label, x, y, p.color.text, "center", 15, 0, -2);
      if (value !== undefined) p.text(value, x, y, color, "center", 12, 0, 16);
    }
    function base(p, col, vals, grads) {
      p.arrow(1.65, 3, 4.2, 3, col.axis); p.arrow(5.8, 3, 8.2, 3, col.axis); p.arrow(9.8, 3, 11.2, 3, col.axis);
      p.text("u = 3x + 1", 5, 3, col.text2, "center", 13, 0, -42);
      p.text("f = u²", 9, 3, col.text2, "center", 13, 0, -42);
      node(p, 1, 3, "x", vals ? "2" : undefined, col.s1);
      node(p, 5, 3, "u", vals ? "7" : undefined, col.s1);
      node(p, 9, 3, "f", vals ? "49" : undefined, col.s1);
      if (grads) {
        grads.forEach(([x, txt]) => p.text(txt, x, 1.4, col.s2, "center", 14));
      }
    }
    stepper(el, p, [
      { text: "Eine verschachtelte Funktion zerlegen wir in einfache Schritte: erst \\(u = 3x + 1\\), dann \\(f = u^2\\).", draw: (p, c, col) => base(p, col) },
      { text: "<b>Vorwärtsrechnung</b> (<span class='term'>Forward Pass</span>): Wir setzen \\(x = 2\\) ein und rechnen von links nach rechts: \\(u = 7\\), \\(f = 49\\).", draw: (p, c, col) => base(p, col, true) },
      { text: "<b>Rückwärts</b> (<span class='term'>Backward Pass</span>): Wir starten am Ende mit \\(\\partial f / \\partial f = 1\\). Lokale Ableitung von \\(f = u^2\\): \\(\\partial f / \\partial u = 2u = 14\\).",
        draw: (p, c, col) => { base(p, col, true, [[9, "∂f/∂f = 1"], [7, "∂f/∂u = 2u = 14"]]); p.arrow(8.2, 2.1, 5.8, 2.1, col.s2); } },
      { text: "Lokale Ableitung von \\(u = 3x + 1\\): \\(\\partial u / \\partial x = 3\\). <b>Kettenregel:</b> multipliziere entlang des Weges: \\(\\frac{df}{dx} = \\frac{\\partial f}{\\partial u} \\cdot \\frac{\\partial u}{\\partial x} = 14 \\cdot 3 = 42\\).",
        draw: (p, c, col) => { base(p, col, true, [[9, "1"], [7, "14"], [3, "14 · 3 = 42"]]); p.arrow(8.2, 2.1, 5.8, 2.1, col.s2); p.arrow(4.2, 2.1, 1.8, 2.1, col.s2); } },
      { text: "Kontrolle: \\(f(x) = (3x+1)^2 \\Rightarrow f'(x) = 2(3x+1) \\cdot 3 = 6(3x+1)\\), bei \\(x = 2\\): \\(6 \\cdot 7 = 42\\) ✓. Neuronale Netze sind riesige solche Graphen – Backpropagation ist genau diese Rückwärtsrechnung.",
        draw: (p, c, col) => { base(p, col, true, [[9, "1"], [7, "14"], [3, "42 ✓"]]); } }
    ]);
  };
})();
