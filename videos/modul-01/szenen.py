"""Erklärvideos für Modul 1 (Manim Community Edition).

Rendern: siehe videos/README.md, z. B.
    manim -qm szenen.py GradientenAbstieg

Es wird bewusst kein LaTeX verwendet (Text statt MathTex), damit die Szenen
ohne TeX-Installation rendern.
"""
import numpy as np
from manim import *

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


def titel(scene, text, sub=None):
    t = T(text, 44, weight=BOLD)
    group = VGroup(t)
    if sub:
        group.add(T(sub, 26, MUTED).next_to(t, DOWN))
    scene.play(FadeIn(group, shift=UP * 0.3))
    scene.wait(1.2)
    scene.play(FadeOut(group))


def box(label, color, w=2.6, h=1.1, size=26):
    r = RoundedRectangle(corner_radius=0.15, width=w, height=h, color=color, stroke_width=3)
    return VGroup(r, T(label, size).move_to(r))


# ---------------------------------------------------------------------------
class WasIstML(Scene):
    """Video 1: Klassisches Programmieren vs. Machine Learning."""

    def construct(self):
        titel(self, "Was ist Machine Learning?", "Regeln programmieren vs. Regeln lernen")

        # Klassisch
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
        self.play(FadeIn(head), FadeIn(daten), FadeIn(regeln))
        self.play(GrowArrow(arrows[0]), GrowArrow(arrows[1]), FadeIn(prog))
        self.play(GrowArrow(arrows[2]), FadeIn(antw))
        bsp = T('if "Gewinnspiel" in mail:  spam = True', 24, S2).to_edge(DOWN, buff=0.8)
        self.play(Write(bsp))
        self.wait(1.5)
        frage = T("Aber: Welche Regel erkennt eine Katze auf einem Foto?", 28, TXT).to_edge(DOWN, buff=0.8)
        self.play(ReplacementTransform(bsp, frage))
        self.wait(2)

        # Umdrehen: ML
        head2 = T("Machine Learning", 30, S1).to_edge(UP)
        labels = box("Antworten", S3).move_to(regeln)
        modell = box("Regeln = Modell", S2, w=3.4).move_to(antw)
        lern = box("Lernalgorithmus", MUTED, w=3.4, size=24).move_to(prog)
        self.play(FadeOut(frage), ReplacementTransform(head, head2))
        self.play(ReplacementTransform(antw, labels), ReplacementTransform(regeln, modell), ReplacementTransform(prog, lern))
        hinweis = T("Daten + Antworten  →  der Computer findet die Regeln selbst", 26).to_edge(DOWN, buff=0.8)
        self.play(Write(hinweis))
        self.wait(2.5)

        # Modell als Funktion
        self.play(*[FadeOut(m) for m in self.mobjects])
        f = T("ŷ = f(x)", 64, S2)
        expl = VGroup(
            T("x  –  Merkmale (Features), z. B. Wohnfläche, Lage", 26),
            T("ŷ  –  Vorhersage (Prediction), z. B. Preis", 26),
            T("f  –  das gelernte Modell", 26),
        ).arrange(DOWN, aligned_edge=LEFT).next_to(f, DOWN, buff=0.8)
        self.play(Write(f))
        for e in expl:
            self.play(FadeIn(e, shift=RIGHT * 0.3))
        self.wait(2)
        self.play(FadeOut(VGroup(f, expl)))

        # Lernen aus Beispielen: Punkte + Trenngerade
        ax = Axes(x_range=[0, 10], y_range=[0, 6], x_length=9, y_length=5.2, tips=False,
                  axis_config={"color": MUTED}).shift(DOWN * 0.3)
        rng = np.random.default_rng(3)
        a = [ax.c2p(*p) for p in rng.normal([3, 4], 0.7, (14, 2))]
        b = [ax.c2p(*p) for p in rng.normal([7, 2], 0.7, (14, 2))]
        dots_a = VGroup(*[Dot(p, color=S1, radius=0.09) for p in a])
        dots_b = VGroup(*[Dot(p, color=S2, radius=0.09) for p in b])
        cap = T("Aus Beispielen lernen: Wo verläuft die Grenze?", 28).to_edge(UP)
        self.play(Create(ax), FadeIn(cap))
        self.play(LaggedStart(*[GrowFromCenter(d) for d in [*dots_a, *dots_b]], lag_ratio=0.04))
        line = DashedLine(ax.c2p(1, 0.2), ax.c2p(9.5, 5.8), color=TXT)
        self.play(Create(line))
        neu = Dot(ax.c2p(4.2, 3.0), color=YELLOW, radius=0.13)
        q = T("neuer Punkt → Klasse blau", 24, S1).next_to(neu, LEFT)
        self.play(GrowFromCenter(neu), FadeIn(q))
        self.wait(2.5)


# ---------------------------------------------------------------------------
class Skalarprodukt(Scene):
    """Video 2: Skalarprodukt als Ähnlichkeit und Projektion."""

    def construct(self):
        titel(self, "Das Skalarprodukt", "die wichtigste Rechnung im Machine Learning")
        plane = NumberPlane(x_range=[-5, 5], y_range=[-3, 3], background_line_style={"stroke_color": "#262a33"},
                            axis_config={"color": MUTED}).shift(LEFT * 1.5)
        self.play(Create(plane))
        o = plane.c2p(0, 0)
        ang = ValueTracker(70 * DEGREES)
        a_vec = np.array([3, 1, 0])

        def b_end():
            return 2.5 * np.array([np.cos(ang.get_value()), np.sin(ang.get_value()), 0])

        va = Arrow(o, plane.c2p(*a_vec[:2]), buff=0, color=S1, stroke_width=6)
        vb = always_redraw(lambda: Arrow(o, plane.c2p(*b_end()[:2]), buff=0, color=S2, stroke_width=6))
        la = T("a", 30, S1).next_to(va.get_end(), RIGHT)
        lb = always_redraw(lambda: T("b", 30, S2).next_to(vb.get_end(), UP))

        def proj_pt():
            b = b_end()
            t = np.dot(a_vec, b) / np.dot(a_vec, a_vec)
            return t * a_vec

        proj = always_redraw(lambda: Line(o, plane.c2p(*proj_pt()[:2]), color=S3, stroke_width=12, stroke_opacity=0.7))
        drop = always_redraw(lambda: DashedLine(plane.c2p(*b_end()[:2]), plane.c2p(*proj_pt()[:2]), color=MUTED))
        self.play(GrowArrow(va), FadeIn(la))
        self.play(GrowArrow(vb), FadeIn(lb))

        formel = VGroup(
            T("a · b = a₁b₁ + a₂b₂", 28),
            T("     = ‖a‖ · ‖b‖ · cos θ", 28),
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UR).shift(LEFT * 0.2)
        self.play(Write(formel))
        self.play(Create(drop), Create(proj))

        wert = always_redraw(lambda: T(f"a · b = {np.dot(a_vec, b_end()):.2f}", 34,
                                       S3 if np.dot(a_vec, b_end()) > 0.05 else (S2 if np.dot(a_vec, b_end()) < -0.05 else TXT))
                             .to_corner(DR).shift(UP * 0.6 + LEFT * 0.3))
        self.add(wert)
        self.wait(1)
        for target, txt in [(20 * DEGREES, "ähnliche Richtung → großes Skalarprodukt"),
                            (np.arctan2(-3, 1) + np.pi, "senkrecht → Skalarprodukt = 0"),
                            (160 * DEGREES, "entgegengesetzt → negativ")]:
            cap = T(txt, 26).to_edge(DOWN, buff=0.3)
            self.play(ang.animate.set_value(target), FadeIn(cap), run_time=2)
            self.wait(1.3)
            self.play(FadeOut(cap))
        self.play(ang.animate.set_value(50 * DEGREES), run_time=1.5)
        ml = T("Im ML: Modell-Ausgabe  ŷ = w · x + b", 30, S1).to_edge(DOWN, buff=0.3)
        self.play(Write(ml))
        self.wait(2.5)


# ---------------------------------------------------------------------------
class AbleitungUndGradient(Scene):
    """Video 3: Von der Sekante zur Ableitung, dann zum Gradienten."""

    def construct(self):
        titel(self, "Ableitung & Gradient", "Wie steil ist es hier – und wohin geht's bergab?")
        ax = Axes(x_range=[-4, 4], y_range=[-3, 5], x_length=10, y_length=6, tips=False, axis_config={"color": MUTED})
        f = lambda x: 0.15 * x ** 3 - 0.9 * x + 1
        df = lambda x: 0.45 * x ** 2 - 0.9
        graph = ax.plot(f, color=TXT, x_range=[-3.9, 3.9])
        self.play(Create(ax), Create(graph))
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
        self.play(FadeIn(p0), FadeIn(p1), Create(sec), FadeIn(label))
        self.wait(0.5)
        self.play(h.animate.set_value(0.01), run_time=4, rate_func=smooth)
        tan_txt = T(f"f'(x) = {df(x0):.3f}  –  die Ableitung", 30, S1).to_corner(UR)
        self.play(Write(tan_txt))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # Gradient in 2D
        cap = T("Bei zwei Variablen: der Gradient ∇f = (∂f/∂x, ∂f/∂y)", 28).to_edge(UP)
        self.play(FadeIn(cap))
        plane = NumberPlane(x_range=[-4, 4], y_range=[-3, 3], background_line_style={"stroke_color": "#262a33"},
                            axis_config={"color": MUTED}).shift(DOWN * 0.4)
        g = lambda x, y: 0.5 * x * x + 1.5 * y * y
        rings = VGroup(*[
            ParametricFunction(lambda t, c=c: plane.c2p(np.sqrt(2 * c) * np.cos(t), np.sqrt(2 * c / 3) * np.sin(t)),
                               t_range=[0, TAU], color=S1, stroke_opacity=0.35 + 0.05 * i)
            for i, c in enumerate([0.25, 0.75, 1.5, 2.5, 3.75, 5.25, 7])
        ])
        self.play(Create(plane), Create(rings))
        field = ArrowVectorField(lambda p: (lambda x, y: np.array([x, 3 * y, 0]) * 0.25)(*plane.p2c(p)),
                                 x_range=[-3.5, 3.5, 0.9], y_range=[-2.0, 2.0, 0.9], colors=[MUTED, S2])
        field.shift(DOWN * 0.4)
        self.play(Create(field), run_time=2)
        note = T("Pfeile zeigen bergauf (steilster Anstieg) und stehen senkrecht auf den Höhenlinien", 22).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(note))
        self.wait(2)
        note2 = T("Für das Minimum gehen wir in Richtung −∇f  →  Gradientenabstieg", 24, S3).to_edge(DOWN, buff=0.25)
        self.play(ReplacementTransform(note, note2))
        self.wait(2.5)


# ---------------------------------------------------------------------------
class GradientenAbstieg(Scene):
    """Video 4: Gradientenabstieg und der Einfluss der Lernrate."""

    def construct(self):
        titel(self, "Gradientenabstieg", "Schritt für Schritt bergab")
        ax = Axes(x_range=[-5, 5], y_range=[0, 13], x_length=10, y_length=5.5, tips=False, axis_config={"color": MUTED}).shift(DOWN * 0.5)
        f = lambda x: 0.5 * x * x
        df = lambda x: x
        self.play(Create(ax), Create(ax.plot(f, color=TXT, x_range=[-5, 5])))
        regel = T("x_neu = x − η · f'(x)", 34, S1).to_edge(UP)
        self.play(Write(regel))
        self.wait(1)

        def run(lr, start, color, label, steps=10):
            cap = T(label, 26, color).next_to(regel, DOWN)
            self.play(FadeIn(cap))
            x = start
            ball = Dot(ax.c2p(x, f(x)), color=color, radius=0.13)
            self.play(GrowFromCenter(ball))
            trail = VGroup()
            for _ in range(steps):
                nx = x - lr * df(x)
                if abs(nx) > 5:
                    warn = T("divergiert! η ist zu groß", 28, S2).move_to(ax.c2p(0, 10))
                    self.play(FadeIn(warn))
                    self.wait(1)
                    trail.add(warn)
                    break
                arr = Arrow(ax.c2p(x, f(x)), ax.c2p(nx, f(nx)), buff=0.05, color=color, stroke_width=4, max_tip_length_to_length_ratio=0.15)
                self.play(GrowArrow(arr), ball.animate.move_to(ax.c2p(nx, f(nx))), run_time=0.45)
                trail.add(arr)
                x = nx
            self.wait(1)
            self.play(FadeOut(trail), FadeOut(ball), FadeOut(cap))

        run(0.3, -4.5, S3, "η = 0.3 : stetig zum Minimum")
        run(0.05, -4.5, S1, "η = 0.05 : sicher, aber sehr langsam", steps=8)
        run(1.8, -2.0, S2, "η = 1.8 : springt hin und her", steps=7)
        run(2.2, -1.5, S2, "η = 2.2 : schießt über das Ziel hinaus", steps=6)
        fazit = T("Die Lernrate ist der wichtigste Hyperparameter des Trainings.", 28).to_edge(DOWN, buff=0.3)
        self.play(Write(fazit))
        self.wait(2.5)


# ---------------------------------------------------------------------------
class RegressionLernen(Scene):
    """Video 5: Eine Gerade per Gradientenabstieg an Daten anpassen."""

    def construct(self):
        titel(self, "Eine Gerade lernen", "Lineare Regression mit Gradientenabstieg")
        data = np.array([[0.5, 1.6], [1.0, 2.1], [1.6, 2.4], [2.1, 3.3], [2.7, 3.2], [3.2, 4.1],
                         [3.8, 4.3], [4.3, 5.2], [4.9, 5.1], [5.4, 6.0]])
        X, Y = data[:, 0], data[:, 1]
        ax = Axes(x_range=[0, 6], y_range=[0, 7], x_length=6.2, y_length=5.2, tips=False,
                  axis_config={"color": MUTED}).to_edge(LEFT, buff=0.6).shift(DOWN * 0.3)
        dots = VGroup(*[Dot(ax.c2p(x, y), color=TXT, radius=0.08) for x, y in data])
        self.play(Create(ax), LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.08))

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
        self.play(Create(line), Create(res), FadeIn(info))
        erkl = VGroup(
            T("1. Vorhersage berechnen", 24),
            T("2. Fehler (Residuen) messen", 24, S2),
            T("3. Gradient von MSE nach w, b", 24),
            T("4. kleinen Schritt bergab", 24, S3),
            T("5. wiederholen", 24),
        ).arrange(DOWN, aligned_edge=LEFT)
        erkl.move_to([0.8 + erkl.width / 2, 0.2, 0])
        self.play(LaggedStart(*[FadeIn(e, shift=RIGHT * 0.2) for e in erkl], lag_ratio=0.3))

        lr = 0.03
        wv, bv = w.get_value(), b.get_value()
        for epoch in range(60):
            r = wv * X + bv - Y
            gw, gb = 2 * np.mean(r * X), 2 * np.mean(r)
            wv, bv = wv - lr * gw, bv - lr * gb
            t = 0.35 if epoch < 8 else 0.08
            self.play(w.animate.set_value(wv), b.animate.set_value(bv), run_time=t, rate_func=linear)
        # danach die exakte Lösung (viele Schritte später)
        wopt, bopt = np.polyfit(X, Y, 1)
        later = T("… nach 2000 Schritten:", 24, MUTED).next_to(erkl, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(FadeIn(later))
        self.play(w.animate.set_value(wopt), b.animate.set_value(bopt), run_time=1.5)
        self.wait(2.5)
