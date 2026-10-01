"""Exportiert die Lektionstexte eines Moduls als Markdown-Quelle für NotebookLM.

    python tools/export_quellen.py
Benötigt: beautifulsoup4
"""
import re
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString

ROOT = Path(__file__).resolve().parent.parent
MODULE = {"modul-01": "Modul 1 – Grundlagen & Mathe"}


def inline(el):
    """Text eines Elements; Formeln \\( \\) bleiben als lesbarer LaTeX-Quelltext erhalten."""
    out = []
    for c in el.children:
        if isinstance(c, NavigableString):
            out.append(str(c))
        elif c.name in ("b", "strong"):
            out.append(f"**{inline(c).strip()}**")
        elif c.name == "code":
            out.append(f"`{c.get_text()}`")
        elif c.name == "br":
            out.append("\n")
        else:
            out.append(inline(c))
    return re.sub(r"[ \t]+", " ", "".join(out))


def convert(html):
    soup = BeautifulSoup(html, "html.parser")
    main = soup.find("main")
    # Interaktive Teile haben in einer Textquelle keinen Sinn
    for sel in ["[data-anim]", "[data-quiz]", "figure", ".notebook-link"]:
        for el in main.select(sel):
            el.decompose()
    lines = []
    for el in main.find_all(["h1", "h2", "h3", "p", "ul", "ol", "table", "pre", "div"], recursive=True):
        if el.find_parent(["ul", "ol", "table", "pre", "p"]):
            continue
        if el.name == "div" and "callout" not in el.get("class", []) and "goals" not in el.get("class", []):
            continue
        if el.name == "div":
            label = el.find(class_="label")
            if label:
                lines.append(f"> **{label.get_text().strip()}**")
                label.decompose()
            h3 = el.find("h3")
            if h3:
                lines.append(f"### {h3.get_text().strip()}")
                h3.decompose()
            text = el.get_text(" ", strip=True)
            lines.append("> " + re.sub(r"\s+", " ", text))
            # Kinder nicht doppelt ausgeben
            for c in el.find_all(["p", "ul", "ol"]):
                c.decompose()
        elif el.name in ("h1", "h2", "h3"):
            lines.append("#" * (int(el.name[1]) + 1) + " " + el.get_text().strip())
        elif el.name == "p":
            lines.append(inline(el).strip())
        elif el.name in ("ul", "ol"):
            for i, li in enumerate(el.find_all("li", recursive=False), 1):
                lines.append(f"{i}. " if el.name == "ol" else "- " + inline(li).strip() if el.name == "ul" else "")
                if el.name == "ol":
                    lines[-1] += inline(li).strip()
        elif el.name == "table":
            rows = [[re.sub(r"\s+", " ", inline(c)).strip() for c in tr.find_all(["th", "td"])] for tr in el.find_all("tr")]
            if rows:
                lines.append("| " + " | ".join(rows[0]) + " |")
                lines.append("|" + "---|" * len(rows[0]))
                lines += ["| " + " | ".join(r) + " |" for r in rows[1:]]
        elif el.name == "pre":
            lines.append("```python\n" + el.get_text().rstrip() + "\n```")
        lines.append("")
    # freistehende Formelblöcke \[ … \] stehen direkt in <main>
    return "\n".join(lines)


def main():
    for modul, titel in MODULE.items():
        teile = [f"# {titel}\n\nKursmaterial aus „Machine Learning – von vorne bis hinten“.\n"]
        for f in sorted((ROOT / "website" / modul).glob("*.html")):
            html = f.read_text(encoding="utf-8")
            # Display-Formeln, die nicht in einem Absatz stehen, als eigenen Absatz retten
            html = re.sub(r"\n\s*(\\\[.*?\\\])\s*\n", r"\n<p>\1</p>\n", html, flags=re.S)
            teile.append(convert(html))
        out = ROOT / "notebooklm" / "quellen" / f"{modul}.md"
        text = re.sub(r"\n{3,}", "\n\n", "\n".join(teile))
        out.write_text(text, encoding="utf-8")
        print(out.relative_to(ROOT), len(text), "Zeichen")


if __name__ == "__main__":
    main()
