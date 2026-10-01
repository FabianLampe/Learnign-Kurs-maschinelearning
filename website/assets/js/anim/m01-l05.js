// Animationen für Lektion 1.5 – Verlustfunktionen & Gradientenabstieg
(function () {
  const { Plot, UI } = ML;

  // Kleiner Datensatz für die Regressionsbeispiele (fest, damit alle dasselbe sehen)
  const DATA = [[0.5, 1.6], [1.0, 2.1], [1.6, 2.4], [2.1, 3.3], [2.7, 3.2], [3.2, 4.1], [3.8, 4.3], [4.3, 5.2], [4.9, 5.1], [5.4, 6.0]];

  // ---------- Fehlerquadrate sichtbar machen ----------
  ANIMS["fehlerquadrate"] = function (el) {
    UI.head(el, "Mittlerer quadratischer Fehler – wörtlich genommen", "Ziehe die beiden Griffe der Geraden. Jedes Quadrat ist ein Fehler². MSE = durchschnittliche Fläche.");
    const p = new Plot(el, { height: 380, xmin: 0, xmax: 6, ymin: 0, ymax: 7, pad: 30 });
    const A = { x: 0.5, y: 3.5 }, B = { x: 5.5, y: 3.5 };
    let squares = true;
    const out = UI.readout(el);
    p.onDraw = (c, col) => {
      p.grid();
      const w = (B.y - A.y) / (B.x - A.x), b = A.y - w * A.x;
      let mse = 0, mae = 0;
      DATA.forEach(([x, y]) => {
        const yh = w * x + b, r = y - yh; mse += r * r; mae += Math.abs(r);
        if (squares) {
          // Quadrat mit Seitenlänge |r| (in Pixeln der y-Achse, damit es wirklich quadratisch aussieht)
          const side = Math.abs(p.sy(yh) - p.sy(y));
          c.fillStyle = col.s2; c.globalAlpha = 0.18;
          c.fillRect(p.sx(x), Math.min(p.sy(y), p.sy(yh)), side, side); c.globalAlpha = 1;
        }
        p.line(x, y, x, yh, col.s2, 2);
      });
      mse /= DATA.length; mae /= DATA.length;
      p.line(0, b, 6, w * 6 + b, col.s1, 2.5);
      DATA.forEach(([x, y]) => p.dot(x, y, col.text, 6));
      p.dot(A.x, A.y, col.s1, 9); p.dot(B.x, B.y, col.s1, 9);
      out.innerHTML = `ŷ = ${w.toFixed(2)}·x + ${b.toFixed(2)} &nbsp;|&nbsp; MSE = <b>${mse.toFixed(3)}</b> &nbsp;|&nbsp; MAE = ${mae.toFixed(3)} &nbsp;(Optimum: w ≈ 0.87, b ≈ 1.18, MSE ≈ 0.049)`;
    };
    p.draggable(() => [A, B], (i, x, y) => { const v = i ? B : A; v.y = Math.max(-2, Math.min(9, y)); });
    const ctrl = UI.controls(el);
    const bt = UI.button(ctrl, "Quadrate ausblenden", () => { squares = !squares; bt.textContent = squares ? "Quadrate ausblenden" : "Quadrate zeigen"; p.draw(); }, true);
    UI.legend(el, [["--series-1", "Modell ŷ = w·x + b"], ["--series-2", "Residuen y − ŷ und ihre Quadrate"]]);
    p.draw();
  };

  // ---------- Gradientenabstieg in 1D ----------
  ANIMS["gd-1d"] = function (el) {
    UI.head(el, "Gradientenabstieg Schritt für Schritt", "Klick auf die Kurve setzt den Startpunkt. Probiere kleine, mittlere und zu große Lernraten.");
    const fns = {
      "Parabel": { f: x => 0.5 * x * x, df: x => x, range: [-5, 5, -0.5, 12.5], x0: -4.2 },
      "Zwei Täler": { f: x => 0.05 * x ** 4 - 0.6 * x * x + 0.3 * x + 2, df: x => 0.2 * x ** 3 - 1.2 * x + 0.3, range: [-4.2, 4.2, -1, 6], x0: 3.6 }
    };
    let cur = fns["Parabel"], lr = 0.3, path = [], timer = null;
    const p = new Plot(el, { height: 340, xmin: -5, xmax: 5, ymin: -0.5, ymax: 12.5 });
    const out = UI.readout(el);
    function reset(x0) { path = [x0 ?? cur.x0]; p.draw(); }
    function step() {
      const x = path[path.length - 1], g = cur.df(x), nx = x - lr * g;
      if (!isFinite(nx) || Math.abs(nx) > 1e3) return false;
      path.push(nx); p.draw(); return Math.abs(nx - x) > 1e-4;
    }
    p.onDraw = (c, col) => {
      p.setRange(...cur.range); p.grid();
      p.fn(cur.f, col.text2, 2);
      for (let i = 1; i < path.length; i++) {
        const a = path[i - 1], b = path[i];
        p.arrow(a, cur.f(a), b, cur.f(b), col.s2, 1.8);
      }
      path.forEach((x, i) => p.dot(x, cur.f(x), i === path.length - 1 ? col.s1 : col.s2, i === path.length - 1 ? 8 : 4));
      const x = path[path.length - 1], g = cur.df(x);
      // aktuelle Tangente
      p.fn(t => cur.f(x) + g * (t - x), col.s1, 1, x - 1.2, x + 1.2);
      out.innerHTML = `Schritt ${path.length - 1}: x = ${x.toFixed(4)}, f(x) = ${cur.f(x).toFixed(4)}, f'(x) = ${g.toFixed(4)} &nbsp;→&nbsp; x<sub>neu</sub> = x − η·f'(x) = ${(x - lr * g).toFixed(4)}`;
    };
    p.canvas.addEventListener("click", e => { const r = p.canvas.getBoundingClientRect(); reset(p.wx(e.clientX - r.left)); });
    const ctrl = UI.controls(el);
    UI.button(ctrl, "Ein Schritt", () => step());
    const play = UI.button(ctrl, "▶ Abspielen", () => {
      if (timer) { clearInterval(timer); timer = null; play.textContent = "▶ Abspielen"; return; }
      play.textContent = "⏸ Pause";
      timer = setInterval(() => { if (!step() || path.length > 60) play.click(); }, 350);
    });
    UI.slider(ctrl, "Lernrate η", 0.01, 2.2, 0.01, lr, v => { lr = v; reset(path[0]); }, v => v.toFixed(2));
    Object.keys(fns).forEach(k => UI.button(ctrl, k, () => { cur = fns[k]; reset(); }, true));
    UI.button(ctrl, "Neustart", () => reset(path[0]), true);
    reset();
  };

  // ---------- Gradientenabstieg in 2D ----------
  ANIMS["gd-2d"] = function (el) {
    UI.head(el, "Gradientenabstieg auf einer Fehlerlandschaft", "Ziehe den Startpunkt. Bei einem langgezogenen Tal entsteht der typische Zickzack-Kurs.");
    let k = 6; // Streckung des Tals
    const f = (x, y) => 0.5 * (x * x + k * y * y), g = (x, y) => [x, k * y];
    const p = new Plot(el, { height: 380, pad: 20 });
    const S = { x: -3.5, y: 1.4 };
    let lr = 0.28;
    const out = UI.readout(el);
    p.onDraw = (c, col) => {
      const aspect = (p.W - 40) / (p.H - 40); p.setRange(-2.2 * aspect, 2.2 * aspect, -2.2, 2.2);
      const levels = Array.from({ length: 16 }, (_, i) => 0.05 * (i + 1) ** 2);
      p.contour(f, levels, col.s1);
      let x = S.x, y = S.y, n = 0;
      for (; n < 80; n++) {
        const [gx, gy] = g(x, y), nx = x - lr * gx, ny = y - lr * gy;
        if (Math.abs(nx) > 50 || Math.abs(ny) > 50) break;
        p.line(x, y, nx, ny, col.s2, 2); p.dot(nx, ny, col.s2, 3, false);
        if (Math.hypot(nx - x, ny - y) < 1e-3) { x = nx; y = ny; break; }
        x = nx; y = ny;
      }
      p.dot(0, 0, col.s3, 7);
      p.dot(S.x, S.y, col.text, 9);
      out.textContent = `Nach ${n} Schritten: (x, y) = (${x.toFixed(3)}, ${y.toFixed(3)}), Verlust = ${f(x, y).toExponential(2)}` + (lr * k >= 2 ? "  ⚠ η zu groß für die steile Richtung → divergiert" : "");
    };
    p.draggable(() => [S], (i, x, y) => { S.x = x; S.y = y; });
    const ctrl = UI.controls(el);
    UI.slider(ctrl, "Lernrate η", 0.02, 0.4, 0.01, lr, v => { lr = v; p.draw(); }, v => v.toFixed(2));
    UI.slider(ctrl, "Tal-Streckung", 1, 10, 0.5, k, v => { k = v; p.draw(); }, v => v.toFixed(1));
    UI.legend(el, [["--series-2", "Pfad des Gradientenabstiegs"], ["--series-3", "Minimum"]]);
    p.draw();
  };

  // ---------- Eine Gerade lernen ----------
  ANIMS["regression-live"] = function (el) {
    UI.head(el, "Lineare Regression lernt live", "Links: die Gerade im Datenraum. Rechts: derselbe Zustand als Punkt in der Verlustlandschaft über (w, b).");
    const wrap = document.createElement("div"); wrap.style.cssText = "display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));";
    const L = document.createElement("div"), R = document.createElement("div"); wrap.append(L, R); el.appendChild(wrap);
    const pd = new Plot(L, { height: 320, xmin: 0, xmax: 6, ymin: 0, ymax: 7, pad: 30 });
    const pl = new Plot(R, { height: 320, xmin: -1, xmax: 2.5, ymin: -2, ymax: 4, pad: 30 });
    const n = DATA.length;
    const loss = (w, b) => DATA.reduce((s, [x, y]) => s + (w * x + b - y) ** 2, 0) / n;
    const grad = (w, b) => DATA.reduce(([gw, gb], [x, y]) => { const r = w * x + b - y; return [gw + 2 * r * x / n, gb + 2 * r / n]; }, [0, 0]);
    let w = -0.6, b = 3.5, lr = 0.03, hist = [[w, b]], timer = null, epoch = 0;
    const out = UI.readout(el);
    const levels = Array.from({ length: 18 }, (_, i) => 0.08 * Math.pow(1.45, i));
    pl.onDraw = (c, col) => {
      pl.contour(loss, levels, col.s1, 5);
      pl.grid();
      for (let i = 1; i < hist.length; i++) pl.line(hist[i - 1][0], hist[i - 1][1], hist[i][0], hist[i][1], col.s2, 2);
      pl.dot(w, b, col.s2, 7);
      pl.text("w", 2.5, -2, col.text2, "right", 12, -4, -6); pl.text("b", -1, 4, col.text2, "left", 12, 6, 12);
    };
    pd.onDraw = (c, col) => {
      pd.grid();
      DATA.forEach(([x, y]) => pd.line(x, y, x, w * x + b, col.s2, 1.5));
      pd.fn(x => w * x + b, col.s1, 2.5);
      DATA.forEach(([x, y]) => pd.dot(x, y, col.text, 6));
    };
    function render() {
      pd.draw(); pl.draw();
      const [gw, gb] = grad(w, b);
      out.innerHTML = `Epoche ${epoch}: w = ${w.toFixed(3)}, b = ${b.toFixed(3)}, MSE = <b>${loss(w, b).toFixed(4)}</b>, ∇ = (${gw.toFixed(3)}, ${gb.toFixed(3)})`;
    }
    function step() {
      const [gw, gb] = grad(w, b); w -= lr * gw; b -= lr * gb; epoch++;
      hist.push([w, b]); if (hist.length > 400) hist.shift(); render();
    }
    function reset() { w = -0.6; b = 3.5; hist = [[w, b]]; epoch = 0; render(); }
    pl.canvas.addEventListener("click", e => { const r = pl.canvas.getBoundingClientRect(); w = pl.wx(e.clientX - r.left); b = pl.wy(e.clientY - r.top); hist = [[w, b]]; epoch = 0; render(); });
    const ctrl = UI.controls(el);
    UI.button(ctrl, "Ein Schritt", step);
    const play = UI.button(ctrl, "▶ Trainieren", () => {
      if (timer) { clearInterval(timer); timer = null; play.textContent = "▶ Trainieren"; return; }
      play.textContent = "⏸ Pause"; timer = setInterval(() => { step(); if (epoch > 600) play.click(); }, 40);
    });
    UI.slider(ctrl, "Lernrate η", 0.005, 0.07, 0.001, lr, v => { lr = v; }, v => v.toFixed(3));
    UI.button(ctrl, "Zurücksetzen", reset, true);
    const tip = document.createElement("span"); tip.style.color = "var(--muted)"; tip.textContent = "Tipp: Klick rechts setzt (w, b).";
    ctrl.appendChild(tip);
    reset();
  };
})();
