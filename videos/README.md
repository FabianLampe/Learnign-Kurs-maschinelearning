# Erklärvideos (Manim)

Die Videos sind mit [Manim Community Edition](https://www.manim.community/) programmiert. Die fertigen MP4-Dateien liegen bereits in
`website/assets/videos/` – du musst nichts rendern, um den Kurs zu nutzen.

## Selbst rendern

Manim braucht Systembibliotheken (Cairo, Pango, ffmpeg). Anleitung je Betriebssystem:
<https://docs.manim.community/en/stable/installation.html>

```bash
pip install manim
cd videos/modul-01
manim -qm szenen.py GradientenAbstieg      # 720p, schnelle Vorschau
manim -qh szenen.py GradientenAbstieg      # 1080p
```

Die Szenen nutzen bewusst kein LaTeX, damit keine TeX-Installation nötig ist.

## Modul 1

| Szene | Datei auf der Website | Lektion |
|---|---|---|
| `WasIstML` | `m01_v01_was_ist_ml.mp4` | 1.1 |
| `Skalarprodukt` | `m01_v02_skalarprodukt.mp4` | 1.2 |
| `AbleitungUndGradient` | `m01_v03_ableitung_gradient.mp4` | 1.4 |
| `GradientenAbstieg` | `m01_v04_gradientenabstieg.mp4` | 1.5 |
| `RegressionLernen` | `m01_v05_regression.mp4` | 1.5 |

Nach dem Rendern liegt das Video unter `media/videos/szenen/720p30/<Szene>.mp4` und wird mit dem Namen aus der Tabelle nach
`website/assets/videos/` kopiert.
