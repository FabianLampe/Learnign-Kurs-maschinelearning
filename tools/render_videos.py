"""Rendert die Erklärvideos mit Erzählstimme und kopiert sie auf die Website.

    python tools/render_videos.py                 # alle Videos, 720p
    python tools/render_videos.py --qualitaet h   # 1080p
    python tools/render_videos.py GradientenAbstieg

Stimme wählen über Umgebungsvariablen (siehe videos/sprecher.py):
    STIMME_ENGINE=edge   STIMME=de-DE-SeraphinaMultilingualNeural   (Standard, kostenlos)
    STIMME_ENGINE=openai STIMME=marin   OPENAI_API_KEY=...          (ChatGPT-Stimme)
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VIDEOS = {
    "modul-01": {
        "WasIstML": "m01_v01_was_ist_ml.mp4",
        "Skalarprodukt": "m01_v02_skalarprodukt.mp4",
        "AbleitungUndGradient": "m01_v03_ableitung_gradient.mp4",
        "GradientenAbstieg": "m01_v04_gradientenabstieg.mp4",
        "RegressionLernen": "m01_v05_regression.mp4",
    },
}
AUFLOESUNG = {"l": "480p15", "m": "720p30", "h": "1080p60"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("szenen", nargs="*", help="nur diese Szenen rendern")
    ap.add_argument("--qualitaet", default="m", choices=AUFLOESUNG)
    args = ap.parse_args()
    media = ROOT / "videos" / "media"
    for modul, szenen in VIDEOS.items():
        quelle = ROOT / "videos" / modul / "szenen.py"
        for szene, ziel in szenen.items():
            if args.szenen and szene not in args.szenen:
                continue
            print(f"▶ {modul}/{szene}", flush=True)
            subprocess.run([sys.executable, "-m", "manim", f"-q{args.qualitaet}", "--disable_caching", "--media_dir", str(media),
                            str(quelle), szene], check=True, cwd=quelle.parent)
            mp4 = media / "videos" / "szenen" / AUFLOESUNG[args.qualitaet] / f"{szene}.mp4"
            shutil.copy(mp4, ROOT / "website" / "assets" / "videos" / ziel)
            print(f"  → website/assets/videos/{ziel}")


if __name__ == "__main__":
    main()
