// Animationen für Lektion 1.1 – Was ist Machine Learning?
(function () {
  const { Plot, UI, stepper } = ML;

  // Zeichnet eine abgerundete Box mit Text in Weltkoordinaten.
  function box(p, x, y, w, h, label, color, filled) {
    const c = p.ctx, X = p.sx(x), Y = p.sy(y + h), W = p.sx(x + w) - X, H = p.sy(y) - Y;
    c.beginPath(); c.roundRect(X, Y, W, H, 10);
    c.fillStyle = filled ? color : p.color.bg; c.fill();
    c.lineWidth = 2; c.strokeStyle = color; c.stroke();
    c.fillStyle = filled ? "#fff" : p.color.text; c.font = `600 14px ${ML.cssVar("--font")}`; c.textAlign = "center";
    label.split("\n").forEach((line, i, arr) => c.fillText(line, X + W / 2, Y + H / 2 + 5 + (i - (arr.length - 1) / 2) * 18));
  }

  // ---------- Klassische Programmierung vs. Machine Learning ----------
  ANIMS["regel-vs-ml"] = function (el) {
    UI.head(el, "Klassisches Programmieren vs. Machine Learning", "Was geht rein, was kommt raus?");
    const p = new Plot(el, { height: 300, xmin: 0, xmax: 12, ymin: 0, ymax: 6, pad: 10 });
    function classic(p, col, hl) {
      p.text("Klassisch", 0.3, 5.4, col.text2, "left", 13);
      box(p, 0.3, 3.4, 2.6, 1.2, "Daten", col.s1);
      box(p, 0.3, 1.4, 2.6, 1.2, "Regeln\n(von Hand)", col.s2);
      box(p, 4.4, 2.4, 3, 1.2, "Programm", col.text2, false);
      box(p, 8.9, 2.4, 2.8, 1.2, "Antworten", col.s3);
      p.arrow(2.9, 4.0, 4.4, 3.2, col.axis); p.arrow(2.9, 2.0, 4.4, 2.8, col.axis); p.arrow(7.4, 3.0, 8.9, 3.0, col.axis);
    }
    function ml(p, col) {
      p.text("Machine Learning", 0.3, 5.4, col.text2, "left", 13);
      box(p, 0.3, 3.4, 2.6, 1.2, "Daten", col.s1);
      box(p, 0.3, 1.4, 2.6, 1.2, "Antworten\n(Labels)", col.s3);
      box(p, 4.4, 2.4, 3, 1.2, "Lernalgorithmus", col.text2, false);
      box(p, 8.9, 2.4, 2.8, 1.2, "Regeln =\nModell", col.s2);
      p.arrow(2.9, 4.0, 4.4, 3.2, col.axis); p.arrow(2.9, 2.0, 4.4, 2.8, col.axis); p.arrow(7.4, 3.0, 8.9, 3.0, col.axis);
    }
    stepper(el, p, [
      { text: "Beim <b>klassischen Programmieren</b> schreibst du die Regeln selbst, z.&nbsp;B. <code>if \"Gewinnspiel\" in mail: spam = True</code>. Das Programm wendet sie auf Daten an und liefert Antworten.",
        draw: (p, c, col) => classic(p, col) },
      { text: "Das Problem: Für viele Aufgaben kennen wir die Regeln nicht oder sie sind zu kompliziert – wie erkennst du eine Katze auf einem Foto, Pixel für Pixel?",
        draw: (p, c, col) => { classic(p, col); p.text("?", 1.6, 1.0, col.bad, "center", 30); } },
      { text: "Beim <b>Machine Learning</b> drehen wir es um: Wir geben <b>Daten und die richtigen Antworten</b> (Labels). Ein Lernalgorithmus findet die Regeln selbst.",
        draw: (p, c, col) => ml(p, col) },
      { text: "Das Ergebnis ist ein <b>Modell</b> – eine Funktion \\(f(x)\\), die gelernte Regeln enthält. Es wird anschließend auf <b>neue, ungesehene</b> Daten angewendet (Inferenz / <span class='term'>Inference</span>).",
        draw: (p, c, col) => { ml(p, col); p.arrow(10.3, 2.4, 10.3, 1.1, col.accent); p.text("neue Daten → Vorhersage", 10.3, 0.5, col.accent, "center", 13); } }
    ]);
  };

  // ---------- Lernen aus Beispielen: Klick-Spielplatz mit k-Nächste-Nachbarn ----------
  ANIMS["lern-spielplatz"] = function (el) {
    UI.head(el, "Lernen aus Beispielen", "Klicke ins Feld, um Beispiele hinzuzufügen. Das Modell färbt jeden Ort nach seinen k nächsten Nachbarn.");
    const p = new Plot(el, { height: 360, xmin: 0, xmax: 10, ymin: 0, ymax: 6, pad: 12 });
    let cls = 0, k = 3;
    let pts = [
      { x: 2, y: 4.5, c: 0 }, { x: 2.8, y: 3.8, c: 0 }, { x: 1.5, y: 3.2, c: 0 }, { x: 3.1, y: 4.9, c: 0 },
      { x: 7, y: 1.5, c: 1 }, { x: 7.8, y: 2.4, c: 1 }, { x: 6.2, y: 1.0, c: 1 }, { x: 8.3, y: 1.2, c: 1 }
    ];
    function predict(x, y) {
      const d = pts.map(q => [Math.hypot(q.x - x, q.y - y), q.c]).sort((a, b) => a[0] - b[0]).slice(0, k);
      const votes = d.filter(v => v[1] === 1).length;
      return votes / d.length;
    }
    p.onDraw = (c, col) => {
      if (pts.length) {
        const step = 8;
        for (let px = 0; px < p.W; px += step) for (let py = 0; py < p.H; py += step) {
          const v = predict(p.wx(px + step / 2), p.wy(py + step / 2));
          c.globalAlpha = 0.22;
          c.fillStyle = v > 0.5 ? col.s2 : v < 0.5 ? col.s1 : col.grid;
          c.fillRect(px, py, step, step);
        }
        c.globalAlpha = 1;
      }
      pts.forEach(q => p.dot(q.x, q.y, q.c ? col.s2 : col.s1, 7));
    };
    p.canvas.addEventListener("click", e => {
      const r = p.canvas.getBoundingClientRect();
      pts.push({ x: p.wx(e.clientX - r.left), y: p.wy(e.clientY - r.top), c: cls });
      p.draw();
    });
    UI.legend(el, [["--series-1", "Klasse A"], ["--series-2", "Klasse B"]]);
    const ctrl = UI.controls(el);
    const btn = UI.button(ctrl, "Neue Punkte: Klasse A", () => {
      cls = 1 - cls; btn.textContent = "Neue Punkte: Klasse " + (cls ? "B" : "A");
    }, true);
    UI.slider(ctrl, "k =", 1, 9, 1, k, v => { k = v; p.draw(); });
    UI.button(ctrl, "Alles löschen", () => { pts = []; p.draw(); }, true);
    p.draw();
  };

  // ---------- Die drei Lernarten ----------
  ANIMS["lernarten"] = function (el) {
    UI.head(el, "Die drei großen Lernarten", "Überwacht, unüberwacht, bestärkend");
    const p = new Plot(el, { height: 320, xmin: 0, xmax: 10, ymin: 0, ymax: 6, pad: 14 });
    // feste Pseudo-Zufallspunkte, damit die Grafik stabil bleibt
    let seed = 7; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
    const gauss = () => { let s = 0; for (let i = 0; i < 6; i++) s += rnd(); return s - 3; };
    const A = Array.from({ length: 18 }, () => ({ x: 3 + gauss() * .7, y: 4 + gauss() * .6 }));
    const B = Array.from({ length: 18 }, () => ({ x: 7 + gauss() * .7, y: 2 + gauss() * .6 }));
    const C = Array.from({ length: 18 }, () => ({ x: 7.2 + gauss() * .5, y: 4.6 + gauss() * .4 }));
    const grid = (p, col, path) => {
      for (let i = 0; i < 5; i++) for (let j = 0; j < 4; j++) {
        p.ctx.strokeStyle = col.grid; p.ctx.lineWidth = 1;
        p.ctx.strokeRect(p.sx(2.5 + i), p.sy(1 + j + 1), p.sx(1) - p.sx(0), p.sy(0) - p.sy(1));
      }
      p.text("🏁", 7, 4.35, col.text, "center", 20); p.text("🔥", 4, 2.35, col.text, "center", 20);
      path.forEach((q, i) => { if (i) p.line(path[i - 1][0], path[i - 1][1], q[0], q[1], col.s3, 3); });
      const last = path[path.length - 1]; p.text("🤖", last[0], last[1] - .15, col.text, "center", 22);
    };
    stepper(el, p, [
      { text: "<b>Überwachtes Lernen</b> (<span class='term'>Supervised Learning</span>): Jedes Beispiel hat ein <b>Label</b>. Das Modell lernt die Zuordnung Eingabe → Label. Beispiele: Spam-Filter, Hauspreis-Vorhersage.",
        draw: (p, c, col) => { A.forEach(q => p.dot(q.x, q.y, col.s1, 6)); B.forEach(q => p.dot(q.x, q.y, col.s2, 6)); } },
      { text: "Das Modell lernt eine <b>Entscheidungsgrenze</b>. Ist das Label eine Kategorie, heißt das <b>Klassifikation</b>; ist es eine Zahl, <b>Regression</b>.",
        draw: (p, c, col) => { A.forEach(q => p.dot(q.x, q.y, col.s1, 6)); B.forEach(q => p.dot(q.x, q.y, col.s2, 6)); p.line(2, .3, 8.5, 5.8, col.text, 2, [6, 5]); } },
      { text: "<b>Unüberwachtes Lernen</b> (<span class='term'>Unsupervised Learning</span>): Es gibt <b>keine Labels</b>. Der Algorithmus sucht selbst Struktur – z.&nbsp;B. Gruppen (Clustering) oder Ausreißer.",
        draw: (p, c, col) => { [...A, ...B, ...C].forEach(q => p.dot(q.x, q.y, col.axis, 6)); } },
      { text: "Ein Clustering-Algorithmus wie k-Means findet hier drei Gruppen – ohne dass ihm jemand gesagt hat, was die Gruppen bedeuten.",
        draw: (p, c, col) => { A.forEach(q => p.dot(q.x, q.y, col.s1, 6)); B.forEach(q => p.dot(q.x, q.y, col.s2, 6)); C.forEach(q => p.dot(q.x, q.y, col.s3, 6)); } },
      { text: "<b>Bestärkendes Lernen</b> (<span class='term'>Reinforcement Learning</span>): Ein <b>Agent</b> handelt in einer Umgebung und bekommt <b>Belohnungen</b> oder Strafen. Er lernt durch Ausprobieren eine Strategie.",
        draw: (p, c, col) => grid(p, col, [[3, 1.5]]) },
      { text: "Nach vielen Versuchen hat der Agent gelernt, das Feuer zu meiden und das Ziel zu erreichen. So lernen z.&nbsp;B. Spiel-KIs und Roboter.",
        draw: (p, c, col) => grid(p, col, [[3, 1.5], [3, 2.5], [3, 3.5], [4, 3.5], [5, 3.5], [6, 3.5], [7, 3.5], [7, 4.5]]) }
    ]);
  };
})();
