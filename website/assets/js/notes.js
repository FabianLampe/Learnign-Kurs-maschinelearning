// Notiz-Seitenleiste: ein Notizbuch für den ganzen Kurs, gespeichert im Browser.
// Zeilen wie "1. Titel", "2. Titel" oder "1.1 Titel" werden automatisch zum Inhaltsverzeichnis.
(function () {
  "use strict";
  const { Store } = ML;
  // "1. Text", "2) Text", "1.2 Text", "1.2.3. Text" → Nummer + Titel.
  // Eine einzelne Zahl braucht Punkt oder Klammer, damit "2024 war …" keine Überschrift wird.
  const HEADING = /^\s*(\d+(?:\.\d+)+\.?|\d+[.)])\s+(\S.*)$/;

  function parseToc(text) {
    const toc = [];
    let offset = 0;
    for (const line of text.split("\n")) {
      const m = line.match(HEADING);
      if (m) {
        const nr = m[1].replace(/[.)]$/, "");
        toc.push({ nr, title: m[2].trim(), level: nr.split(".").length, offset });
      }
      offset += line.length + 1;
    }
    return toc;
  }

  function escapeHtml(s) {
    return s.replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  }

  // Pixelposition einer Textstelle im Textfeld messen (berücksichtigt Zeilenumbrüche).
  function caretTop(ta, pos) {
    const mirror = document.createElement("div");
    const cs = getComputedStyle(ta);
    ["fontFamily", "fontSize", "lineHeight", "letterSpacing", "paddingTop", "paddingLeft", "paddingRight", "borderLeftWidth", "borderRightWidth", "boxSizing", "tabSize"]
      .forEach(p => (mirror.style[p] = cs[p]));
    Object.assign(mirror.style, { position: "absolute", visibility: "hidden", whiteSpace: "pre-wrap", overflowWrap: "break-word", width: ta.clientWidth + "px" });
    mirror.textContent = ta.value.slice(0, pos);
    const marker = document.createElement("span"); marker.textContent = "​";
    mirror.appendChild(marker);
    document.body.appendChild(mirror);
    const top = marker.offsetTop;
    mirror.remove();
    return top;
  }

  function build() {
    const bar = document.querySelector(".topbar");
    if (!bar) return;

    const btn = document.createElement("button");
    btn.className = "icon-btn"; btn.id = "notes-toggle";
    btn.textContent = "📝 Notizen";
    btn.setAttribute("aria-label", "Notizen öffnen");
    bar.insertBefore(btn, bar.querySelector("#theme-toggle, #theme-btn"));

    const panel = document.createElement("aside");
    panel.className = "notes-panel"; panel.setAttribute("aria-label", "Notizen");
    panel.innerHTML = `
      <div class="notes-head">
        <strong>Meine Notizen</strong>
        <span class="notes-status" aria-live="polite"></span>
        <button class="icon-btn notes-close" aria-label="Notizen schließen">✕</button>
      </div>
      <details class="notes-toc" open>
        <summary>Inhaltsverzeichnis</summary>
        <ol></ol>
      </details>
      <textarea spellcheck="true" placeholder="Schreib hier deine Notizen …

Nummerierte Zeilen werden zum Inhaltsverzeichnis:
1. Gradientenabstieg
1.1 Lernrate
2. Statistik"></textarea>
      <div class="notes-actions">
        <button class="btn secondary" data-act="lesson" title="Aktuelle Lektion als nächste Überschrift einfügen">+ Lektion als Überschrift</button>
        <button class="btn secondary" data-act="export" title="Als Markdown-Datei herunterladen">⬇ Exportieren</button>
        <label class="btn secondary" title="Notizen aus einer Datei laden">⬆ Importieren<input type="file" accept=".md,.txt" hidden></label>
      </div>`;
    document.body.appendChild(panel);

    const ta = panel.querySelector("textarea");
    const tocList = panel.querySelector(".notes-toc ol");
    const tocBox = panel.querySelector(".notes-toc");
    const status = panel.querySelector(".notes-status");
    ta.value = Store.get("notes", "");

    function renderToc() {
      const toc = parseToc(ta.value);
      tocBox.hidden = toc.length === 0;
      tocList.innerHTML = toc.map((h, i) =>
        `<li style="--lvl:${h.level - 1}"><a href="#" data-i="${i}"><span class="nr">${escapeHtml(h.nr)}${h.level === 1 ? "." : ""}</span> ${escapeHtml(h.title)}</a></li>`).join("");
      tocList.querySelectorAll("a").forEach(a => a.addEventListener("click", e => {
        e.preventDefault();
        const h = toc[+a.dataset.i];
        ta.focus();
        ta.setSelectionRange(h.offset, h.offset);
        ta.scrollTop = Math.max(0, caretTop(ta, h.offset) - 8);
      }));
    }

    let timer = null;
    function save() {
      Store.set("notes", ta.value);
      status.textContent = "gespeichert ✓";
      clearTimeout(timer); timer = setTimeout(() => (status.textContent = ""), 1500);
    }
    let saveTimer = null;
    ta.addEventListener("input", () => {
      renderToc();
      status.textContent = "…";
      clearTimeout(saveTimer); saveTimer = setTimeout(save, 400);
    });

    // Nächste freie Hauptnummer für "Lektion als Überschrift"
    function nextNumber() {
      const tops = parseToc(ta.value).filter(h => h.level === 1).map(h => parseInt(h.nr, 10));
      return tops.length ? Math.max(...tops) + 1 : 1;
    }
    panel.querySelector('[data-act="lesson"]').addEventListener("click", () => {
      const h1 = document.querySelector("main h1, .hero h1");
      const title = h1 ? h1.textContent.trim() : document.title;
      const sep = ta.value && !ta.value.endsWith("\n") ? "\n\n" : ta.value ? "\n" : "";
      ta.value += `${sep}${nextNumber()}. ${title}\n`;
      ta.focus(); ta.setSelectionRange(ta.value.length, ta.value.length); ta.scrollTop = ta.scrollHeight;
      renderToc(); save();
    });
    panel.querySelector('[data-act="export"]').addEventListener("click", () => {
      const blob = new Blob([ta.value], { type: "text/markdown;charset=utf-8" });
      const a = document.createElement("a");
      a.href = URL.createObjectURL(blob);
      a.download = "ml-kurs-notizen.md";
      a.click();
      setTimeout(() => URL.revokeObjectURL(a.href), 1000);
    });
    panel.querySelector('input[type="file"]').addEventListener("change", async e => {
      const file = e.target.files[0];
      if (!file) return;
      const text = await file.text();
      if (!ta.value.trim() || confirm("Vorhandene Notizen durch die Datei ersetzen? (Abbrechen = anhängen)")) ta.value = text;
      else ta.value += "\n" + text;
      e.target.value = "";
      renderToc(); save();
    });

    function setOpen(open) {
      document.body.classList.toggle("notes-open", open);
      btn.setAttribute("aria-expanded", open);
      Store.set("notesOpen", open);
      if (open) ta.focus({ preventScroll: true });
    }
    btn.addEventListener("click", () => setOpen(!document.body.classList.contains("notes-open")));
    panel.querySelector(".notes-close").addEventListener("click", () => setOpen(false));
    // Strg/Cmd + Shift + N öffnet/schließt die Notizen
    document.addEventListener("keydown", e => {
      if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key.toLowerCase() === "n") { e.preventDefault(); btn.click(); }
    });
    // Änderungen aus einem anderen Tab übernehmen
    window.addEventListener("storage", () => {
      const v = Store.get("notes", "");
      if (v !== ta.value && document.activeElement !== ta) { ta.value = v; renderToc(); }
    });

    renderToc();
    if (Store.get("notesOpen", false)) document.body.classList.add("notes-open");
  }

  if (document.readyState === "loading") document.addEventListener("mlkurs:ready", build);
  else build();
})();
