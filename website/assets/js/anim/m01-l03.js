// Animationen für Lektion 1.3 – Statistik & Wahrscheinlichkeit
(function () {
  const { Plot, UI } = ML;

  // ---------- Mittelwert & Standardabweichung ----------
  ANIMS["mittelwert-varianz"] = function (el) {
    UI.head(el, "Mittelwert und Streuung", "Ziehe die Punkte entlang der Achse. Beobachte, wie ein Ausreißer den Mittelwert, aber kaum den Median verschiebt.");
    const p = new Plot(el, { height: 200, xmin: 0, xmax: 20, ymin: -1, ymax: 2, pad: 24 });
    const pts = [4, 6, 7, 8, 8.5, 9, 10, 12].map(x => ({ x, y: 0 }));
    const out = UI.readout(el);
    p.onDraw = (c, col) => {
      const xs = pts.map(q => q.x), n = xs.length;
      const mean = xs.reduce((a, b) => a + b) / n;
      const varc = xs.reduce((a, b) => a + (b - mean) ** 2, 0) / n, sd = Math.sqrt(varc);
      const s = xs.slice().sort((a, b) => a - b), med = (s[n / 2 - 1] + s[n / 2]) / 2;
      // ±1 Standardabweichung als Band
      c.fillStyle = col.s1; c.globalAlpha = 0.15;
      c.fillRect(p.sx(mean - sd), p.sy(1.4), p.sx(mean + sd) - p.sx(mean - sd), p.sy(-0.6) - p.sy(1.4)); c.globalAlpha = 1;
      p.line(0, 0, 20, 0, col.axis, 1);
      for (let x = 0; x <= 20; x += 2) p.text(String(x), x, 0, col.axis, "center", 11, 0, 20);
      p.line(mean, -0.6, mean, 1.4, col.s1, 2.5); p.text("Mittelwert", mean, 1.4, col.s1, "center", 12, 0, -6);
      p.line(med, -0.6, med, 1.0, col.s2, 2.5, [5, 4]); p.text("Median", med, 1.0, col.s2, "center", 12, 0, -6);
      pts.forEach(q => p.dot(q.x, q.y, col.text, 7));
      out.textContent = `μ = ${mean.toFixed(2)}   Median = ${med.toFixed(2)}   σ² = ${varc.toFixed(2)}   σ = ${sd.toFixed(2)}   (Band = μ ± σ)`;
    };
    p.draggable(() => pts, (i, x) => { pts[i].x = Math.max(0, Math.min(20, x)); }, 16);
    UI.legend(el, [["--series-1", "Mittelwert μ und Band μ ± σ"], ["--series-2", "Median"]]);
    p.draw();
  };

  // ---------- Normalverteilung ----------
  ANIMS["normalverteilung"] = function (el) {
    UI.head(el, "Die Normalverteilung", "Verschiebe μ und ändere σ. Die Fläche unter der Kurve bleibt immer 1.");
    const p = new Plot(el, { height: 300, xmin: -6, xmax: 6, ymin: 0, ymax: 0.9, pad: 30 });
    let mu = 0, sd = 1;
    const pdf = (x, m, s) => Math.exp(-((x - m) ** 2) / (2 * s * s)) / (s * Math.sqrt(2 * Math.PI));
    p.onDraw = (c, col) => {
      p.grid();
      // 68-95-99,7-Regel als Flächen
      [[3, 0.12], [2, 0.18], [1, 0.3]].forEach(([k, a]) => {
        c.beginPath(); c.moveTo(p.sx(mu - k * sd), p.sy(0));
        for (let i = 0; i <= 100; i++) { const x = mu - k * sd + 2 * k * sd * i / 100; c.lineTo(p.sx(x), p.sy(pdf(x, mu, sd))); }
        c.lineTo(p.sx(mu + k * sd), p.sy(0)); c.closePath(); c.fillStyle = col.s1; c.globalAlpha = a; c.fill(); c.globalAlpha = 1;
      });
      p.fn(x => pdf(x, 0, 1), col.axis, 1.5);
      p.fn(x => pdf(x, mu, sd), col.s1, 2.5);
      p.text("68 %", mu, pdf(mu, mu, sd) * 0.35, col.text, "center", 12);
    };
    const ctrl = UI.controls(el);
    UI.slider(ctrl, "μ", -3, 3, 0.1, mu, v => { mu = v; p.draw(); }, v => v.toFixed(1));
    UI.slider(ctrl, "σ", 0.5, 3, 0.1, sd, v => { sd = v; p.draw(); }, v => v.toFixed(1));
    UI.legend(el, [["--series-1", "N(μ, σ²) mit Bereichen ±1σ / ±2σ / ±3σ"], ["--muted", "Standardnormalverteilung N(0, 1)"]]);
    p.draw();
  };

  // ---------- Zentraler Grenzwertsatz ----------
  ANIMS["grenzwertsatz"] = function (el) {
    UI.head(el, "Zentraler Grenzwertsatz", "Wir würfeln n Würfel und notieren den Mittelwert. Egal wie die Einzelverteilung aussieht – die Mittelwerte werden normalverteilt.");
    const p = new Plot(el, { height: 300, xmin: 0.5, xmax: 6.5, ymin: 0, ymax: 1, pad: 30 });
    let n = 1, counts, total, timer = null;
    // Ein Balken pro möglicher Augensumme s = n … 6n, also pro möglichem Mittelwert s/n.
    function reset() { counts = new Array(5 * n + 1).fill(0); total = 0; }
    function sample(k) {
      for (let r = 0; r < k; r++) {
        let s = 0; for (let i = 0; i < n; i++) s += 1 + Math.floor(Math.random() * 6);
        counts[s - n]++; total++;
      }
    }
    const out = UI.readout(el);
    p.onDraw = (c, col) => {
      p.grid(false);
      for (let x = 1; x <= 6; x++) p.text(String(x), x, 0, col.axis, "center", 11, 0, 16);
      const max = Math.max(1, ...counts), w = 1 / n;
      counts.forEach((v, i) => {
        if (!v) return;
        const m = (i + n) / n, h = v / max * 0.95;
        const X0 = p.sx(m - w / 2), X1 = p.sx(m + w / 2), gap = Math.min(2, (X1 - X0) * 0.2);
        c.fillStyle = col.s1;
        c.beginPath(); c.roundRect(X0 + gap / 2, p.sy(h), X1 - X0 - gap, p.sy(0) - p.sy(h), [3, 3, 0, 0]); c.fill();
      });
      // theoretische Normalverteilung: μ = 3,5, σ² = (35/12) / n; erwartete Anzahl je Balken = total · w · Dichte
      if (n > 1 && total > 50) {
        const sd = Math.sqrt(35 / 12 / n);
        const pdf = x => Math.exp(-((x - 3.5) ** 2) / (2 * sd * sd)) / (sd * Math.sqrt(2 * Math.PI));
        p.fn(x => total * w * pdf(x) / max * 0.95, col.s2, 2);
      }
      out.textContent = `n = ${n} Würfel pro Wurf · ${total} Würfe`;
    };
    const ctrl = UI.controls(el);
    const play = UI.button(ctrl, "▶ Würfeln", () => {
      if (timer) { clearInterval(timer); timer = null; play.textContent = "▶ Würfeln"; return; }
      play.textContent = "⏸ Pause";
      timer = setInterval(() => { sample(Math.max(5, Math.floor(total / 20))); p.draw(); if (total > 20000) play.click(); }, 50);
    });
    UI.slider(ctrl, "n =", 1, 30, 1, n, v => { n = v; reset(); p.draw(); });
    UI.button(ctrl, "Zurücksetzen", () => { reset(); p.draw(); }, true);
    UI.legend(el, [["--series-1", "Histogramm der Mittelwerte"], ["--series-2", "theoretische Normalverteilung"]]);
    reset(); p.draw();
  };

  // ---------- Satz von Bayes ----------
  ANIMS["bayes"] = function (el) {
    UI.head(el, "Satz von Bayes: der medizinische Test", "1000 Personen. Wie wahrscheinlich ist man wirklich krank, wenn der Test positiv ist?");
    const p = new Plot(el, { height: 340, xmin: 0, xmax: 1, ymin: 0, ymax: 1, pad: 10 });
    let prev = 0.01, sens = 0.95, spec = 0.95;
    const out = UI.readout(el);
    p.onDraw = (c, col) => {
      const N = 1000, cols = 50, rows = 20;
      const sick = Math.round(N * prev), tp = Math.round(sick * sens), fp = Math.round((N - sick) * (1 - spec));
      const cw = (p.W - 20) / cols, ch = (p.H - 20) / rows, r = Math.min(cw, ch) * 0.36;
      for (let i = 0; i < N; i++) {
        const cx = 10 + (i % cols + 0.5) * cw, cy = 10 + (Math.floor(i / cols) + 0.5) * ch;
        // Reihenfolge: richtig positiv, falsch negativ, falsch positiv, richtig negativ
        let fill, ring = null;
        if (i < tp) { fill = col.bad; ring = col.text; }
        else if (i < sick) fill = col.bad;
        else if (i < sick + fp) { fill = col.grid; ring = col.text; }
        else fill = col.grid;
        c.beginPath(); c.arc(cx, cy, r, 0, 2 * Math.PI); c.fillStyle = fill; c.fill();
        if (ring) { c.lineWidth = 2; c.strokeStyle = ring; c.stroke(); }
      }
      const post = tp / Math.max(1, tp + fp);
      out.innerHTML = `Krank: ${sick} · davon positiv getestet: ${tp} · Gesunde mit positivem Test: ${fp}<br>` +
        `P(krank | positiv) = ${tp} / (${tp} + ${fp}) = <b>${(post * 100).toFixed(1)} %</b>`;
    };
    const ctrl = UI.controls(el);
    UI.slider(ctrl, "Häufigkeit", 0.001, 0.3, 0.001, prev, v => { prev = v; p.draw(); }, v => (v * 100).toFixed(1) + " %");
    UI.slider(ctrl, "Sensitivität", 0.5, 1, 0.01, sens, v => { sens = v; p.draw(); }, v => (v * 100).toFixed(0) + " %");
    UI.slider(ctrl, "Spezifität", 0.5, 1, 0.005, spec, v => { spec = v; p.draw(); }, v => (v * 100).toFixed(1) + " %");
    UI.legend(el, [["--bad", "krank"], ["--grid", "gesund"], ["--text", "Ring = Test positiv"]]);
    p.draw();
  };
})();
