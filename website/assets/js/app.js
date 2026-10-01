// Gemeinsame Logik für alle Seiten: Layout, Theme, Fortschritt, Quiz, Formeln, Animationen.
(function () {
  "use strict";

  // ---------- Speicher (Fortschritt bleibt im Browser) ----------
  const STORE_KEY = "mlkurs.v1";
  const Store = {
    load() {
      try { return JSON.parse(localStorage.getItem(STORE_KEY)) || {}; } catch (e) { return {}; }
    },
    save(data) {
      try { localStorage.setItem(STORE_KEY, JSON.stringify(data)); } catch (e) { /* privates Fenster o. Ä. */ }
    },
    get(key, fallback) { const d = this.load(); return key in d ? d[key] : fallback; },
    set(key, value) { const d = this.load(); d[key] = value; this.save(d); }
  };
  const Progress = {
    isDone(id) { return !!(Store.get("done", {})[id]); },
    setDone(id, value) {
      const done = Store.get("done", {});
      if (value) done[id] = Date.now(); else delete done[id];
      Store.set("done", done);
    },
    quizScore(id) { return Store.get("quiz", {})[id] || null; },
    setQuizScore(id, score) { const q = Store.get("quiz", {}); q[id] = score; Store.set("quiz", q); },
    moduleRatio(mod) {
      if (!mod.lessons) return 0;
      return mod.lessons.filter(l => this.isDone(l.id)).length / mod.lessons.length;
    }
  };

  // ---------- Theme ----------
  function applyTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    Store.set("theme", theme);
    document.dispatchEvent(new CustomEvent("themechange"));
  }
  document.documentElement.setAttribute("data-theme", Store.get("theme", "dark"));

  function cssVar(name) {
    return getComputedStyle(document.documentElement).getPropertyValue(name).trim();
  }

  // ---------- Layout für Lektionsseiten ----------
  function buildTopbar(root) {
    const bar = document.createElement("header");
    bar.className = "topbar";
    bar.innerHTML = `
      <button class="icon-btn" id="nav-toggle" aria-label="Navigation öffnen">☰</button>
      <a class="brand" href="${root}index.html">ML-Kurs</a>
      <span class="spacer"></span>
      <button class="icon-btn" id="theme-toggle" aria-label="Hell/Dunkel umschalten">◐ Theme</button>`;
    document.body.prepend(bar);
    bar.querySelector("#theme-toggle").addEventListener("click", () => {
      applyTheme(document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark");
    });
    return bar;
  }

  function findLesson(id) {
    for (const m of COURSE.modules) {
      if (!m.lessons) continue;
      const i = m.lessons.findIndex(l => l.id === id);
      if (i >= 0) return { module: m, lesson: m.lessons[i], index: i };
    }
    return null;
  }

  function buildSidebar(current, root) {
    const aside = document.createElement("nav");
    aside.className = "sidebar";
    let html = "";
    for (const m of COURSE.modules) {
      if (m.status !== "fertig") continue;
      html += `<h4>Modul ${m.nr} · ${m.title}</h4>
        <div class="module-progress"><div data-mod="${m.id}"></div></div><ol>`;
      for (const l of m.lessons) {
        const href = `${root}${m.dir}/${l.file}`;
        const active = current && l.id === current.lesson.id ? " active" : "";
        html += `<li data-lesson="${l.id}"><a class="${active}" href="${href}">
          <span class="check">○</span><span>${l.project ? "🛠 " : ""}${l.title}</span></a></li>`;
      }
      html += `</ol>`;
    }
    html += `<h4>Weitere Module</h4><ol>`;
    for (const m of COURSE.modules) {
      if (m.status === "fertig") continue;
      html += `<li><a href="${root}index.html#${m.id}"><span class="check">·</span><span>${m.nr}. ${m.title}</span></a></li>`;
    }
    html += `</ol>`;
    aside.innerHTML = html;
    return aside;
  }

  function refreshSidebar() {
    document.querySelectorAll(".sidebar li[data-lesson]").forEach(li => {
      const done = Progress.isDone(li.dataset.lesson);
      li.classList.toggle("done", done);
      li.querySelector(".check").textContent = done ? "✓" : "○";
    });
    document.querySelectorAll(".sidebar [data-mod]").forEach(bar => {
      const mod = COURSE.modules.find(m => m.id === bar.dataset.mod);
      bar.style.width = Math.round(Progress.moduleRatio(mod) * 100) + "%";
    });
  }

  function buildLessonFooter(current, root) {
    const { module: m, index } = current;
    const prev = m.lessons[index - 1];
    const next = m.lessons[index + 1];
    const box = document.createElement("div");
    box.innerHTML = `
      <div class="complete-box">
        <p id="complete-text"></p>
        <button class="btn" id="complete-btn"></button>
      </div>
      <div class="lesson-footer">
        ${prev ? `<a class="btn secondary" href="${prev.file}">← ${prev.title}</a>` : `<a class="btn secondary" href="${root}index.html">← Kursübersicht</a>`}
        ${next ? `<a class="btn" href="${next.file}">${next.title} →</a>` : `<a class="btn" href="${root}index.html">Zur Kursübersicht →</a>`}
      </div>`;
    const btn = box.querySelector("#complete-btn");
    const txt = box.querySelector("#complete-text");
    const cbox = box.querySelector(".complete-box");
    function render() {
      const done = Progress.isDone(current.lesson.id);
      cbox.classList.toggle("is-done", done);
      txt.textContent = done ? "✓ Diese Lektion ist als erledigt markiert." : "Alles verstanden und das Quiz gemacht?";
      btn.textContent = done ? "Als unerledigt markieren" : "Lektion als erledigt markieren";
      btn.classList.toggle("secondary", done);
    }
    btn.addEventListener("click", () => {
      Progress.setDone(current.lesson.id, !Progress.isDone(current.lesson.id));
      render(); refreshSidebar();
    });
    render();
    return box;
  }

  // ---------- Quiz ----------
  function mountQuiz(el) {
    const id = el.dataset.quiz;
    const data = JSON.parse(el.querySelector("script[type='application/json']").textContent);
    const prev = Progress.quizScore(id);
    el.classList.add("quiz");
    el.innerHTML = `<h3>Quiz: Teste dein Verständnis</h3>
      <p class="score">${prev ? `Letztes Ergebnis: ${prev.correct} / ${prev.total}` : `${data.length} Fragen – sofortiges Feedback mit Erklärung.`}</p>`;
    let answered = 0, correct = 0;
    data.forEach((item, qi) => {
      const q = document.createElement("div");
      q.className = "q";
      q.innerHTML = `<p class="qtext">${qi + 1}. ${item.q}</p>`;
      const explain = document.createElement("div");
      explain.className = "explain";
      item.options.forEach((opt, oi) => {
        const b = document.createElement("button");
        b.className = "opt";
        b.innerHTML = opt;
        b.addEventListener("click", () => {
          const buttons = q.querySelectorAll(".opt");
          buttons.forEach(x => (x.disabled = true));
          buttons[item.answer].classList.add("correct");
          const ok = oi === item.answer;
          if (!ok) b.classList.add("wrong");
          explain.innerHTML = `<b class="${ok ? "ok" : "no"}">${ok ? "Richtig!" : "Nicht ganz."}</b> ${item.explain}`;
          explain.classList.add("show");
          renderMath(explain);
          answered++; if (ok) correct++;
          if (answered === data.length) {
            Progress.setQuizScore(id, { correct, total: data.length });
            el.querySelector(".score").textContent =
              `Ergebnis: ${correct} / ${data.length}` + (correct === data.length ? " – perfekt! 🎉" : " – lies die Erklärungen und versuch's später nochmal.");
            const again = document.createElement("button");
            again.className = "btn secondary";
            again.textContent = "Quiz neu starten";
            again.addEventListener("click", () => { el.innerHTML = ""; el.appendChild(scriptTag(data)); mountQuiz(el); });
            el.appendChild(again);
          }
        });
        q.appendChild(b);
      });
      q.appendChild(explain);
      el.appendChild(q);
    });
    renderMath(el);
  }
  function scriptTag(data) {
    const s = document.createElement("script");
    s.type = "application/json";
    s.textContent = JSON.stringify(data);
    return s;
  }

  // ---------- Formeln ----------
  function renderMath(el) {
    if (window.renderMathInElement) {
      renderMathInElement(el, {
        delimiters: [
          { left: "\\[", right: "\\]", display: true },
          { left: "\\(", right: "\\)", display: false }
        ],
        throwOnError: false
      });
    }
  }

  // ---------- Plot-Helfer für Canvas-Animationen ----------
  // Ein Plot bildet Weltkoordinaten (x, y) auf Pixel ab und kümmert sich um Retina-Auflösung,
  // Größenänderung und Theme-Wechsel.
  class Plot {
    constructor(container, opts) {
      this.opts = Object.assign({ height: 340, xmin: -5, xmax: 5, ymin: -5, ymax: 5, pad: 36, equal: false }, opts);
      this.canvas = document.createElement("canvas");
      container.appendChild(this.canvas);
      this.ctx = this.canvas.getContext("2d");
      this.onDraw = null;
      this.resize = this.resize.bind(this);
      new ResizeObserver(this.resize).observe(container);
      document.addEventListener("themechange", () => this.draw());
      this.resize();
    }
    resize() {
      const dpr = window.devicePixelRatio || 1;
      const w = this.canvas.parentElement.clientWidth;
      const h = this.opts.height;
      this.W = w; this.H = h;
      this.canvas.width = w * dpr; this.canvas.height = h * dpr;
      this.canvas.style.height = h + "px";
      this.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      this.draw();
    }
    setRange(xmin, xmax, ymin, ymax) { Object.assign(this.opts, { xmin, xmax, ymin, ymax }); }
    get color() {
      return {
        bg: cssVar("--surface"), grid: cssVar("--grid"), axis: cssVar("--muted"), text: cssVar("--text"),
        text2: cssVar("--text-2"), s1: cssVar("--series-1"), s2: cssVar("--series-2"), s3: cssVar("--series-3"),
        good: cssVar("--good"), bad: cssVar("--bad"), accent: cssVar("--accent")
      };
    }
    // Weltkoordinaten -> Pixel
    sx(x) { const o = this.opts; return o.pad + (x - o.xmin) / (o.xmax - o.xmin) * (this.W - 2 * o.pad); }
    sy(y) { const o = this.opts; return this.H - o.pad + -(y - o.ymin) / (o.ymax - o.ymin) * (this.H - 2 * o.pad); }
    // Pixel -> Weltkoordinaten
    wx(px) { const o = this.opts; return o.xmin + (px - o.pad) / (this.W - 2 * o.pad) * (o.xmax - o.xmin); }
    wy(py) { const o = this.opts; return o.ymin + (this.H - o.pad - py) / (this.H - 2 * o.pad) * (o.ymax - o.ymin); }
    draw() { if (this.W && this.onDraw) { this.clear(); this.onDraw(this.ctx, this.color); } }
    clear() { this.ctx.fillStyle = this.color.bg; this.ctx.fillRect(0, 0, this.W, this.H); }
    niceStep(range) {
      const raw = range / 8, p = Math.pow(10, Math.floor(Math.log10(raw)));
      const n = raw / p;
      return (n < 1.5 ? 1 : n < 3.5 ? 2 : n < 7.5 ? 5 : 10) * p;
    }
    grid(labels = true) {
      const c = this.ctx, o = this.opts, col = this.color;
      c.lineWidth = 1; c.font = "11px " + cssVar("--mono"); c.fillStyle = col.axis;
      const sxStep = this.niceStep(o.xmax - o.xmin), syStep = this.niceStep(o.ymax - o.ymin);
      c.strokeStyle = col.grid;
      for (let x = Math.ceil(o.xmin / sxStep) * sxStep; x <= o.xmax + 1e-9; x += sxStep) {
        c.beginPath(); c.moveTo(this.sx(x), this.sy(o.ymin)); c.lineTo(this.sx(x), this.sy(o.ymax)); c.stroke();
        if (labels) { c.textAlign = "center"; c.fillText(+x.toFixed(3), this.sx(x), this.sy(o.ymin) + 15); }
      }
      for (let y = Math.ceil(o.ymin / syStep) * syStep; y <= o.ymax + 1e-9; y += syStep) {
        c.beginPath(); c.moveTo(this.sx(o.xmin), this.sy(y)); c.lineTo(this.sx(o.xmax), this.sy(y)); c.stroke();
        if (labels) { c.textAlign = "right"; c.fillText(+y.toFixed(3), this.sx(o.xmin) - 5, this.sy(y) + 4); }
      }
      c.strokeStyle = col.axis;
      if (o.ymin < 0 && o.ymax > 0) { c.beginPath(); c.moveTo(this.sx(o.xmin), this.sy(0)); c.lineTo(this.sx(o.xmax), this.sy(0)); c.stroke(); }
      if (o.xmin < 0 && o.xmax > 0) { c.beginPath(); c.moveTo(this.sx(0), this.sy(o.ymin)); c.lineTo(this.sx(0), this.sy(o.ymax)); c.stroke(); }
    }
    fn(f, color, width = 2, x0 = this.opts.xmin, x1 = this.opts.xmax) {
      const c = this.ctx; c.strokeStyle = color; c.lineWidth = width; c.beginPath();
      const n = Math.max(200, this.W);
      let started = false;
      for (let i = 0; i <= n; i++) {
        const x = x0 + (x1 - x0) * i / n, y = f(x);
        if (!isFinite(y)) { started = false; continue; }
        const py = this.sy(y);
        if (py < -2000 || py > this.H + 2000) { started = false; continue; }
        if (!started) { c.moveTo(this.sx(x), py); started = true; } else c.lineTo(this.sx(x), py);
      }
      c.stroke();
    }
    line(x0, y0, x1, y1, color, width = 2, dash) {
      const c = this.ctx; c.strokeStyle = color; c.lineWidth = width; c.setLineDash(dash || []);
      c.beginPath(); c.moveTo(this.sx(x0), this.sy(y0)); c.lineTo(this.sx(x1), this.sy(y1)); c.stroke(); c.setLineDash([]);
    }
    dot(x, y, color, r = 5, ring = true) {
      const c = this.ctx; c.beginPath(); c.arc(this.sx(x), this.sy(y), r, 0, 2 * Math.PI);
      c.fillStyle = color; c.fill();
      if (ring) { c.lineWidth = 2; c.strokeStyle = this.color.bg; c.stroke(); }
    }
    arrow(x0, y0, x1, y1, color, width = 2.5) {
      const c = this.ctx, X0 = this.sx(x0), Y0 = this.sy(y0), X1 = this.sx(x1), Y1 = this.sy(y1);
      const a = Math.atan2(Y1 - Y0, X1 - X0), L = Math.hypot(X1 - X0, Y1 - Y0), h = Math.min(11, L * .4);
      c.strokeStyle = color; c.fillStyle = color; c.lineWidth = width;
      c.beginPath(); c.moveTo(X0, Y0); c.lineTo(X1 - h * .7 * Math.cos(a), Y1 - h * .7 * Math.sin(a)); c.stroke();
      c.beginPath(); c.moveTo(X1, Y1);
      c.lineTo(X1 - h * Math.cos(a - .4), Y1 - h * Math.sin(a - .4));
      c.lineTo(X1 - h * Math.cos(a + .4), Y1 - h * Math.sin(a + .4)); c.closePath(); c.fill();
    }
    text(str, x, y, color, align = "left", size = 13, dx = 0, dy = 0) {
      const c = this.ctx; c.fillStyle = color || this.color.text; c.font = `${size}px ${cssVar("--font")}`;
      c.textAlign = align; c.fillText(str, this.sx(x) + dx, this.sy(y) + dy);
    }
    // Höhenlinien-Bild einer Funktion f(x, y): Bänder in einer Farbe (kräftiger = höher)
    // plus echte Höhenlinien per Marching Squares. levels: aufsteigende Grenzwerte.
    contour(f, levels, color, cell = 5) {
      const c = this.ctx, nx = Math.ceil(this.W / cell), ny = Math.ceil(this.H / cell);
      const V = new Float64Array((nx + 1) * (ny + 1));
      const at = (i, j) => V[i * (ny + 1) + j];
      for (let i = 0; i <= nx; i++) for (let j = 0; j <= ny; j++) V[i * (ny + 1) + j] = f(this.wx(i * cell), this.wy(j * cell));
      // Flächen
      c.fillStyle = color;
      for (let i = 0; i < nx; i++) for (let j = 0; j < ny; j++) {
        const v = (at(i, j) + at(i + 1, j) + at(i, j + 1) + at(i + 1, j + 1)) / 4;
        let b = 0; while (b < levels.length && v > levels[b]) b++;
        c.globalAlpha = 0.03 + 0.3 * b / levels.length;
        c.fillRect(i * cell, j * cell, cell, cell);
      }
      // Linien
      c.globalAlpha = 0.6; c.strokeStyle = color; c.lineWidth = 1; c.beginPath();
      const lerp = (a, b, L) => (L - a) / (b - a);
      for (const L of levels) {
        for (let i = 0; i < nx; i++) for (let j = 0; j < ny; j++) {
          const a = at(i, j), b = at(i + 1, j), d = at(i, j + 1), e = at(i + 1, j + 1);
          const pts = [];
          if ((a > L) !== (b > L)) pts.push([(i + lerp(a, b, L)) * cell, j * cell]);
          if ((b > L) !== (e > L)) pts.push([(i + 1) * cell, (j + lerp(b, e, L)) * cell]);
          if ((d > L) !== (e > L)) pts.push([(i + lerp(d, e, L)) * cell, (j + 1) * cell]);
          if ((a > L) !== (d > L)) pts.push([i * cell, (j + lerp(a, d, L)) * cell]);
          for (let k = 0; k + 1 < pts.length; k += 2) { c.moveTo(pts[k][0], pts[k][1]); c.lineTo(pts[k + 1][0], pts[k + 1][1]); }
        }
      }
      c.stroke(); c.globalAlpha = 1;
    }
    // Ziehen von Punkten mit Maus/Touch: getPoints() liefert [{x,y}], onMove(i, x, y)
    draggable(getPoints, onMove, radius = 14) {
      let active = -1;
      const pos = e => { const r = this.canvas.getBoundingClientRect(); return [e.clientX - r.left, e.clientY - r.top]; };
      this.canvas.addEventListener("pointerdown", e => {
        const [px, py] = pos(e);
        getPoints().forEach((p, i) => { if (Math.hypot(this.sx(p.x) - px, this.sy(p.y) - py) < radius) active = i; });
        if (active >= 0) this.canvas.setPointerCapture(e.pointerId);
      });
      this.canvas.addEventListener("pointermove", e => {
        const [px, py] = pos(e);
        if (active >= 0) { onMove(active, this.wx(px), this.wy(py)); this.draw(); return; }
        const hover = getPoints().some(p => Math.hypot(this.sx(p.x) - px, this.sy(p.y) - py) < radius);
        this.canvas.style.cursor = hover ? "grab" : "default";
      });
      const end = () => (active = -1);
      this.canvas.addEventListener("pointerup", end);
      this.canvas.addEventListener("pointercancel", end);
    }
  }

  // Baukasten für die Steuerleiste unter einer Animation
  const UI = {
    head(el, title, sub) {
      const h = document.createElement("div"); h.className = "anim-head";
      h.innerHTML = `<strong>${title}</strong>${sub ? `<span>${sub}</span>` : ""}`;
      el.appendChild(h); return h;
    },
    controls(el) { const c = document.createElement("div"); c.className = "anim-controls"; el.appendChild(c); return c; },
    slider(ctrl, label, min, max, step, value, onInput, fmt = v => v) {
      const l = document.createElement("label");
      l.innerHTML = `${label} <input type="range" min="${min}" max="${max}" step="${step}" value="${value}"> <span class="val">${fmt(value)}</span>`;
      const inp = l.querySelector("input"), out = l.querySelector(".val");
      inp.addEventListener("input", () => { out.textContent = fmt(+inp.value); onInput(+inp.value); });
      ctrl.appendChild(l);
      return { set(v) { inp.value = v; out.textContent = fmt(v); }, get value() { return +inp.value; } };
    },
    button(ctrl, label, onClick, secondary) {
      const b = document.createElement("button"); b.className = "btn" + (secondary ? " secondary" : "");
      b.textContent = label; b.addEventListener("click", onClick); ctrl.appendChild(b); return b;
    },
    readout(el) { const r = document.createElement("div"); r.className = "anim-readout"; el.appendChild(r); return r; },
    legend(el, items) {
      const l = document.createElement("div"); l.className = "legend";
      l.innerHTML = items.map(([color, label]) => `<span><i style="background:var(${color})"></i>${label}</span>`).join("");
      el.appendChild(l); return l;
    }
  };

  // Schritt-für-Schritt-Erklärer: steps = [{text, draw(plot, ctx, col)}]
  function stepper(el, plot, steps) {
    el.classList.add("stepper");
    let i = 0;
    const text = document.createElement("div"); text.className = "step-text";
    const ctrl = UI.controls(el);
    const back = UI.button(ctrl, "← Zurück", () => go(i - 1), true);
    const fwd = UI.button(ctrl, "Weiter →", () => go(i + 1));
    const dots = document.createElement("div"); dots.className = "step-dots";
    dots.innerHTML = steps.map(() => "<i></i>").join("");
    ctrl.appendChild(dots);
    el.insertBefore(text, ctrl);
    function go(n) {
      i = Math.max(0, Math.min(steps.length - 1, n));
      text.innerHTML = `<b>Schritt ${i + 1}/${steps.length}:</b> ${steps[i].text}`;
      renderMath(text);
      back.disabled = i === 0; fwd.disabled = i === steps.length - 1;
      dots.querySelectorAll("i").forEach((d, k) => d.classList.toggle("on", k <= i));
      plot.onDraw = (c, col) => steps[i].draw(plot, c, col);
      plot.draw();
    }
    go(0);
  }

  window.ML = { Plot, UI, stepper, cssVar, renderMath, Progress, Store };
  window.ANIMS = window.ANIMS || {};

  // ---------- Start ----------
  document.addEventListener("DOMContentLoaded", () => {
    const root = document.body.dataset.root || "";
    const lessonId = document.body.dataset.lesson;
    const main = document.querySelector("main");

    if (lessonId) {
      const current = findLesson(lessonId);
      buildTopbar(root);
      const layout = document.createElement("div"); layout.className = "layout";
      const side = buildSidebar(current, root);
      main.parentNode.insertBefore(layout, main);
      layout.appendChild(side); layout.appendChild(main);
      main.classList.add("content");
      if (current) {
        main.insertAdjacentHTML("afterbegin",
          `<div class="breadcrumb">Modul ${current.module.nr} · ${current.module.title} — ${current.lesson.project ? "Projekt" : "Lektion " + (current.index + 1)} · ca. ${current.lesson.minutes} Min.</div>`);
        main.appendChild(buildLessonFooter(current, root));
      }
      document.getElementById("nav-toggle").addEventListener("click", () => side.classList.toggle("open"));
      refreshSidebar();
    }

    document.querySelectorAll("[data-quiz]").forEach(mountQuiz);
    document.querySelectorAll("[data-anim]").forEach(el => {
      const fn = window.ANIMS[el.dataset.anim];
      el.classList.add("anim");
      if (fn) fn(el); else el.textContent = "Animation nicht gefunden: " + el.dataset.anim;
    });
    renderMath(document.body);
    document.dispatchEvent(new CustomEvent("mlkurs:ready"));
  });
})();
