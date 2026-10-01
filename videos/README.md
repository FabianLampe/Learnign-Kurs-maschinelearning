# Erklärvideos (Manim)

Die Videos sind mit [Manim Community Edition](https://www.manim.community/) programmiert. Die fertigen MP4-Dateien liegen bereits in
`website/assets/videos/` – du musst nichts rendern, um den Kurs zu nutzen.

## Erzählstimme

Jede Szene ist in Sprechblöcke gegliedert (`with self.sprich("…")`, siehe `sprecher.py`). Der Text wird vertont, und die
Animationen des Blocks passen sich an die Länge des gesprochenen Satzes an. Die Audiodateien landen in `videos/audio/`
und werden beim nächsten Rendern wiederverwendet.

| `STIMME_ENGINE` | Klang | Kosten | Standardstimme |
|---|---|---|---|
| `edge` (Standard) | natürliche Microsoft-Neuralstimme | kostenlos, kein Key | `de-DE-SeraphinaMultilingualNeural` (weiblich), Alternative: `de-DE-FlorianMultilingualNeural` (männlich) |
| `openai` | ChatGPT-Stimme mit Regieanweisung „freundliche Tutorin“ | wenige Cent pro Video, `OPENAI_API_KEY` nötig | `marin`, Alternativen: `cedar`, `coral`, `nova` … |
| `espeak` | Roboterstimme, nur zum Testen | kostenlos, offline | – |
| `stumm` | ohne Ton, Dauer geschätzt | – | – |

### Ohne Installation: GitHub Actions

Unter **Actions → „Erklärvideos mit Stimme rendern“ → Run workflow** wählst du Stimme und Auflösung. Der Workflow rendert alle Videos
und committet sie zurück ins Repo. Er startet außerdem automatisch, wenn sich Szenen oder Sprechertexte ändern.
Für die ChatGPT-Stimme legst du vorher unter **Settings → Secrets and variables → Actions** ein Secret `OPENAI_API_KEY` an.

### Lokal

Manim braucht Systembibliotheken (Cairo, Pango, ffmpeg): <https://docs.manim.community/en/stable/installation.html>

```bash
pip install manim edge-tts openai
python tools/render_videos.py                                   # alle Videos, kostenlose Stimme
STIMME=de-DE-FlorianMultilingualNeural python tools/render_videos.py
STIMME_ENGINE=openai OPENAI_API_KEY=sk-... python tools/render_videos.py --qualitaet h
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

`tools/render_videos.py` kopiert die fertigen Videos mit den Namen aus der Tabelle nach `website/assets/videos/`.
