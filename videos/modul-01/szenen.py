"""Erklärvideos für Modul 1 (Manim Community Edition) mit Erzählstimme.

Rendern: siehe videos/README.md, z. B.
    STIMME_ENGINE=edge manim -qm szenen.py GradientenAbstieg

Jede Szene ist in Sprechblöcke gegliedert (`with self.sprich(...)`). Die Animationen
eines Blocks werden an die Länge des gesprochenen Satzes angepasst.
Die Sprechertexte sind für das Hören geschrieben: Formeln werden ausgesprochen.
Es wird bewusst kein LaTeX verwendet (Text statt MathTex).
"""
import sys
from pathlib import Path

import numpy as np
from manim import *

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sprecher import SprecherSzene  # noqa: E402

# Farben passend zur Kurs-Website (Dark Theme)
BG = "#0f1115"
TXT = "#eceef2"
MUTED = "#7d8494"
S1 = "#3987e5"  # blau
S2 = "#d95926"  # orange
S3 = "#199e70"  # grün
FONT = "DejaVu Sans"

config.background_color = BG


def T(text, size=32, color=TXT, **kw):
    """Text mit Kurs-Schrift."""
    # groß rendern und verkleinern: gibt bei kleinen Größen saubere Buchstabenabstände
    return Text(text, font=FONT, font_size=size * 3, color=color, **kw).scale(1 / 3)


def titel_gruppe(text, sub=None):
    t = T(text, 44, weight=BOLD)
    group = VGroup(t)
    if sub:
        group.add(T(sub, 26, MUTED).next_to(t, DOWN))
    return group


def box(label, color, w=2.6, h=1.1, size=26):
    r = RoundedRectangle(corner_radius=0.15, width=w, height=h, color=color, stroke_width=3)
    return VGroup(r, T(label, size).move_to(r))


# ---------------------------------------------------------------------------
class WasIstML(SprecherSzene):
    """Video 1: Klassisches Programmieren vs. Machine Learning."""

    def construct(self):
        tg = titel_gruppe("Was ist Machine Learning?", "Regeln programmieren vs. Regeln lernen")
        with self.sprich("Was heißt es eigentlich, dass ein Computer lernt? Lass uns das mal ganz in Ruhe auseinandernehmen."):
            self.play(FadeIn(tg, shift=UP * 0.3))
        self.play(FadeOut(tg))

        head = T("Klassisches Programmieren", 30, MUTED).to_edge(UP)
        daten = box("Daten", S1).move_to(LEFT * 4.5 + UP * 0.9)
        regeln = box("Regeln", S2).move_to(LEFT * 4.5 + DOWN * 0.9)
        prog = box("Programm", MUTED, w=3).move_to(ORIGIN)
        antw = box("Antworten", S3).move_to(RIGHT * 4.5)
        arrows = VGroup(
            Arrow(daten.get_right(), prog.get_left(), color=MUTED),
            Arrow(regeln.get_right(), prog.get_left(), color=MUTED),
            Arrow(prog.get_right(), antw.get_left(), color=MUTED),
        )
        with self.sprich("Beim klassischen Programmieren schreibst du die Regeln selbst. "
                         "Das Programm nimmt Daten, wendet deine Regeln an, und heraus kommen Antworten.") as t:
            self.play(FadeIn(head), FadeIn(daten), FadeIn(regeln), run_time=t.dauer * 0.3)
            self.play(GrowArrow(arrows[0]), GrowArrow(arrows[1]), FadeIn(prog), run_time=t.dauer * 0.3)
            self.play(GrowArrow(arrows[2]), FadeIn(antw), run_time=t.dauer * 0.3)

        bsp = T('if "Gewinnspiel" in mail:  spam = True', 24, S2).to_edge(DOWN, buff=0.8)
        with self.sprich("Zum Beispiel ein Spamfilter: Wenn in der Mail das Wort Gewinnspiel steht, dann ist es Spam. "
                         "Das funktioniert super – solange du die Regeln kennst."):
            self.play(Write(bsp))

        frage = T("Aber: Welche Regel erkennt eine Katze auf einem Foto?", 28, TXT).to_edge(DOWN, buff=0.8)
        with self.sprich("Aber jetzt überleg mal: Welche Regel erkennt eine Katze auf einem Foto? "
                         "Pixel für Pixel? Ehrlich gesagt – das kann niemand aufschreiben."):
            self.play(ReplacementTransform(bsp, frage))

        head2 = T("Machine Learning", 30, S1).to_edge(UP)
        labels = box("Antworten", S3).move_to(regeln)
        modell = box("Regeln = Modell", S2, w=3.4).move_to(antw)
        lern = box("Lernalgorithmus", MUTED, w=3.4, size=24).move_to(prog)
        hinweis = T("Daten + Antworten  →  der Computer findet die Regeln selbst", 26).to_edge(DOWN, buff=0.8)
        with self.sprich("Und genau hier dreht Machine Learning den Spieß um. Wir geben dem Computer Daten "
                         "und die richtigen Antworten dazu. Und ein Lernalgorithmus findet die Regeln selbst.") as t:
            self.play(FadeOut(frage), ReplacementTransform(head, head2), run_time=t.dauer * 0.25)
            self.play(ReplacementTransform(antw, labels), ReplacementTransform(regeln, modell),
                      ReplacementTransform(prog, lern), run_time=t.dauer * 0.35)
            self.play(Write(hinweis), run_time=t.dauer * 0.3)
        self.play(*[FadeOut(m) for m in self.mobjects])

        f = T("ŷ = f(x)", 64, S2)
        expl = VGroup(
            T("x  –  Merkmale (Features), z. B. Wohnfläche, Lage", 26),
            T("ŷ  –  Vorhersage (Prediction), z. B. Preis", 26),
            T("f  –  das gelernte Modell", 26),
        ).arrange(DOWN, aligned_edge=LEFT).next_to(f, DOWN, buff=0.8)
        with self.sprich("Das Ergebnis nennen wir ein Modell. Das ist im Grunde einfach eine Funktion: "
                         "y Dach gleich f von x."):
            self.play(Write(f))
        with self.sprich("x sind die Merkmale, auf Englisch Features, zum Beispiel die Wohnfläche und die Lage einer Wohnung."):
            self.play(FadeIn(expl[0], shift=RIGHT * 0.3))
        with self.sprich("y Dach ist die Vorhersage – etwa der Preis. Und f ist das, was gelernt wurde."):
            self.play(FadeIn(expl[1], shift=RIGHT * 0.3))
            self.play(FadeIn(expl[2], shift=RIGHT * 0.3))
        self.play(FadeOut(VGroup(f, expl)))

        ax = Axes(x_range=[0, 10], y_range=[0, 6], x_length=9, y_length=5.2, tips=False,
                  axis_config={"color": MUTED}).shift(DOWN * 0.3)
        rng = np.random.default_rng(3)
        a = [ax.c2p(*p) for p in rng.normal([3, 4], 0.7, (14, 2))]
        b = [ax.c2p(*p) for p in rng.normal([7, 2], 0.7, (14, 2))]
        dots_a = VGroup(*[Dot(p, color=S1, radius=0.09) for p in a])
        dots_b = VGroup(*[Dot(p, color=S2, radius=0.09) for p in b])
        cap = T("Aus Beispielen lernen: Wo verläuft die Grenze?", 28).to_edge(UP)
        with self.sprich("Wie sieht das konkret aus? Hier haben wir Beispiele aus zwei Klassen, blau und orange.") as t:
            self.play(Create(ax), FadeIn(cap), run_time=t.dauer * 0.4)
            self.play(LaggedStart(*[GrowFromCenter(d) for d in [*dots_a, *dots_b]], lag_ratio=0.04), run_time=t.dauer * 0.5)
        line = DashedLine(ax.c2p(1, 0.2), ax.c2p(9.5, 5.8), color=TXT)
        with self.sprich("Das Training sucht eine Grenze, die die beiden Gruppen möglichst gut trennt."):
            self.play(Create(line))
        neu = Dot(ax.c2p(4.2, 3.0), color=YELLOW, radius=0.13)
        q = T("neuer Punkt → Klasse blau", 24, S1).next_to(neu, LEFT)
        with self.sprich("Und kommt jetzt ein neuer Punkt dazu, schaut das Modell einfach, auf welcher Seite er liegt. "
                         "Fertig ist die Vorhersage. Das ist Machine Learning im Kern: aus Beispielen lernen, "
                         "und das Gelernte auf Neues anwenden."):
            self.play(GrowFromCenter(neu), FadeIn(q))


# ---------------------------------------------------------------------------
class Skalarprodukt(SprecherSzene):
    """Video 2: Skalarprodukt als Ähnlichkeit und Projektion."""

    def construct(self):
        tg = titel_gruppe("Das Skalarprodukt", "die wichtigste Rechnung im Machine Learning")
        with self.sprich("Wenn es eine einzige Rechnung gibt, die im Machine Learning wirklich überall auftaucht, "
                         "dann ist es das Skalarprodukt. Schauen wir es uns an."):
            self.play(FadeIn(tg, shift=UP * 0.3))
        self.play(FadeOut(tg))

        plane = NumberPlane(x_range=[-5, 5], y_range=[-3, 3], background_line_style={"stroke_color": "#262a33"},
                            axis_config={"color": MUTED}).shift(LEFT * 1.5)
        o = plane.c2p(0, 0)
        ang = ValueTracker(70 * DEGREES)
        a_vec = np.array([3, 1, 0])

        def b_end():
            return 2.5 * np.array([np.cos(ang.get_value()), np.sin(ang.get_value()), 0])

        va = Arrow(o, plane.c2p(*a_vec[:2]), buff=0, color=S1, stroke_width=6)
        vb = always_redraw(lambda: Arrow(o, plane.c2p(*b_end()[:2]), buff=0, color=S2, stroke_width=6))
        la = T("a", 30, S1).next_to(va.get_end(), RIGHT)
        lb = always_redraw(lambda: T("b", 30, S2).next_to(vb.get_end(), UP))
        with self.sprich("Wir haben zwei Vektoren, a in Blau und b in Orange. Im Machine Learning können das zum Beispiel "
                         "zwei Datenpunkte sein, oder ein Datenpunkt und die Gewichte eines Modells.") as t:
            self.play(Create(plane), run_time=t.dauer * 0.3)
            self.play(GrowArrow(va), FadeIn(la), run_time=t.dauer * 0.25)
            self.play(GrowArrow(vb), FadeIn(lb), run_time=t.dauer * 0.25)

        formel = VGroup(
            T("a · b = a₁b₁ + a₂b₂", 28),
            T("     = ‖a‖ · ‖b‖ · cos θ", 28),
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UR).shift(LEFT * 0.2)
        with self.sprich("Rechnen ist ganz einfach: Du multiplizierst die Einträge paarweise und zählst alles zusammen. "
                         "Spannend wird es aber geometrisch: Das Ergebnis ist die Länge von a, mal die Länge von b, "
                         "mal dem Kosinus des Winkels dazwischen.") as t:
            self.play(Write(formel[0]), run_time=t.dauer * 0.35)
            self.wait(t.dauer * 0.15)
            self.play(Write(formel[1]), run_time=t.dauer * 0.35)

        def proj_pt():
            b = b_end()
            return np.dot(a_vec, b) / np.dot(a_vec, a_vec) * a_vec

        proj = always_redraw(lambda: Line(o, plane.c2p(*proj_pt()[:2]), color=S3, stroke_width=12, stroke_opacity=0.7))
        drop = always_redraw(lambda: DashedLine(plane.c2p(*b_end()[:2]), plane.c2p(*proj_pt()[:2]), color=MUTED))
        wert = always_redraw(lambda: T(f"a · b = {np.dot(a_vec, b_end()):.2f}", 34,
                                       S3 if np.dot(a_vec, b_end()) > 0.05 else (S2 if np.dot(a_vec, b_end()) < -0.05 else TXT))
                             .to_corner(DR).shift(UP * 0.6 + LEFT * 0.3))
        with self.sprich("Die grüne Linie ist der Schatten von b auf a, die sogenannte Projektion. "
                         "Sie zeigt dir, wie viel von b in die Richtung von a zeigt.") as t:
            self.play(Create(drop), Create(proj), run_time=t.dauer * 0.5)
            self.add(wert)

        for target, sprech, txt in [
            (20 * DEGREES, "Zeigen beide ungefähr in dieselbe Richtung, wird das Skalarprodukt groß und positiv.",
             "ähnliche Richtung → großes Skalarprodukt"),
            (np.arctan2(-3, 1) + np.pi, "Stehen sie genau senkrecht aufeinander, ist es null. Die beiden haben sozusagen nichts gemeinsam.",
             "senkrecht → Skalarprodukt = 0"),
            (160 * DEGREES, "Und zeigen sie in entgegengesetzte Richtungen, wird es negativ.",
             "entgegengesetzt → negativ"),
        ]:
            cap = T(txt, 26).to_edge(DOWN, buff=0.3)
            with self.sprich(sprech) as t:
                self.play(ang.animate.set_value(target), FadeIn(cap), run_time=min(2.0, t.dauer * 0.6))
            self.play(FadeOut(cap), run_time=0.4)

        ml = T("Im ML: Modell-Ausgabe  ŷ = w · x + b", 30, S1).to_edge(DOWN, buff=0.3)
        with self.sprich("Das Skalarprodukt ist also ein Maß für Ähnlichkeit. Und genau so rechnet ein lineares Modell: "
                         "y Dach gleich w mal x plus b. Auch jedes Neuron in einem neuronalen Netz macht genau das.") as t:
            self.play(ang.animate.set_value(50 * DEGREES), run_time=t.dauer * 0.3)
            self.play(Write(ml), run_time=t.dauer * 0.3)


# ---------------------------------------------------------------------------
class AbleitungUndGradient(SprecherSzene):
    """Video 3: Von der Sekante zur Ableitung, dann zum Gradienten."""

    def construct(self):
        tg = titel_gruppe("Ableitung & Gradient", "Wie steil ist es hier – und wohin geht's bergab?")
        with self.sprich("Um ein Modell zu trainieren, müssen wir wissen, in welche Richtung wir seine Parameter verändern sollen. "
                         "Dafür brauchen wir die Ableitung."):
            self.play(FadeIn(tg, shift=UP * 0.3))
        self.play(FadeOut(tg))

        ax = Axes(x_range=[-4, 4], y_range=[-3, 5], x_length=10, y_length=6, tips=False, axis_config={"color": MUTED})
        f = lambda x: 0.15 * x ** 3 - 0.9 * x + 1
        df = lambda x: 0.45 * x ** 2 - 0.9
        graph = ax.plot(f, color=TXT, x_range=[-3.9, 3.9])
        x0 = 1.2
        h = ValueTracker(2.0)
        p0 = Dot(ax.c2p(x0, f(x0)), color=TXT)
        p1 = always_redraw(lambda: Dot(ax.c2p(x0 + h.get_value(), f(x0 + h.get_value())), color=S2))

        def sec_line():
            hv = h.get_value()
            m = (f(x0 + hv) - f(x0)) / hv
            return ax.plot(lambda x: f(x0) + m * (x - x0), x_range=[-3.5, 3.5], color=S2)

        sec = always_redraw(sec_line)
        label = always_redraw(lambda: T(f"h = {h.get_value():.2f}   Steigung = {(f(x0 + h.get_value()) - f(x0)) / h.get_value():.3f}", 26, S2).to_corner(UL))
        with self.sprich("Nimm diese Kurve. Wie steil ist sie genau an dem weißen Punkt? Für eine Gerade wäre das leicht: "
                         "Höhenunterschied geteilt durch Abstand.") as t:
            self.play(Create(ax), Create(graph), run_time=t.dauer * 0.5)
            self.play(FadeIn(p0), run_time=t.dauer * 0.1)
        with self.sprich("Also legen wir eine Gerade durch zwei Punkte der Kurve, im Abstand h. Das nennt man eine Sekante.") as t:
            self.play(FadeIn(p1), Create(sec), FadeIn(label), run_time=t.dauer * 0.5)
        with self.sprich("Und jetzt der Trick: Wir schieben den zweiten Punkt immer näher heran. h wird winzig, "
                         "und die Sekante wird zur Tangente.") as t:
            self.play(h.animate.set_value(0.01), run_time=t.dauer * 0.9, rate_func=smooth)
        tan_txt = T(f"f'(x) = {df(x0):.3f}  –  die Ableitung", 30, S1).to_corner(UR)
        with self.sprich("Ihre Steigung ist die Ableitung. Hier ist sie leicht negativ. Das heißt: Wenn du x ein kleines Stück "
                         "vergrößerst, wird die Funktion kleiner. Genau diese Information brauchen wir, um bergab zu gehen."):
            self.play(Write(tan_txt))
        self.play(*[FadeOut(m) for m in self.mobjects])

        cap = T("Bei zwei Variablen: der Gradient ∇f = (∂f/∂x, ∂f/∂y)", 28).to_edge(UP)
        plane = NumberPlane(x_range=[-4, 4], y_range=[-3, 3], background_line_style={"stroke_color": "#262a33"},
                            axis_config={"color": MUTED}).shift(DOWN * 0.4)
        rings = VGroup(*[
            ParametricFunction(lambda t, c=c: plane.c2p(np.sqrt(2 * c) * np.cos(t), np.sqrt(2 * c / 3) * np.sin(t)),
                               t_range=[0, TAU], color=S1, stroke_opacity=0.35 + 0.05 * i)
            for i, c in enumerate([0.25, 0.75, 1.5, 2.5, 3.75, 5.25, 7])
        ])
        with self.sprich("Echte Modelle haben aber nicht einen Parameter, sondern viele. Dann wird die Kurve zu einer Landschaft. "
                         "Die Ringe hier sind Höhenlinien, wie auf einer Wanderkarte.") as t:
            self.play(FadeIn(cap), Create(plane), run_time=t.dauer * 0.35)
            self.play(Create(rings), run_time=t.dauer * 0.45)
        field = ArrowVectorField(lambda p: (lambda x, y: np.array([x, 3 * y, 0]) * 0.25)(*plane.p2c(p)),
                                 x_range=[-3.5, 3.5, 0.9], y_range=[-2.0, 2.0, 0.9], colors=[MUTED, S2])
        field.shift(DOWN * 0.4)
        with self.sprich("Für jede Richtung gibt es jetzt eine eigene Ableitung, die partielle Ableitung. Packst du sie zusammen "
                         "in einen Vektor, hast du den Gradienten. Und der zeigt immer in die Richtung, in der es am steilsten bergauf geht.") as t:
            self.play(Create(field), run_time=t.dauer * 0.6)
        note = T("Pfeile zeigen bergauf und stehen senkrecht auf den Höhenlinien", 22).to_edge(DOWN, buff=0.25)
        with self.sprich("Siehst du, wie die Pfeile immer senkrecht auf den Höhenlinien stehen?"):
            self.play(FadeIn(note))
        note2 = T("Für das Minimum gehen wir in Richtung −∇f  →  Gradientenabstieg", 24, S3).to_edge(DOWN, buff=0.25)
        with self.sprich("Und wenn wir das Minimum suchen, gehen wir einfach in die Gegenrichtung, also minus Gradient. "
                         "Das ist die Idee hinter dem Gradientenabstieg."):
            self.play(FadeOut(note), FadeIn(note2))


# ---------------------------------------------------------------------------
class GradientenAbstieg(SprecherSzene):
    """Video 4: Gradientenabstieg und der Einfluss der Lernrate."""

    def construct(self):
        tg = titel_gruppe("Gradientenabstieg", "Schritt für Schritt bergab")
        with self.sprich("Stell dir vor, du stehst nachts im Nebel auf einem Berg und willst ins Tal. Du siehst nichts, "
                         "aber du spürst, wie steil der Boden unter deinen Füßen ist."):
            self.play(FadeIn(tg, shift=UP * 0.3))
        self.play(FadeOut(tg))

        ax = Axes(x_range=[-5, 5], y_range=[0, 13], x_length=10, y_length=5.5, tips=False, axis_config={"color": MUTED}).shift(DOWN * 0.5)
        f = lambda x: 0.5 * x * x
        df = lambda x: x
        regel = T("x_neu = x − η · f'(x)", 34, S1).to_edge(UP)
        with self.sprich("Die naheliegende Strategie: Mach einen kleinen Schritt dahin, wo es bergab geht, und wiederhole das. "
                         "Als Formel: x neu gleich x minus eta mal die Ableitung.") as t:
            self.play(Create(ax), Create(ax.plot(f, color=TXT, x_range=[-5, 5])), run_time=t.dauer * 0.4)
            self.play(Write(regel), run_time=t.dauer * 0.4)
        with self.sprich("Eta ist die Lernrate. Sie bestimmt, wie groß jeder Schritt ist. Und wie du gleich siehst, "
                         "ist das der wichtigste Regler beim ganzen Training."):
            self.play(Indicate(regel, color=S2))

        def run(lr, start, color, label, sprech, steps=10):
            cap = T(label, 26, color).next_to(regel, DOWN)
            x = start
            ball = Dot(ax.c2p(x, f(x)), color=color, radius=0.13)
            trail = VGroup()
            with self.sprich(sprech) as t:
                self.play(FadeIn(cap), GrowFromCenter(ball), run_time=0.6)
                step_time = max(0.25, (t.dauer - 0.8) / steps)
                for _ in range(steps):
                    nx = x - lr * df(x)
                    if abs(nx) > 5:
                        warn = T("divergiert! η ist zu groß", 28, S2).move_to(ax.c2p(0, 10))
                        self.play(FadeIn(warn), run_time=0.4)
                        trail.add(warn)
                        break
                    arr = Arrow(ax.c2p(x, f(x)), ax.c2p(nx, f(nx)), buff=0.05, color=color, stroke_width=4,
                                max_tip_length_to_length_ratio=0.15)
                    self.play(GrowArrow(arr), ball.animate.move_to(ax.c2p(nx, f(nx))), run_time=step_time)
                    trail.add(arr)
                    x = nx
            self.play(FadeOut(trail), FadeOut(ball), FadeOut(cap), run_time=0.5)

        run(0.3, -4.5, S3, "η = 0.3 : stetig zum Minimum",
            "Mit einer Lernrate von null Komma drei läuft alles nach Plan. Am Anfang ist es steil, also macht die Kugel große Schritte. "
            "Je flacher es wird, desto kleiner werden sie, ganz von allein.")
        run(0.05, -4.5, S1, "η = 0.05 : sicher, aber sehr langsam",
            "Mit null Komma null fünf ist es zwar sicher, aber quälend langsam. Wir bräuchten hunderte Schritte.", steps=8)
        run(1.8, -2.0, S2, "η = 1.8 : springt hin und her",
            "Bei eins Komma acht springt die Kugel über das Minimum hinweg, hin und her. Sie kommt zwar an, aber auf Umwegen.", steps=7)
        run(2.2, -1.5, S2, "η = 2.2 : schießt über das Ziel hinaus",
            "Und bei zwei Komma zwei? Jeder Schritt landet höher als der davor. Das Training explodiert, man sagt: es divergiert.", steps=6)
        fazit = T("Die Lernrate ist der wichtigste Hyperparameter des Trainings.", 28).to_edge(DOWN, buff=0.3)
        with self.sprich("Merke dir also: Zu klein ist langsam, zu groß ist instabil. Eine gute Lernrate zu finden, "
                         "gehört zum Handwerk – und genau so werden auch riesige neuronale Netze trainiert."):
            self.play(Write(fazit))


# ---------------------------------------------------------------------------
class RegressionLernen(SprecherSzene):
    """Video 5: Eine Gerade per Gradientenabstieg an Daten anpassen."""

    def construct(self):
        tg = titel_gruppe("Eine Gerade lernen", "Lineare Regression mit Gradientenabstieg")
        with self.sprich("Jetzt bringen wir alles zusammen und trainieren unser erstes richtiges Modell: eine Gerade, "
                         "die möglichst gut durch ein paar Datenpunkte läuft."):
            self.play(FadeIn(tg, shift=UP * 0.3))
        self.play(FadeOut(tg))

        data = np.array([[0.5, 1.6], [1.0, 2.1], [1.6, 2.4], [2.1, 3.3], [2.7, 3.2], [3.2, 4.1],
                         [3.8, 4.3], [4.3, 5.2], [4.9, 5.1], [5.4, 6.0]])
        X, Y = data[:, 0], data[:, 1]
        ax = Axes(x_range=[0, 6], y_range=[0, 7], x_length=6.2, y_length=5.2, tips=False,
                  axis_config={"color": MUTED}).to_edge(LEFT, buff=0.6).shift(DOWN * 0.3)
        dots = VGroup(*[Dot(ax.c2p(x, y), color=TXT, radius=0.08) for x, y in data])

        w, b = ValueTracker(-0.6), ValueTracker(3.5)
        line = always_redraw(lambda: ax.plot(lambda x: w.get_value() * x + b.get_value(), x_range=[0, 6], color=S1))
        res = always_redraw(lambda: VGroup(*[
            Line(ax.c2p(x, y), ax.c2p(x, w.get_value() * x + b.get_value()), color=S2, stroke_width=3)
            for x, y in data]))
        mse = lambda: float(np.mean((w.get_value() * X + b.get_value() - Y) ** 2))

        # rechte Spalte beginnt fest bei x = 0.8, damit sich nichts verschiebt
        def place(m, y):
            return m.move_to([0.8 + m.width / 2, y, 0])

        info = always_redraw(lambda: VGroup(
            place(T(f"ŷ = {w.get_value():.2f} · x + {b.get_value():.2f}", 28, S1), 2.9),
            place(T(f"MSE = {mse():.3f}", 28, S2), 2.3),
        ))
        with self.sprich("Hier sind unsere Daten. Und das hier ist unser Modell, eine Gerade mit Steigung w und Achsenabschnitt b. "
                         "Am Anfang liegt sie natürlich völlig daneben.") as t:
            self.play(Create(ax), LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.08), run_time=t.dauer * 0.45)
            self.play(Create(line), FadeIn(info), run_time=t.dauer * 0.35)
        with self.sprich("Die orangen Linien sind die Fehler, also wie weit jeder Punkt von der Geraden entfernt ist. "
                         "Wir quadrieren sie und nehmen den Durchschnitt. Das ist der mittlere quadratische Fehler, kurz M S E.") as t:
            self.play(Create(res), run_time=t.dauer * 0.4)
            self.play(Indicate(info[1], color=S2), run_time=t.dauer * 0.3)

        erkl = VGroup(
            T("1. Vorhersage berechnen", 24),
            T("2. Fehler (Residuen) messen", 24, S2),
            T("3. Gradient von MSE nach w, b", 24),
            T("4. kleinen Schritt bergab", 24, S3),
            T("5. wiederholen", 24),
        ).arrange(DOWN, aligned_edge=LEFT)
        erkl.move_to([0.8 + erkl.width / 2, 0.2, 0])
        with self.sprich("Das Training ist eine Schleife aus fünf Schritten: Vorhersage berechnen, Fehler messen, "
                         "den Gradienten des Fehlers nach w und b ausrechnen, einen kleinen Schritt bergab machen, und wiederholen.") as t:
            self.play(LaggedStart(*[FadeIn(e, shift=RIGHT * 0.2) for e in erkl], lag_ratio=0.5), run_time=t.dauer * 0.8)

        lr = 0.03
        wv, bv = w.get_value(), b.get_value()
        with self.sprich("Schau zu, was passiert. Mit jedem Schritt dreht und verschiebt sich die Gerade ein kleines bisschen, "
                         "und der Fehler wird kleiner und kleiner.") as t:
            n = 60
            for epoch in range(n):
                r = wv * X + bv - Y
                gw, gb = 2 * np.mean(r * X), 2 * np.mean(r)
                wv, bv = wv - lr * gw, bv - lr * gb
                self.play(w.animate.set_value(wv), b.animate.set_value(bv), run_time=t.dauer * 0.9 / n, rate_func=linear)
        wopt, bopt = np.polyfit(X, Y, 1)
        later = T("… nach 2000 Schritten:", 24, MUTED).next_to(erkl, DOWN, buff=0.5, aligned_edge=LEFT)
        with self.sprich("Und nach ein paar tausend Schritten liegt sie genau richtig. Niemand hat dem Computer gesagt, wo die Gerade hin muss. "
                         "Er hat es aus den Daten gelernt. Und genau das ist Machine Learning.") as t:
            self.play(FadeIn(later), run_time=t.dauer * 0.15)
            self.play(w.animate.set_value(wopt), b.animate.set_value(bopt), run_time=t.dauer * 0.35)
