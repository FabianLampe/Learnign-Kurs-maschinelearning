"""Erzeugt alle Übungs- und Lösungsnotebooks.

    python tools/build_all.py            # nur erzeugen
    python tools/build_all.py --execute  # Lösungen zusätzlich ausführen (prüft, dass alles läuft, und speichert die Ausgaben)
"""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from nbbuild import build  # noqa: E402
import modul01_notebooks  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
MODULE = {"modul-01": modul01_notebooks.NOTEBOOKS}


def main():
    execute = "--execute" in sys.argv
    for modul, notebooks in MODULE.items():
        base = ROOT / "notebooks" / modul
        for name, title, cells in notebooks:
            ex = base / f"{name}.ipynb"
            sol = base / "loesungen" / f"{name}_loesung.ipynb"
            build(cells, title, ex, sol)
            print("erzeugt:", ex.relative_to(ROOT), "+", sol.relative_to(ROOT))
            if execute:
                subprocess.run([sys.executable, "-m", "jupyter", "nbconvert", "--to", "notebook", "--execute",
                                "--inplace", "--ExecutePreprocessor.timeout=600", str(sol)], check=True)
                print("  ausgeführt ✓")


if __name__ == "__main__":
    main()
