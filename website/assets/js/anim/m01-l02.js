// Animationen für Lektion 1.2 – Vektoren, Matrizen & Daten
(function () {
  const { Plot, UI } = ML;
  const f2 = v => (Math.abs(v) < 0.005 ? 0 : v).toFixed(2);

  // Gleichmäßige Achsen: Weltbereich so wählen, dass 1 Einheit in x und y gleich lang ist.
  function equalRange(p, half) {
    const aspect = (p.W - 2 * p.opts.pad) / (p.H - 2 * p.opts.pad);
    p.setRange(-half * aspect, half * aspect, -half, half);
  }

  // ---------- Skalarprodukt & Projektion ----------
  ANIMS["skalarprodukt"] = function (el) {
    UI.head(el, "Skalarprodukt & Projektion", "Ziehe die Pfeilspitzen von a und b.");
    const p = new Plot(el, { height: 380, pad: 20 });
    const a = { x: 3, y: 1 }, b = { x: 1.5, y: 2.5 };
    const out = UI.readout(el);
    p.onDraw = (c, col) => {
      equalRange(p, 4);
      p.grid(false);
      const dot = a.x * b.x + a.y * b.y, la = Math.hypot(a.x, a.y), lb = Math.hypot(b.x, b.y);
      // Projektion von b auf a
      const t = dot / (la * la), px = a.x * t, py = a.y * t;
      p.line(b.x, b.y, px, py, col.axis, 1.5, [4, 4]);
      p.line(0, 0, px, py, col.s3, 7);
      p.arrow(0, 0, a.x, a.y, col.s1);
      p.arrow(0, 0, b.x, b.y, col.s2);
      p.text("a", a.x, a.y, col.s1, "left", 15, 8, -6);
      p.text("b", b.x, b.y, col.s2, "left", 15, 8, -6);
      const ang = Math.acos(Math.max(-1, Math.min(1, dot / (la * lb || 1)))) * 180 / Math.PI;
      out.innerHTML = `a·b = ${f2(a.x)}·${f2(b.x)} + ${f2(a.y)}·${f2(b.y)} = <b>${f2(dot)}</b> &nbsp;|&nbsp; ‖a‖ = ${f2(la)}, ‖b‖ = ${f2(lb)} &nbsp;|&nbsp; Winkel = ${ang.toFixed(0)}° &nbsp;|&nbsp; ` +
        (Math.abs(dot) < 0.15 ? "≈ orthogonal (a·b ≈ 0)" : dot > 0 ? "gleiche Richtung (a·b > 0)" : "entgegengesetzt (a·b < 0)");
    };
    p.draggable(() => [a, b], (i, x, y) => {
      const v = i === 0 ? a : b; v.x = Math.round(x * 10) / 10; v.y = Math.round(y * 10) / 10;
    });
    UI.legend(el, [["--series-1", "a"], ["--series-2", "b"], ["--series-3", "Projektion von b auf a"]]);
    p.draw();
  };

  // ---------- Matrix als lineare Abbildung ----------
  ANIMS["matrix-transformation"] = function (el) {
    UI.head(el, "Eine Matrix verformt den Raum", "Die Spalten der Matrix sind die Bilder der Einheitsvektoren.");
    const p = new Plot(el, { height: 380, pad: 20 });
    let M = [[1, 0], [0, 1]], tAnim = 1;
    const out = UI.readout(el);
    function cur() { // Interpolation von Einheitsmatrix zu M für die Animation
      return [[1 + (M[0][0] - 1) * tAnim, M[0][1] * tAnim], [M[1][0] * tAnim, 1 + (M[1][1] - 1) * tAnim]];
    }
    p.onDraw = (c, col) => {
      equalRange(p, 4);
      p.grid(false);
      const A = cur();
      const T = (x, y) => [A[0][0] * x + A[0][1] * y, A[1][0] * x + A[1][1] * y];
      c.globalAlpha = 0.55;
      for (let k = -8; k <= 8; k++) {
        let s = T(k, -8), e = T(k, 8); p.line(s[0], s[1], e[0], e[1], col.s1, 1);
        s = T(-8, k); e = T(8, k); p.line(s[0], s[1], e[0], e[1], col.s1, 1);
      }
      c.globalAlpha = 1;
      // Einheitsquadrat und seine Fläche (= Determinante)
      const q = [T(0, 0), T(1, 0), T(1, 1), T(0, 1)];
      c.beginPath(); q.forEach((v, i) => (i ? c.lineTo : c.moveTo).call(c, p.sx(v[0]), p.sy(v[1]))); c.closePath();
      c.fillStyle = col.s3; c.globalAlpha = 0.3; c.fill(); c.globalAlpha = 1;
      const i1 = T(1, 0), j1 = T(0, 1);
      p.arrow(0, 0, i1[0], i1[1], col.s2, 3); p.arrow(0, 0, j1[0], j1[1], col.s3, 3);
      p.text("î", i1[0], i1[1], col.s2, "left", 15, 6, -6); p.text("ĵ", j1[0], j1[1], col.s3, "left", 15, 6, -6);
      const det = A[0][0] * A[1][1] - A[0][1] * A[1][0];
      out.textContent = `M = [[${f2(A[0][0])}, ${f2(A[0][1])}], [${f2(A[1][0])}, ${f2(A[1][1])}]]   det(M) = ${f2(det)} (Flächenfaktor)`;
    };
    const ctrl = UI.controls(el);
    const sl = [];
    [["a₁₁", 0, 0], ["a₁₂", 0, 1], ["a₂₁", 1, 0], ["a₂₂", 1, 1]].forEach(([lab, i, j]) => {
      sl.push(UI.slider(ctrl, lab, -2, 2, 0.1, M[i][j], v => { M[i][j] = v; tAnim = 1; p.draw(); }, v => v.toFixed(1)));
    });
    const presets = { "Drehung 45°": [[.7, -.7], [.7, .7]], "Scherung": [[1, 1], [0, 1]], "Streckung": [[2, 0], [0, .5]], "Spiegelung": [[-1, 0], [0, 1]], "Singulär": [[1, 2], [.5, 1]] };
    Object.entries(presets).forEach(([name, P]) => UI.button(ctrl, name, () => {
      M = P.map(r => r.slice()); sl.forEach((s, k) => s.set(M[k >> 1][k & 1]));
      const t0 = performance.now();
      const run = now => { tAnim = Math.min(1, (now - t0) / 900); tAnim = tAnim * tAnim * (3 - 2 * tAnim); p.draw(); if (tAnim < 1) requestAnimationFrame(run); };
      requestAnimationFrame(run);
    }, true));
    p.draw();
  };

  // ---------- Distanzmaße ----------
  ANIMS["distanzen"] = function (el) {
    UI.head(el, "Wie weit sind zwei Datenpunkte voneinander entfernt?", "Ziehe die Punkte. Euklidisch = Luftlinie, Manhattan = entlang der Achsen.");
    const p = new Plot(el, { height: 320, pad: 20 });
    const P = { x: -2, y: -1 }, Q = { x: 2, y: 1.5 };
    const out = UI.readout(el);
    p.onDraw = (c, col) => {
      equalRange(p, 3);
      p.grid(false);
      p.line(P.x, P.y, Q.x, P.y, col.s2, 3); p.line(Q.x, P.y, Q.x, Q.y, col.s2, 3);
      p.line(P.x, P.y, Q.x, Q.y, col.s1, 3);
      p.dot(P.x, P.y, col.text, 8); p.dot(Q.x, Q.y, col.text, 8);
      p.text("P", P.x, P.y, col.text, "right", 14, -10, -8); p.text("Q", Q.x, Q.y, col.text, "left", 14, 10, -8);
      const dx = Q.x - P.x, dy = Q.y - P.y;
      out.innerHTML = `Euklidisch (L2): √(${f2(dx)}² + ${f2(dy)}²) = <b>${f2(Math.hypot(dx, dy))}</b> &nbsp;|&nbsp; Manhattan (L1): |${f2(dx)}| + |${f2(dy)}| = <b>${f2(Math.abs(dx) + Math.abs(dy))}</b>`;
    };
    p.draggable(() => [P, Q], (i, x, y) => { const v = i ? Q : P; v.x = x; v.y = y; });
    UI.legend(el, [["--series-1", "Euklidische Distanz"], ["--series-2", "Manhattan-Distanz"]]);
    p.draw();
  };
})();
