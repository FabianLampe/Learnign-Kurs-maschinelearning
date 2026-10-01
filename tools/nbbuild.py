"""Hilfsfunktionen, um Übungs- und Lösungsnotebooks aus derselben Quelle zu erzeugen.

In Code-Zellen markiert man Aufgaben so:

    # >>> Berechne den Mittelwert
    #! mittelwert = ...  # dein Code
    mittelwert = x.sum() / len(x)
    # <<<

- Übungsversion: "# TODO: Berechne den Mittelwert" + alle Zeilen mit "#!" (ohne Präfix)
- Lösungsversion: "# Berechne den Mittelwert" + alle Zeilen ohne "#!"
"""
import re
from pathlib import Path

import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook

BLOCK = re.compile(r"^(\s*)# >>> ?(.*)$")


def _render(code: str, solution: bool) -> str:
    out, in_block, indent = [], False, ""
    for line in code.strip("\n").split("\n"):
        m = BLOCK.match(line)
        if m and not in_block:
            in_block, indent = True, m.group(1)
            out.append(f"{indent}# {'' if solution else 'TODO: '}{m.group(2)}")
            continue
        if in_block and line.strip() == "# <<<":
            in_block = False
            continue
        if in_block:
            stripped = line.lstrip()
            if stripped.startswith("#!"):
                if not solution:
                    pad = line[: len(line) - len(stripped)]
                    out.append(pad + (stripped[3:] if stripped.startswith("#! ") else stripped[2:]))
            elif solution:
                out.append(line)
            continue
        out.append(line)
    return "\n".join(out)


def md(text):
    return ("md", text)


def code(text):
    return ("code", text)


def build(cells, title, exercise_path: Path, solution_path: Path):
    for solution, path in [(False, exercise_path), (True, solution_path)]:
        nb = new_notebook()
        nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
        nb.metadata["language_info"] = {"name": "python"}
        head = f"# {title}" + (" — Lösung" if solution else "")
        nb.cells.append(new_markdown_cell(head))
        for kind, text in cells:
            text = text.strip("\n")
            if kind == "md":
                nb.cells.append(new_markdown_cell(text))
            else:
                nb.cells.append(new_code_cell(_render(text, solution)))
        path.parent.mkdir(parents=True, exist_ok=True)
        nbformat.write(nb, str(path))
