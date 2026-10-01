"""Erzählstimme für Manim-Szenen.

Benutzung in einer Szene (Klasse erbt von SprecherSzene statt Scene):

    with self.sprich("Stell dir vor, du stehst im Nebel auf einem Berg.") as t:
        self.play(Create(berg), run_time=t.dauer * 0.6)
        self.play(FadeIn(wanderer))
    # Nach dem Block wird gewartet, bis der Satz zu Ende gesprochen ist.

Die Audiodateien werden einmal erzeugt und in videos/audio/<stimme>/ zwischengespeichert.
Gesteuert über Umgebungsvariablen:

    STIMME_ENGINE = edge (Standard, kostenlos) | openai (ChatGPT-Stimmen, API-Key nötig) | espeak (nur Test) | stumm
    STIMME        = Stimmenname, Standard: de-DE-SeraphinaMultilingualNeural (edge) bzw. marin (openai)
    OPENAI_API_KEY für openai
"""
import asyncio
import hashlib
import os
import subprocess
from contextlib import contextmanager
from pathlib import Path

from manim import Scene

AUDIO_DIR = Path(__file__).resolve().parent / "audio"

ENGINE = os.environ.get("STIMME_ENGINE", "edge")
STANDARD_STIMME = {"edge": "de-DE-SeraphinaMultilingualNeural", "openai": "marin", "espeak": "de", "stumm": "-"}
STIMME = os.environ.get("STIMME") or STANDARD_STIMME.get(ENGINE, "")

# Wie die Stimme klingen soll (nur openai versteht Regieanweisungen)
OPENAI_ANWEISUNG = (
    "Du bist eine freundliche, geduldige Tutorin, die einer einzelnen Person Machine Learning erklärt. "
    "Sprich natürlich und im Gesprächston, wie im Sprachmodus von ChatGPT: warm, neugierig, mit kleinen Pausen vor "
    "wichtigen Gedanken und leichter Betonung der Schlüsselbegriffe. Nicht vorlesen, sondern erklären. Hochdeutsch."
)


def _dauer(pfad: Path) -> float:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(pfad)],
                         capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def _erzeuge(text: str, ziel: Path):
    ziel.parent.mkdir(parents=True, exist_ok=True)
    tmp = ziel.with_suffix(".tmp" + ziel.suffix)
    if ENGINE == "edge":
        import edge_tts
        # leicht langsamer als Standard: Erklären statt Vorlesen
        asyncio.run(edge_tts.Communicate(text, STIMME, rate="-6%").save(str(tmp)))
    elif ENGINE == "openai":
        from openai import OpenAI
        with OpenAI().audio.speech.with_streaming_response.create(
            model=os.environ.get("OPENAI_TTS_MODEL", "gpt-4o-mini-tts"), voice=STIMME, input=text,
            instructions=OPENAI_ANWEISUNG, response_format="mp3",
        ) as resp:
            resp.stream_to_file(tmp)
    elif ENGINE == "espeak":
        wav = tmp.with_suffix(".wav")
        subprocess.run(["espeak-ng", "-v", STIMME, "-s", "150", "-w", str(wav), text], check=True)
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(wav), str(tmp)], check=True)
        wav.unlink()
    else:
        raise ValueError(f"Unbekannte STIMME_ENGINE: {ENGINE}")
    tmp.rename(ziel)


class _Takt:
    def __init__(self, dauer):
        self.dauer = dauer


class SprecherSzene(Scene):
    @contextmanager
    def sprich(self, text: str, min_dauer: float = 0.0):
        text = " ".join(text.split())
        if ENGINE == "stumm":
            dauer = max(min_dauer, len(text) / 15)  # grobe Schätzung ≈ 15 Zeichen pro Sekunde
        else:
            key = hashlib.sha1(f"{ENGINE}|{STIMME}|{text}".encode()).hexdigest()[:16]
            pfad = AUDIO_DIR / f"{ENGINE}-{STIMME}" / f"{key}.mp3"
            if not pfad.exists():
                _erzeuge(text, pfad)
            dauer = max(min_dauer, _dauer(pfad))
            self.add_sound(str(pfad))
        start = self.renderer.time
        yield _Takt(dauer)
        rest = dauer - (self.renderer.time - start)
        if rest > 0.05:
            self.wait(rest + 0.25)  # kurze Atempause nach jedem Satz
        else:
            self.wait(0.25)
