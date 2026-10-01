"""Quelle der Notebooks für Modul 1. Erzeugen mit:  python tools/build_all.py"""
from nbbuild import code, md

SETUP = code("""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (7, 4)
rng = np.random.default_rng(42)
""")

# ---------------------------------------------------------------------------
NB01 = ("01_was_ist_ml", "1.1 Was ist Machine Learning?", [
    md("""
Dieses Notebook gehört zu **Lektion 1.1** auf der Kurs-Website.

Du wirst
1. einen echten Datensatz als Matrix `X` und Vektor `y` kennenlernen,
2. dein erstes scikit-learn-Modell trainieren und bewerten,
3. den k-Nächste-Nachbarn-Algorithmus selbst implementieren,
4. sehen, wie der Hyperparameter `k` Over- und Underfitting steuert.

Zellen mit `# TODO` sind deine Aufgaben. Die Lösung liegt im Ordner `loesungen/`.
"""),
    SETUP,
    md("""
## 1. Der Datensatz

Der **Iris-Datensatz** enthält 150 Blüten von drei Schwertlilien-Arten. Für jede Blüte sind vier Merkmale gemessen
(Länge und Breite von Kelch- und Blütenblatt, in cm). Er ist in scikit-learn eingebaut.
"""),
    code("""
from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target
print("Feature-Namen:", iris.feature_names)
print("Klassen:      ", iris.target_names)
print("X:", X.shape, " y:", y.shape)
print(X[:5])
print(y[:5])
"""),
    md("""
**Aufgabe 1.1:** Beantworte mit Code:
- Wie viele Beispiele und wie viele Features gibt es?
- Wie viele Beispiele hat jede Klasse? (Tipp: `np.bincount`)
"""),
    code("""
# >>> Anzahl Beispiele und Features aus X.shape auslesen
#! n_beispiele, n_features = ...
n_beispiele, n_features = X.shape
# <<<
# >>> Anzahl Beispiele pro Klasse zählen
#! pro_klasse = ...
pro_klasse = np.bincount(y)
# <<<
print(n_beispiele, n_features, pro_klasse)
"""),
    md("Zwei Features lassen sich als Punktwolke zeichnen. Jede Farbe ist eine Klasse – das sind die **Labels**."),
    code("""
plt.scatter(X[:, 2], X[:, 3], c=y, cmap="viridis", edgecolor="k")
plt.xlabel(iris.feature_names[2]); plt.ylabel(iris.feature_names[3])
plt.title("Iris: Blütenblatt-Länge vs. -Breite")
plt.show()
"""),
    md("""
## 2. Dein erstes Modell mit scikit-learn

Jedes scikit-learn-Modell folgt demselben Muster:

```python
model = Modellklasse(hyperparameter=...)
model.fit(X_train, y_train)      # Training
y_pred = model.predict(X_test)   # Inferenz
```

Damit wir ehrlich messen, teilen wir die Daten in **Training** und **Test**. Das Modell sieht die Testdaten beim Training nie.
"""),
    code("""
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0, stratify=y)
print(X_train.shape, X_test.shape)
"""),
    md("**Aufgabe 2.1:** Trainiere einen `KNeighborsClassifier` mit `n_neighbors=5` und berechne die Genauigkeit (Anteil richtiger Vorhersagen) auf den Testdaten."),
    code("""
# >>> Modell erzeugen und trainieren
#! model = ...
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
# <<<
# >>> Vorhersagen für X_test berechnen und Genauigkeit bestimmen
#! y_pred = ...
#! genauigkeit = ...
y_pred = model.predict(X_test)
genauigkeit = np.mean(y_pred == y_test)
# <<<
print(f"Genauigkeit: {genauigkeit:.3f}")
"""),
    md("""
## 3. k-Nächste-Nachbarn selbst bauen

Der Algorithmus ist verblüffend einfach:
1. Berechne die Distanz vom neuen Punkt zu **allen** Trainingspunkten.
2. Nimm die `k` Punkte mit der kleinsten Distanz.
3. Sage die Klasse vorher, die unter diesen `k` am häufigsten vorkommt.

Das "Training" besteht nur darin, die Daten zu speichern.
"""),
    code("""
class MeinKNN:
    def __init__(self, k=5):
        self.k = k

    def fit(self, X, y):
        # >>> Trainingsdaten speichern
        #! ...
        self.X_train = X
        self.y_train = y
        # <<<
        return self

    def predict_one(self, x):
        # >>> Euklidische Distanzen von x zu allen Trainingspunkten (ohne Schleife!)
        #! distanzen = ...
        distanzen = np.sqrt(((self.X_train - x) ** 2).sum(axis=1))
        # <<<
        # >>> Indizes der k kleinsten Distanzen (Tipp: np.argsort)
        #! naechste = ...
        naechste = np.argsort(distanzen)[: self.k]
        # <<<
        # >>> Häufigste Klasse unter den Nachbarn (Tipp: np.bincount + argmax)
        #! return ...
        return np.bincount(self.y_train[naechste]).argmax()
        # <<<

    def predict(self, X):
        return np.array([self.predict_one(x) for x in X])


mein = MeinKNN(k=5).fit(X_train, y_train)
meine_pred = mein.predict(X_test)
print("Meine Genauigkeit:  ", np.mean(meine_pred == y_test))
print("Stimmt mit sklearn überein:", np.all(meine_pred == y_pred))
"""),
    md("""
## 4. Over- und Underfitting

Wir messen die Genauigkeit auf Trainings- **und** Testdaten für verschiedene `k`.

**Aufgabe 4.1:** Fülle die beiden Listen und betrachte das Diagramm. Bei welchem `k` ist der Abstand zwischen Training und Test am größten? Was passiert bei sehr großem `k`?
"""),
    code("""
ks = list(range(1, 60, 2))
train_acc, test_acc = [], []
for k in ks:
    # >>> Modell mit k Nachbarn trainieren, Genauigkeit auf Training und Test anhängen
    #! ...
    m = KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train)
    train_acc.append(m.score(X_train, y_train))
    test_acc.append(m.score(X_test, y_test))
    # <<<

plt.plot(ks, train_acc, "o-", label="Training")
plt.plot(ks, test_acc, "s-", label="Test")
plt.xlabel("k"); plt.ylabel("Genauigkeit"); plt.legend(); plt.title("Einfluss des Hyperparameters k")
plt.show()
"""),
    md("""
**Beobachtung:** Bei `k = 1` ist die Trainingsgenauigkeit 100 % – jeder Punkt ist sein eigener nächster Nachbar. Das Modell hat
auswendig gelernt. Bei sehr großem `k` werden die Vorhersagen grob, beide Genauigkeiten fallen: Underfitting.

## 5. Bonus: Entscheidungsgrenzen sichtbar machen

Wir nehmen nur zwei Features, damit wir zeichnen können, und färben ein feines Raster nach der Vorhersage ein.
"""),
    code("""
X2 = X[:, 2:4]
fig, axes = plt.subplots(1, 3, figsize=(13, 4))
xx, yy = np.meshgrid(np.linspace(0.5, 7.5, 300), np.linspace(-0.2, 2.8, 300))
gitter = np.c_[xx.ravel(), yy.ravel()]
for ax, k in zip(axes, [1, 15, 75]):
    m = KNeighborsClassifier(n_neighbors=k).fit(X2, y)
    zz = m.predict(gitter).reshape(xx.shape)
    ax.contourf(xx, yy, zz, alpha=0.3, cmap="viridis")
    ax.scatter(X2[:, 0], X2[:, 1], c=y, cmap="viridis", edgecolor="k", s=20)
    ax.set_title(f"k = {k}")
plt.show()
"""),
    md("""
## Zusammenfassung

- Ein Datensatz ist eine Matrix `X` (Beispiele × Features) plus ein Label-Vektor `y`.
- scikit-learn: `fit` zum Trainieren, `predict` für Vorhersagen, `score` für eine Standardmetrik.
- Bewertet wird **immer** auf Daten, die das Modell nicht gesehen hat.
- Hyperparameter wie `k` steuern, wie flexibel ein Modell ist – zu flexibel → Overfitting, zu starr → Underfitting.
"""),
])

# ---------------------------------------------------------------------------
NB02 = ("02_vektoren_matrizen", "1.2 Vektoren, Matrizen & Daten", [
    md("""
Begleit-Notebook zu **Lektion 1.2**. Du implementierst die Grundoperationen der linearen Algebra erst "von Hand" mit Schleifen
und dann vektorisiert mit NumPy – und misst, wie viel schneller das ist.
"""),
    SETUP,
    md("""
## 1. Das Skalarprodukt

**Aufgabe 1.1:** Implementiere das Skalarprodukt mit einer Schleife.
"""),
    code("""
def skalarprodukt(a, b):
    # >>> Summe der paarweisen Produkte mit einer for-Schleife
    #! ...
    summe = 0.0
    for ai, bi in zip(a, b):
        summe += ai * bi
    return summe
    # <<<

a = np.array([1.0, 2.0, 3.0])
b = np.array([4.0, -1.0, 2.0])
print(skalarprodukt(a, b), a @ b, np.dot(a, b))   # alle drei sollten 8.0 sein
"""),
    md("""
**Aufgabe 1.2:** Implementiere Norm, Winkel und Kosinus-Ähnlichkeit mithilfe von `@`.
Prüfe: Zwei senkrechte Vektoren haben den Winkel 90°.
"""),
    code("""
def norm(v):
    # >>> Länge: Wurzel aus v · v
    #! ...
    return np.sqrt(v @ v)
    # <<<

def kosinus_aehnlichkeit(a, b):
    # >>> (a · b) / (‖a‖ ‖b‖)
    #! ...
    return (a @ b) / (norm(a) * norm(b))
    # <<<

def winkel_grad(a, b):
    return np.degrees(np.arccos(np.clip(kosinus_aehnlichkeit(a, b), -1, 1)))

print(norm(np.array([3.0, 4.0])))                                  # 5.0
print(winkel_grad(np.array([1.0, 0.0]), np.array([0.0, 2.0])))     # 90.0
print(kosinus_aehnlichkeit(np.array([1.0, 1.0]), np.array([2.0, 2.0])))  # 1.0
"""),
    md("""
### Anwendung: Ähnliche Dokumente finden

Wir stellen Texte als **Wortzähl-Vektoren** dar (jede Position = ein Wort). Die Kosinus-Ähnlichkeit sagt, welche Texte inhaltlich
ähnlich sind – unabhängig von der Textlänge. Genau so funktionierten frühe Suchmaschinen.
"""),
    code("""
vokabular = ["ball", "tor", "spiel", "zinsen", "bank", "kredit"]
texte = {
    "Fußballbericht":   np.array([3, 4, 2, 0, 0, 0]),
    "Sportkommentar":   np.array([1, 2, 3, 0, 1, 0]),   # "bank" = Ersatzbank :)
    "Wirtschaftsnews":  np.array([0, 0, 0, 3, 2, 4]),
}
anfrage = np.array([1, 1, 0, 0, 0, 0])   # Suche nach "ball tor"

# >>> Kosinus-Ähnlichkeit der Anfrage zu jedem Text ausgeben, sortiert absteigend
#! ...
for name, v in sorted(texte.items(), key=lambda kv: -kosinus_aehnlichkeit(anfrage, kv[1])):
    print(f"{name:18s} {kosinus_aehnlichkeit(anfrage, v):.3f}")
# <<<
"""),
    md("""
## 2. Distanzen

**Aufgabe 2.1:** Implementiere euklidische und Manhattan-Distanz **ohne Schleife**. Berechne dann die Distanzmatrix aller Punkte
zueinander mit Broadcasting: `P[:, None, :] - P[None, :, :]` hat die Form `(n, n, d)`.
"""),
    code("""
def euklid(p, q):
    # >>> L2-Distanz
    #! ...
    return np.sqrt(((p - q) ** 2).sum())
    # <<<

def manhattan(p, q):
    # >>> L1-Distanz
    #! ...
    return np.abs(p - q).sum()
    # <<<

p, q = np.array([-2.0, -1.0]), np.array([2.0, 1.5])
print(euklid(p, q), manhattan(p, q))   # 4.717..., 6.5

P = rng.normal(size=(5, 2))
# >>> Distanzmatrix D mit D[i, j] = euklidische Distanz zwischen P[i] und P[j]
#! D = ...
D = np.sqrt(((P[:, None, :] - P[None, :, :]) ** 2).sum(axis=-1))
# <<<
print(np.round(D, 2))
print("symmetrisch:", np.allclose(D, D.T), " Diagonale 0:", np.allclose(np.diag(D), 0))
"""),
    md("""
### Warum Skalierung wichtig ist

Zwei Wohnungen: Fläche in m² und Zimmerzahl. Welche ist Wohnung A "ähnlicher"?
"""),
    code("""
A = np.array([80.0, 2.0])
B = np.array([82.0, 5.0])    # fast gleiche Fläche, ganz andere Zimmerzahl
C = np.array([95.0, 2.0])    # gleiche Zimmerzahl, etwas größer
print("d(A,B) =", euklid(A, B), "  d(A,C) =", euklid(A, C))

daten = np.array([A, B, C, [60, 1], [120, 4], [70, 3]])
# >>> Standardisiere jede Spalte: (x - Mittelwert) / Standardabweichung (axis=0, Broadcasting!)
#! Z = ...
Z = (daten - daten.mean(axis=0)) / daten.std(axis=0)
# <<<
print("standardisiert: d(A,B) =", round(euklid(Z[0], Z[1]), 3), "  d(A,C) =", round(euklid(Z[0], Z[2]), 3))
"""),
    md("Unskaliert dominiert die Fläche. Nach der Standardisierung zählt die Zimmerzahl genauso – das Ergebnis dreht sich um."),
    md("""
## 3. Matrix mal Vektor: ein lineares Modell

Ein lineares Modell sagt für jede Zeile von `X` voraus: $\\hat y_i = w \\cdot x_i + b$.

**Aufgabe 3.1:** Berechne die Vorhersagen einmal mit Schleife und einmal mit `X @ w + b`. Vergleiche die Laufzeit.
"""),
    code("""
import time

n, d = 200_000, 20
X = rng.normal(size=(n, d))
w = rng.normal(size=d)
b = 0.5

t0 = time.perf_counter()
# >>> Vorhersagen mit einer Schleife über alle Zeilen (nutze deine Funktion skalarprodukt)
#! y_schleife = ...
y_schleife = np.array([skalarprodukt(x, w) + b for x in X])
# <<<
t1 = time.perf_counter()
# >>> Vorhersagen vektorisiert
#! y_vec = ...
y_vec = X @ w + b
# <<<
t2 = time.perf_counter()

print(f"Schleife: {t1 - t0:.3f} s   vektorisiert: {t2 - t1:.4f} s   Faktor: {(t1 - t0) / (t2 - t1):.0f}x")
print("gleiches Ergebnis:", np.allclose(y_schleife, y_vec))
"""),
    md("""
## 4. Matrizen als Abbildungen

Wir wenden verschiedene 2×2-Matrizen auf ein Gitter von Punkten an. **Aufgabe 4.1:** Ergänze die Drehmatrix für einen Winkel θ:

$$R(\\theta) = \\begin{pmatrix} \\cos\\theta & -\\sin\\theta \\\\ \\sin\\theta & \\cos\\theta \\end{pmatrix}$$
"""),
    code("""
def drehung(theta):
    # >>> 2x2-Drehmatrix
    #! ...
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    # <<<

gx, gy = np.meshgrid(np.linspace(-1, 1, 11), np.linspace(-1, 1, 11))
punkte = np.stack([gx.ravel(), gy.ravel()])        # Form (2, 121): Punkte als Spalten

matrizen = {"Drehung 30°": drehung(np.pi / 6), "Scherung": np.array([[1, 1], [0, 1]]),
            "Streckung": np.array([[2, 0], [0, 0.5]]), "singulär": np.array([[1, 2], [0.5, 1]])}
fig, axes = plt.subplots(1, 4, figsize=(15, 4))
for ax, (name, M) in zip(axes, matrizen.items()):
    neu = M @ punkte
    ax.scatter(*punkte, s=6, c="lightgray")
    ax.scatter(*neu, s=6)
    ax.set_title(f"{name}\\ndet = {np.linalg.det(M):.2f}")
    ax.set_aspect("equal"); ax.set_xlim(-3, 3); ax.set_ylim(-3, 3)
plt.show()
"""),
    md("""
**Aufgabe 4.2:** Prüfe numerisch: Eine Drehung ändert keine Längen (Determinante 1), und $R(\\theta)^{-1} = R(-\\theta) = R(\\theta)^\\top$.
"""),
    code("""
R = drehung(0.7)
v = np.array([3.0, 4.0])
# >>> Länge von v vor und nach der Drehung vergleichen, Inverse mit Transponierter vergleichen
#! ...
print(norm(v), norm(R @ v))
print(np.allclose(np.linalg.inv(R), R.T), np.allclose(R.T, drehung(-0.7)))
# <<<
"""),
    md("""
## 5. Ausblick: die Normalengleichung

Für lineare Regression gibt es die geschlossene Lösung $w^* = (X^\\top X)^{-1} X^\\top y$. Wir erzeugen Daten mit bekannten Gewichten
und prüfen, ob die Formel sie wiederfindet. (Der Bias wird über eine Spalte aus Einsen modelliert.)
"""),
    code("""
n = 500
X = rng.normal(size=(n, 3))
w_wahr = np.array([2.0, -1.0, 0.5])
y = X @ w_wahr + 3.0 + rng.normal(scale=0.1, size=n)

X1 = np.c_[np.ones(n), X]          # Spalte mit Einsen für den Bias
# >>> Normalengleichung (Tipp: np.linalg.solve(A, c) löst A x = c stabiler als inv)
#! w_hat = ...
w_hat = np.linalg.solve(X1.T @ X1, X1.T @ y)
# <<<
print("geschätzt:", np.round(w_hat, 3), "  wahr: [3. 2. -1. 0.5]")
"""),
])

# ---------------------------------------------------------------------------
NB03 = ("03_statistik", "1.3 Statistik & Wahrscheinlichkeit", [
    md("Begleit-Notebook zu **Lektion 1.3**: Kennzahlen, Verteilungen, Simulationen und eine erste Maximum-Likelihood-Schätzung."),
    SETUP,
    md("## 1. Kennzahlen selbst implementieren"),
    code("""
def mittelwert(x):
    # >>> Summe / Anzahl
    #! ...
    return x.sum() / len(x)
    # <<<

def varianz(x, ddof=0):
    # >>> mittlere quadrierte Abweichung; ddof=1 teilt durch n-1
    #! ...
    return ((x - mittelwert(x)) ** 2).sum() / (len(x) - ddof)
    # <<<

def median(x):
    # >>> sortieren, mittleres Element (bei gerader Anzahl: Mittel der beiden mittleren)
    #! ...
    s = np.sort(x)
    n = len(s)
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2
    # <<<

x = rng.normal(10, 2, size=1001)
print(mittelwert(x), np.mean(x))
print(varianz(x), np.var(x), varianz(x, ddof=1), np.var(x, ddof=1))
print(median(x), np.median(x))
"""),
    md("""
**Aufgabe 1.2:** Füge den Gehältern einen Ausreißer hinzu und beobachte, wie stark sich Mittelwert und Median ändern.
"""),
    code("""
gehaelter = np.array([42, 45, 47, 50, 51, 53, 55, 58, 60], dtype=float)  # in T€
# >>> Hänge ein Gehalt von 1000 T€ an und vergleiche Mittelwert und Median vorher/nachher
#! ...
mit_chefin = np.append(gehaelter, 1000.0)
print(f"vorher:  Mittelwert {mittelwert(gehaelter):7.1f}   Median {median(gehaelter):5.1f}")
print(f"nachher: Mittelwert {mittelwert(mit_chefin):7.1f}   Median {median(mit_chefin):5.1f}")
# <<<
"""),
    md("""
## 2. z-Scores und Ausreißer

**Aufgabe 2.1:** Berechne die z-Scores und finde alle Werte mit $|z| > 3$.
"""),
    code("""
messwerte = np.r_[rng.normal(50, 5, size=500), [85, 12, 90]]
# >>> z-Scores und Indizes der Ausreißer
#! z = ...
#! ausreisser = ...
z = (messwerte - messwerte.mean()) / messwerte.std()
ausreisser = np.where(np.abs(z) > 3)[0]
# <<<
print("Ausreißer:", messwerte[ausreisser])
"""),
    md("""
## 3. Zentraler Grenzwertsatz

Wir ziehen viele Stichproben aus einer **sehr schiefen** Verteilung (Exponentialverteilung) und schauen uns die Verteilung der Mittelwerte an.

**Aufgabe 3.1:** Für jedes `n` in `[1, 2, 10, 50]`: Ziehe 10 000 Stichproben der Größe `n` und berechne jeweils den Mittelwert.
Ergänze außerdem die theoretische Standardabweichung des Mittelwerts $\\sigma/\\sqrt{n}$ (hier ist $\\sigma = 1$).
"""),
    code("""
fig, axes = plt.subplots(1, 4, figsize=(15, 3.5))
for ax, n in zip(axes, [1, 2, 10, 50]):
    # >>> 10 000 Mittelwerte von je n exponentialverteilten Zahlen (rng.exponential(1.0, size=(10_000, n)))
    #! mittelwerte = ...
    mittelwerte = rng.exponential(1.0, size=(10_000, n)).mean(axis=1)
    # <<<
    # >>> theoretische Standardabweichung des Mittelwerts
    #! sd_theorie = ...
    sd_theorie = 1.0 / np.sqrt(n)
    # <<<
    ax.hist(mittelwerte, bins=60, density=True, alpha=0.7)
    t = np.linspace(mittelwerte.min(), mittelwerte.max(), 200)
    ax.plot(t, np.exp(-(t - 1) ** 2 / (2 * sd_theorie**2)) / (sd_theorie * np.sqrt(2 * np.pi)))
    ax.set_title(f"n = {n}: sd = {mittelwerte.std():.3f} (Theorie {sd_theorie:.3f})")
plt.show()
"""),
    md("""
## 4. Satz von Bayes durch Simulation

Statt die Formel anzuwenden, simulieren wir 1 000 000 Personen. **Aufgabe 4.1:** Ergänze die Simulation und vergleiche mit der Formel.
"""),
    code("""
N = 1_000_000
praevalenz, sensitivitaet, spezifitaet = 0.01, 0.95, 0.95

krank = rng.random(N) < praevalenz
# >>> Testergebnis simulieren: Kranke sind mit Wahrscheinlichkeit 'sensitivitaet' positiv,
# Gesunde mit Wahrscheinlichkeit 1 - spezifitaet
#! positiv = ...
zufall = rng.random(N)
positiv = np.where(krank, zufall < sensitivitaet, zufall < 1 - spezifitaet)
# <<<
# >>> P(krank | positiv) aus der Simulation und aus der Bayes-Formel
#! p_sim = ...
#! p_formel = ...
p_sim = krank[positiv].mean()
p_formel = sensitivitaet * praevalenz / (sensitivitaet * praevalenz + (1 - spezifitaet) * (1 - praevalenz))
# <<<
print(f"Simulation: {p_sim:.4f}   Formel: {p_formel:.4f}")
"""),
    md("""
## 5. Korrelation

**Aufgabe 5.1:** Implementiere den Pearson-Korrelationskoeffizienten und teste ihn an drei Fällen: linear, verrauscht, quadratisch.
"""),
    code("""
def pearson(x, y):
    # >>> Kovarianz / (sd_x * sd_y)
    #! ...
    xc, yc = x - x.mean(), y - y.mean()
    return (xc @ yc) / np.sqrt((xc @ xc) * (yc @ yc))
    # <<<

x = rng.uniform(-3, 3, 400)
faelle = {"linear": 2 * x + 1, "verrauscht": 2 * x + rng.normal(0, 3, 400), "quadratisch": x**2}
fig, axes = plt.subplots(1, 3, figsize=(13, 3.5))
for ax, (name, y) in zip(axes, faelle.items()):
    ax.scatter(x, y, s=8)
    ax.set_title(f"{name}: r = {pearson(x, y):.2f} (numpy: {np.corrcoef(x, y)[0, 1]:.2f})")
plt.show()
"""),
    md("""
## 6. Maximum Likelihood

Wir haben Daten aus einer Normalverteilung mit unbekanntem Mittelwert $\\mu$ (Standardabweichung 1 sei bekannt).
Die negative Log-Likelihood ist bis auf Konstanten

$$\\mathrm{NLL}(\\mu) = \\frac{1}{2}\\sum_i (x_i - \\mu)^2 .$$

**Aufgabe 6.1:** Berechne die NLL für viele Kandidaten $\\mu$ und finde das Minimum. Vergleiche mit dem Stichprobenmittelwert.
"""),
    code("""
daten = rng.normal(3.7, 1.0, size=50)
kandidaten = np.linspace(0, 8, 2001)
# >>> NLL für jeden Kandidaten (vektorisiert: kandidaten[:, None] - daten[None, :])
#! nll = ...
nll = 0.5 * ((daten[None, :] - kandidaten[:, None]) ** 2).sum(axis=1)
# <<<
mu_mle = kandidaten[np.argmin(nll)]
plt.plot(kandidaten, nll); plt.axvline(mu_mle, ls="--")
plt.xlabel("μ"); plt.ylabel("negative Log-Likelihood"); plt.show()
print(f"MLE: {mu_mle:.3f}   Stichprobenmittelwert: {daten.mean():.3f}")
"""),
    md("""
Die MLE ist genau der Mittelwert – und die NLL ist (bis auf den Faktor) der **quadratische Fehler**.
Das ist der Grund, warum MSE für Regression so natürlich ist (Lektion 5).
"""),
])

# ---------------------------------------------------------------------------
NB04 = ("04_ableitungen_gradienten", "1.4 Ableitungen & Gradienten", [
    md("Begleit-Notebook zu **Lektion 1.4**: numerische Ableitungen, Gradienten, Gradient Checking und ein Mini-Autograd mit der Kettenregel."),
    SETUP,
    md("## 1. Numerische Ableitung"),
    code("""
def ableitung(f, x, h=1e-5):
    # >>> zentrale Differenz
    #! ...
    return (f(x + h) - f(x - h)) / (2 * h)
    # <<<

f = lambda x: 0.15 * x**3 - 0.9 * x + 1
df = lambda x: 0.45 * x**2 - 0.9          # analytisch
for x in [-2.0, 0.0, 1.2, 3.0]:
    print(f"x = {x:5.1f}: analytisch {df(x):8.5f}  numerisch {ableitung(f, x):8.5f}")
"""),
    md("""
**Aufgabe 1.2:** Wie hängt der Fehler der Vorwärts- bzw. zentralen Differenz von `h` ab? Zeichne beide Fehler log-log.
Warum wird der Fehler für sehr kleine `h` wieder größer? (Stichwort: Rundungsfehler bei Gleitkommazahlen)
"""),
    code("""
hs = np.logspace(-14, -1, 60)
x0 = 1.2
# >>> Fehler der Vorwärtsdifferenz (f(x+h)-f(x))/h und der zentralen Differenz gegenüber df(x0)
#! fehler_vor = ...
#! fehler_zentral = ...
fehler_vor = np.abs((f(x0 + hs) - f(x0)) / hs - df(x0))
fehler_zentral = np.abs((f(x0 + hs) - f(x0 - hs)) / (2 * hs) - df(x0))
# <<<
plt.loglog(hs, fehler_vor, label="vorwärts"); plt.loglog(hs, fehler_zentral, label="zentral")
plt.xlabel("h"); plt.ylabel("absoluter Fehler"); plt.legend(); plt.show()
"""),
    md("""
## 2. Gradienten

**Aufgabe 2.1:** Implementiere einen numerischen Gradienten für Funktionen $f: \\mathbb{R}^d \\to \\mathbb{R}$ (eine Komponente nach der anderen)
und vergleiche ihn mit dem analytischen Gradienten von $f(x, y) = x^2 + 3xy + y^3$.
"""),
    code("""
def num_gradient(f, v, h=1e-5):
    g = np.zeros_like(v, dtype=float)
    for i in range(len(v)):
        # >>> Einheitsvektor e_i bauen, zentrale Differenz in Richtung e_i
        #! ...
        e = np.zeros_like(v, dtype=float)
        e[i] = h
        g[i] = (f(v + e) - f(v - e)) / (2 * h)
        # <<<
    return g

f2 = lambda v: v[0] ** 2 + 3 * v[0] * v[1] + v[1] ** 3
# >>> analytischer Gradient (siehe Lektion)
#! grad_f2 = lambda v: ...
grad_f2 = lambda v: np.array([2 * v[0] + 3 * v[1], 3 * v[0] + 3 * v[1] ** 2])
# <<<
p = np.array([1.0, -2.0])
print(num_gradient(f2, p), grad_f2(p))
"""),
    md("### Gradientenfeld zeichnen"),
    code("""
g = lambda v: 0.5 * v[0] ** 2 + 1.5 * v[1] ** 2
xs, ys = np.meshgrid(np.linspace(-3, 3, 200), np.linspace(-2, 2, 200))
plt.contour(xs, ys, g([xs, ys]), levels=15)
qx, qy = np.meshgrid(np.linspace(-3, 3, 13), np.linspace(-2, 2, 9))
plt.quiver(qx, qy, qx, 3 * qy, color="tab:orange")    # ∇g = (x, 3y)
plt.gca().set_aspect("equal"); plt.title("Gradienten stehen senkrecht auf den Höhenlinien"); plt.show()
"""),
    md("""
## 3. Gradient Checking für den MSE

Das lineare Modell $\\hat y = Xw + b$ mit $L = \\frac1n \\sum (\\hat y_i - y_i)^2$ hat die Gradienten
$\\nabla_w L = \\frac{2}{n} X^\\top(\\hat y - y)$ und $\\partial L/\\partial b = \\frac{2}{n}\\sum(\\hat y_i - y_i)$.

**Aufgabe 3.1:** Implementiere beide und prüfe sie mit `num_gradient`.
"""),
    code("""
X = rng.normal(size=(30, 3))
y = rng.normal(size=30)
w = rng.normal(size=3)
b = 0.3

def mse(w, b):
    return np.mean((X @ w + b - y) ** 2)

def mse_gradient(w, b):
    # >>> analytische Gradienten nach w und b
    #! ...
    r = X @ w + b - y
    return 2 / len(y) * X.T @ r, 2 / len(y) * r.sum()
    # <<<

gw, gb = mse_gradient(w, b)
gw_num = num_gradient(lambda v: mse(v, b), w)
gb_num = num_gradient(lambda v: mse(w, v[0]), np.array([b]))[0]
print("max. Abweichung w:", np.max(np.abs(gw - gw_num)), "  b:", abs(gb - gb_num))
"""),
    md("""
## 4. Mini-Autograd: die Kettenregel automatisch

So funktionieren PyTorch & Co. im Kern: Jede Rechenoperation merkt sich ihre Eingaben und ihre **lokale Ableitung**.
`backward()` läuft den Graphen rückwärts und multipliziert nach der Kettenregel.

**Aufgabe 4.1:** Ergänze die lokalen Ableitungen für `*` und `**`.
"""),
    code("""
class Wert:
    def __init__(self, data, eltern=(), name=""):
        self.data, self.grad = data, 0.0
        self._eltern = eltern
        self._rueckwaerts = lambda: None
        self.name = name

    def __add__(self, other):
        other = other if isinstance(other, Wert) else Wert(other)
        out = Wert(self.data + other.data, (self, other))
        def rueckwaerts():
            self.grad += 1.0 * out.grad        # d(a+b)/da = 1
            other.grad += 1.0 * out.grad       # d(a+b)/db = 1
        out._rueckwaerts = rueckwaerts
        return out

    def __mul__(self, other):
        other = other if isinstance(other, Wert) else Wert(other)
        out = Wert(self.data * other.data, (self, other))
        def rueckwaerts():
            # >>> d(a*b)/da = b, d(a*b)/db = a  — jeweils mal out.grad (Kettenregel)
            #! ...
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
            # <<<
        out._rueckwaerts = rueckwaerts
        return out

    def __pow__(self, k):
        out = Wert(self.data ** k, (self,))
        def rueckwaerts():
            # >>> d(a^k)/da = k * a^(k-1)
            #! ...
            self.grad += k * self.data ** (k - 1) * out.grad
            # <<<
        out._rueckwaerts = rueckwaerts
        return out

    __radd__ = __add__
    __rmul__ = __mul__

    def backward(self):
        # Knoten in topologischer Reihenfolge sammeln, dann rückwärts abarbeiten
        reihenfolge, besucht = [], set()
        def besuche(v):
            if v not in besucht:
                besucht.add(v)
                for e in v._eltern:
                    besuche(e)
                reihenfolge.append(v)
        besuche(self)
        self.grad = 1.0
        for v in reversed(reihenfolge):
            v._rueckwaerts()


# Beispiel aus der Lektion: f(x) = (3x + 1)^2 bei x = 2  →  df/dx = 42
x = Wert(2.0)
f = (3 * x + 1) ** 2
f.backward()
print("f =", f.data, " df/dx =", x.grad)
"""),
    md("""
**Aufgabe 4.2:** Nutze dein Autograd für ein lineares Modell mit einem Beispiel: $L = (w x + b - y)^2$ mit $x=1.5$, $y=4$, $w=0.5$, $b=1$.
Vergleiche `w.grad` und `b.grad` mit den Formeln $2(\\hat y - y)x$ und $2(\\hat y - y)$.
"""),
    code("""
# >>> Werte anlegen, Verlust berechnen, backward() aufrufen
#! ...
w, b = Wert(0.5), Wert(1.0)
x_, y_ = 1.5, 4.0
L = (w * x_ + b + (-y_)) ** 2
L.backward()
y_hat = 0.5 * 1.5 + 1.0
print("Autograd:", w.grad, b.grad)
print("Formel:  ", 2 * (y_hat - y_) * x_, 2 * (y_hat - y_))
# <<<
"""),
])

# ---------------------------------------------------------------------------
NB05 = ("05_gradientenabstieg", "1.5 Verlustfunktionen & Gradientenabstieg", [
    md("Begleit-Notebook zu **Lektion 1.5**: Verlustfunktionen, Gradientenabstieg in 1D und 2D, Lernraten-Experimente und SGD."),
    SETUP,
    md("## 1. Verlustfunktionen"),
    code("""
def mse(y, y_hat):
    # >>> mittlerer quadratischer Fehler
    #! ...
    return np.mean((y - y_hat) ** 2)
    # <<<

def mae(y, y_hat):
    # >>> mittlerer absoluter Fehler
    #! ...
    return np.mean(np.abs(y - y_hat))
    # <<<

def kreuzentropie(y, p, eps=1e-12):
    # >>> binäre Kreuzentropie; p mit np.clip in [eps, 1-eps] halten, damit log(0) nicht vorkommt
    #! ...
    p = np.clip(p, eps, 1 - eps)
    return -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))
    # <<<

y = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
print(mse(y, y + np.array([1, -1, 2, -2, 10])), mae(y, y + np.array([1, -1, 2, -2, 10])))  # 22.0  3.2
print(kreuzentropie(np.array([1, 0, 1]), np.array([0.9, 0.1, 0.8])))   # ~0.145
print(kreuzentropie(np.array([1]), np.array([0.01])))                    # sicher und falsch: ~4.6
"""),
    md("""
**Aufgabe 1.2:** Welcher konstante Wert $c$ minimiert MSE bzw. MAE für die Daten unten? Probiere viele Kandidaten aus und vergleiche mit Mittelwert und Median.
"""),
    code("""
daten = np.array([1, 2, 2, 3, 4, 5, 30], dtype=float)
cs = np.linspace(0, 30, 3001)
# >>> MSE und MAE für jeden Kandidaten c (Vorhersage = c für alle Punkte)
#! mse_c = ...
#! mae_c = ...
mse_c = np.array([mse(daten, c) for c in cs])
mae_c = np.array([mae(daten, c) for c in cs])
# <<<
print("bestes c für MSE:", cs[mse_c.argmin()], " Mittelwert:", daten.mean())
print("bestes c für MAE:", cs[mae_c.argmin()], " Median:   ", np.median(daten))
"""),
    md("""
## 2. Gradientenabstieg in 1D

**Aufgabe 2.1:** Implementiere den Gradientenabstieg. Die Funktion soll den ganzen Pfad zurückgeben.
"""),
    code("""
def gradientenabstieg_1d(df, x0, lr, schritte):
    pfad = [x0]
    x = x0
    for _ in range(schritte):
        # >>> ein Schritt gegen die Ableitung
        #! ...
        x = x - lr * df(x)
        # <<<
        pfad.append(x)
    return np.array(pfad)

f = lambda x: 0.5 * x**2
df = lambda x: x
fig, axes = plt.subplots(1, 4, figsize=(15, 3.5), sharey=True)
t = np.linspace(-5, 5, 200)
for ax, lr in zip(axes, [0.05, 0.3, 1.8, 2.1]):
    pfad = gradientenabstieg_1d(df, -4.0, lr, 12)
    ax.plot(t, f(t), color="gray")
    ax.plot(pfad, f(pfad), "o-", ms=4)
    ax.set_ylim(0, 13); ax.set_xlim(-5, 5); ax.set_title(f"η = {lr}")
plt.show()
"""),
    md("""
**Aufgabe 2.2:** Für $f(x) = \\frac{k}{2}x^2$ divergiert der Gradientenabstieg ab $\\eta = 2/k$. Überprüfe das experimentell für $k = 4$:
Wie groß ist $|x|$ nach 50 Schritten für $\\eta = 0{,}49$ und $\\eta = 0{,}51$?
"""),
    code("""
k = 4
# >>> zwei Läufe mit df = k*x, Start 1.0, je 50 Schritte; letzte |x| ausgeben
#! ...
for lr in [0.49, 0.51]:
    pfad = gradientenabstieg_1d(lambda x: k * x, 1.0, lr, 50)
    print(f"η = {lr}: |x_50| = {abs(pfad[-1]):.3e}")
# <<<
"""),
    md("""
## 3. Gradientenabstieg in 2D und das Zickzack-Problem

**Aufgabe 3.1:** Implementiere die 2D-Version (mit Vektoren!) und vergleiche ein rundes und ein langgezogenes Tal.
"""),
    code("""
def gradientenabstieg(grad, start, lr, schritte):
    theta = np.array(start, dtype=float)
    pfad = [theta.copy()]
    for _ in range(schritte):
        # >>> Vektor-Update
        #! ...
        theta = theta - lr * grad(theta)
        # <<<
        pfad.append(theta.copy())
    return np.array(pfad)

fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
xs, ys = np.meshgrid(np.linspace(-4, 4, 200), np.linspace(-2.5, 2.5, 200))
for ax, k in zip(axes, [1, 8]):
    grad = lambda th, k=k: np.array([th[0], k * th[1]])
    pfad = gradientenabstieg(grad, [-3.5, 2.0], lr=0.22, schritte=40)
    ax.contour(xs, ys, 0.5 * (xs**2 + k * ys**2), levels=20, alpha=0.6)
    ax.plot(pfad[:, 0], pfad[:, 1], "o-", ms=3, color="tab:orange")
    ax.set_aspect("equal"); ax.set_title(f"Streckung k = {k}: Endpunkt {np.round(pfad[-1], 3)}")
plt.show()
"""),
    md("""
## 4. Lineare Regression mit Gradientenabstieg

Wir erzeugen Daten $y = 3x - 2 + \\text{Rauschen}$ und lernen $w$ und $b$.

**Aufgabe 4.1:** Ergänze den Trainingsschritt und zeichne die Lernkurve.
"""),
    code("""
n = 200
x = rng.uniform(0, 5, n)
y = 3 * x - 2 + rng.normal(0, 1, n)

def train_gd(x, y, lr, epochen):
    w, b = 0.0, 0.0
    verluste = []
    for _ in range(epochen):
        y_hat = w * x + b
        # >>> Gradienten von MSE nach w und b, dann Update
        #! ...
        r = y_hat - y
        grad_w = 2 * np.mean(r * x)
        grad_b = 2 * np.mean(r)
        w -= lr * grad_w
        b -= lr * grad_b
        # <<<
        verluste.append(np.mean((w * x + b - y) ** 2))
    return w, b, verluste

w, b, verluste = train_gd(x, y, lr=0.05, epochen=300)
print(f"gelernt: w = {w:.3f}, b = {b:.3f}  (wahr: 3, -2)")

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].scatter(x, y, s=8); t = np.linspace(0, 5, 2); axes[0].plot(t, w * t + b, color="tab:orange")
axes[1].plot(verluste); axes[1].set_yscale("log"); axes[1].set_xlabel("Epoche"); axes[1].set_ylabel("MSE")
plt.show()
"""),
    md("""
## 5. Batch vs. Mini-Batch vs. SGD

**Aufgabe 5.1:** Implementiere Mini-Batch-GD: In jeder Epoche die Daten mischen und in Gruppen der Größe `batch` durchgehen.
Mit `batch = n` ist das Batch-GD, mit `batch = 1` SGD. Vergleiche die Lernkurven über die **Anzahl Updates**.
"""),
    code("""
def train_minibatch(x, y, lr, epochen, batch, seed=0):
    r_gen = np.random.default_rng(seed)
    w, b = 0.0, 0.0
    verluste = []
    for _ in range(epochen):
        idx = r_gen.permutation(len(x))
        for start in range(0, len(x), batch):
            # >>> Mini-Batch auswählen, Gradient auf dem Batch berechnen, Update; danach Gesamt-MSE anhängen
            #! ...
            sel = idx[start:start + batch]
            r = w * x[sel] + b - y[sel]
            w -= lr * 2 * np.mean(r * x[sel])
            b -= lr * 2 * np.mean(r)
            verluste.append(np.mean((w * x + b - y) ** 2))
            # <<<
    return w, b, verluste

for batch, lr in [(n, 0.05), (32, 0.05), (1, 0.01)]:
    w_, b_, v = train_minibatch(x, y, lr, epochen=20, batch=batch)
    plt.plot(v[:600], label=f"Batchgröße {batch}: w={w_:.2f}, b={b_:.2f}")
plt.yscale("log"); plt.xlabel("Anzahl Updates"); plt.ylabel("MSE (alle Daten)"); plt.legend(); plt.show()
"""),
    md("""
**Beobachtung:** Kleine Batches machen viel mehr Updates pro Epoche und kommen deshalb schneller voran – dafür ist die Kurve verrauscht.

## 6. Vergleich mit scikit-learn
"""),
    code("""
from sklearn.linear_model import LinearRegression, SGDRegressor

lin = LinearRegression().fit(x.reshape(-1, 1), y)
sgd = SGDRegressor(max_iter=1000, tol=1e-6, random_state=0).fit(x.reshape(-1, 1), y)
print("LinearRegression:", lin.coef_[0], lin.intercept_)
print("SGDRegressor:    ", sgd.coef_[0], sgd.intercept_[0])
print("unser GD:        ", w, b)
"""),
])

# ---------------------------------------------------------------------------
NB06 = ("06_projekt_regression", "Mini-Projekt 1: Regression von Hand", [
    md("""
Aufgabenbeschreibung und Erfolgskriterien findest du auf der Projektseite der Kurs-Website.
Ziel: eine lineare Regression mit Gradientenabstieg **nur mit NumPy** – und am Ende derselbe Test-Fehler wie scikit-learn.
"""),
    SETUP,
    code("""
from sklearn.datasets import load_diabetes

data = load_diabetes(scaled=False)
X, y = data.data, data.target
namen = data.feature_names
print(X.shape, y.shape)
print(namen)
"""),
    md("## Schritt 1: Erkunden"),
    code("""
# >>> Mittelwert und Standardabweichung jedes Features ausgeben
#! ...
for name, m, s in zip(namen, X.mean(axis=0), X.std(axis=0)):
    print(f"{name:4s}  Mittelwert {m:8.2f}   Std {s:7.2f}")
# <<<
# >>> Korrelation jedes Features mit y; das stärkste Feature bestimmen
#! korrelationen = ...
korrelationen = np.array([np.corrcoef(X[:, j], y)[0, 1] for j in range(X.shape[1])])
# <<<
j_best = np.argmax(np.abs(korrelationen))
print("stärkste Korrelation:", namen[j_best], round(korrelationen[j_best], 3))
plt.scatter(X[:, j_best], y, s=10); plt.xlabel(namen[j_best]); plt.ylabel("Krankheitsfortschritt"); plt.show()
"""),
    md("## Schritt 2: Aufteilen in Training und Test (80/20)"),
    code("""
# >>> zufällige Permutation mit Seed 42, die ersten 80 % sind Training
#! ...
idx = np.random.default_rng(42).permutation(len(y))
n_train = int(0.8 * len(y))
train_idx, test_idx = idx[:n_train], idx[n_train:]
# <<<
X_train, X_test, y_train, y_test = X[train_idx], X[test_idx], y[train_idx], y[test_idx]
print(X_train.shape, X_test.shape)
"""),
    md("""
## Schritt 3: Standardisieren

Mittelwert und Standardabweichung **nur aus den Trainingsdaten** – sonst fließt Information aus dem Test-Satz ins Training (*Data Leakage*).
"""),
    code("""
def standardisierer(X_train):
    # >>> Mittelwert und Std der Trainingsdaten berechnen und eine Transformationsfunktion zurückgeben
    #! ...
    mu, sd = X_train.mean(axis=0), X_train.std(axis=0)
    return lambda X: (X - mu) / sd
    # <<<

transform = standardisierer(X_train)
Z_train, Z_test = transform(X_train), transform(X_test)
print(np.round(Z_train.mean(axis=0), 6))
print(np.round(Z_train.std(axis=0), 6))
"""),
    md("## Schritt 4 und 5: Gradient implementieren und prüfen"),
    code("""
def vorhersage(X, w, b):
    return X @ w + b

def mse(X, y, w, b):
    return np.mean((vorhersage(X, w, b) - y) ** 2)

def mse_gradient(X, y, w, b):
    # >>> Gradienten nach w (Vektor) und b (Zahl)
    #! ...
    r = vorhersage(X, w, b) - y
    return 2 / len(y) * X.T @ r, 2 / len(y) * r.sum()
    # <<<

def num_gradient(X, y, w, b, h=1e-5):
    gw = np.zeros_like(w)
    for i in range(len(w)):
        e = np.zeros_like(w); e[i] = h
        gw[i] = (mse(X, y, w + e, b) - mse(X, y, w - e, b)) / (2 * h)
    gb = (mse(X, y, w, b + h) - mse(X, y, w, b - h)) / (2 * h)
    return gw, gb

w_test, b_test = rng.normal(size=X.shape[1]), 10.0
gw, gb = mse_gradient(Z_train, y_train, w_test, b_test)
gw_n, gb_n = num_gradient(Z_train, y_train, w_test, b_test)
print("relative Abweichung:", np.max(np.abs(gw - gw_n)) / np.max(np.abs(gw)), abs(gb - gb_n) / abs(gb))
"""),
    md("## Schritt 4 (Fortsetzung): Modell nur mit BMI"),
    code("""
def train(X, y, lr, epochen):
    w, b = np.zeros(X.shape[1]), 0.0
    verlauf = []
    for _ in range(epochen):
        # >>> ein Gradientenschritt, dann Verlust protokollieren
        #! ...
        gw, gb = mse_gradient(X, y, w, b)
        w, b = w - lr * gw, b - lr * gb
        verlauf.append(mse(X, y, w, b))
        # <<<
    return w, b, verlauf

j_bmi = namen.index("bmi")
w1, b1, _ = train(Z_train[:, [j_bmi]], y_train, lr=0.1, epochen=500)
plt.scatter(Z_train[:, j_bmi], y_train, s=10)
t = np.linspace(-2.5, 3.5, 2); plt.plot(t, w1[0] * t + b1, color="tab:orange")
plt.xlabel("BMI (standardisiert)"); plt.ylabel("y"); plt.show()
print("Test-MSE nur mit BMI:", mse(Z_test[:, [j_bmi]], y_test, w1, b1))
"""),
    md("## Schritt 6: Alle Features, verschiedene Lernraten"),
    code("""
with np.errstate(over="ignore", invalid="ignore"):   # η = 1.0 divergiert absichtlich
    for lr in [0.001, 0.01, 0.1, 1.0]:
        w, b, verlauf = train(Z_train, y_train, lr, epochen=500)
        verlauf = np.nan_to_num(verlauf, nan=1e9, posinf=1e9)   # divergierte Werte für den Plot kappen
        plt.plot(np.minimum(verlauf, 1e9), label=f"η = {lr}")
plt.yscale("log"); plt.ylim(2e3, 1e5); plt.xlabel("Epoche"); plt.ylabel("Trainings-MSE"); plt.legend(); plt.show()
"""),
    md("""
$\\eta = 1{,}0$ divergiert, obwohl bei einem einzelnen standardisierten Feature sogar Lernraten bis 1 funktionieren würden.
Die maximale stabile Lernrate hängt von der stärksten Krümmung der Verlustlandschaft ab: Einige Blutwerte (`s1`, `s2`) sind stark
miteinander korreliert, was die Landschaft in eine Richtung sehr steil macht. Hier liegt die Grenze bei etwa $\\eta \\approx 0{,}26$.

Wir trainieren das finale Modell mit $\\eta = 0{,}1$ und genügend Epochen.
"""),
    code("""
w_gd, b_gd, verlauf = train(Z_train, y_train, lr=0.1, epochen=20_000)
mse_test_gd = mse(Z_test, y_test, w_gd, b_gd)
baseline = np.mean((y_test - y_train.mean()) ** 2)
print(f"Test-MSE: {mse_test_gd:.1f}   Baseline (immer Mittelwert): {baseline:.1f}   R² = {1 - mse_test_gd / np.var(y_test):.3f}")
"""),
    md("## Schritt 7: Mini-Batch-Gradientenabstieg"),
    code("""
def train_minibatch(X, y, lr, epochen, batch=32, seed=0):
    r_gen = np.random.default_rng(seed)
    w, b = np.zeros(X.shape[1]), 0.0
    verlauf = []
    for _ in range(epochen):
        # >>> Daten mischen, in Batches durchgehen, auf jedem Batch einen Schritt machen
        #! ...
        idx = r_gen.permutation(len(y))
        for s in range(0, len(y), batch):
            sel = idx[s:s + batch]
            gw, gb = mse_gradient(X[sel], y[sel], w, b)
            w, b = w - lr * gw, b - lr * gb
        # <<<
        verlauf.append(mse(X, y, w, b))
    return w, b, verlauf

_, _, v_batch = train(Z_train, y_train, 0.1, 300)
w_mb, b_mb, v_mb = train_minibatch(Z_train, y_train, 0.01, 300)
plt.plot(v_batch, label="Batch-GD (η=0.1)"); plt.plot(v_mb, label="Mini-Batch 32 (η=0.01)")
plt.yscale("log"); plt.xlabel("Epoche"); plt.ylabel("Trainings-MSE"); plt.legend(); plt.show()
"""),
    md("## Schritt 8: Vergleich mit scikit-learn"),
    code("""
from sklearn.linear_model import LinearRegression

sk = LinearRegression().fit(Z_train, y_train)
mse_test_sk = np.mean((sk.predict(Z_test) - y_test) ** 2)
print(f"{'Feature':6s} {'unser GD':>10s} {'sklearn':>10s}")
for name, a, c in zip(namen, w_gd, sk.coef_):
    print(f"{name:6s} {a:10.3f} {c:10.3f}")
print(f"Bias   {b_gd:10.3f} {sk.intercept_:10.3f}")
print(f"Test-MSE: unser {mse_test_gd:.2f}  sklearn {mse_test_sk:.2f}")
print("max. relative Abweichung der Gewichte:", np.max(np.abs(w_gd - sk.coef_) / np.abs(sk.coef_)))
"""),
    md("## Schritt 9: Ohne Standardisierung"),
    code("""
# >>> Trainiere auf den unskalierten X_train mit verschiedenen Lernraten (200 Epochen) und gib den letzten Verlust aus
#! ...
with np.errstate(over="ignore", invalid="ignore"):
    for lr in [1e-1, 1e-3, 1e-5, 1e-6]:
        _, _, v = train(X_train, y_train, lr, 200)
        print(f"η = {lr:g}: letzter Trainings-MSE = {v[-1]:.4g}")
# <<<
"""),
    md("""
Ohne Skalierung reichen die Features von ca. 1 (Geschlecht) bis über 200 (Cholesterin). Die Verlustlandschaft ist extrem langgezogen:
Für die großen Features ist sie so steil, dass nur winzige Lernraten stabil sind – und mit denen kommt man in den flachen Richtungen kaum voran.

## Schritt 10: Deuten
"""),
    code("""
# >>> Die drei Features mit den betragsmäßig größten Gewichten (standardisiert) ausgeben
#! ...
for j in np.argsort(-np.abs(w_gd))[:3]:
    print(f"{namen[j]:4s} {w_gd[j]:8.2f}")
# <<<
"""),
    md("""
Bei standardisierten Features bedeutet ein Gewicht: "Wie stark ändert sich die Vorhersage, wenn dieses Feature um eine Standardabweichung steigt?"
Damit sind Gewichte vergleichbar. Bei unskalierten Features hängt das Gewicht von der Einheit ab (mg/dl oder g/l?) und ist nicht vergleichbar.

**Vorsicht:** Bei stark korrelierten Features (hier `s1` und `s2`) können sich große Gewichte mit entgegengesetztem Vorzeichen gegenseitig aufheben.
Dieses Problem heißt **Multikollinearität** – Regularisierung (Ridge, Modul 3) hilft dagegen.
"""),
])

NOTEBOOKS = [NB01, NB02, NB03, NB04, NB05, NB06]
