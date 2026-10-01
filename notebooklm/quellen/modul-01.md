# Modul 1 – Grundlagen & Mathe

Kursmaterial aus „Machine Learning – von vorne bis hinten“.

## Was ist Machine Learning?

Bevor wir rechnen: Was heißt es überhaupt, dass ein Computer „lernt“? In dieser Lektion baust du das Grundvokabular auf,
 das in jeder weiteren Lektion vorkommt.

### Lernziele
> Du kannst erklären, wie sich Machine Learning vom klassischen Programmieren unterscheidet. Du kennst die Begriffe Feature, Label, Modell, Parameter, Hyperparameter, Training und Inferenz. Du unterscheidest überwachtes, unüberwachtes und bestärkendes Lernen sowie Klassifikation und Regression. Du kennst die Schritte eines typischen ML-Projekts.

### Regeln schreiben oder Regeln lernen?

Ein klassisches Programm ist eine Liste von Regeln, die ein Mensch aufgeschrieben hat. Das klappt hervorragend, solange wir die Regeln kennen:
 Steuern berechnen, eine Datei sortieren, einen Warenkorb summieren.

Für viele interessante Probleme kennen wir die Regeln aber nicht. Niemand kann aufschreiben, welche Pixelmuster eine Katze ausmachen,
 oder welche Kombination aus 200 Kundenmerkmalen eine Kündigung ankündigt. Machine Learning dreht den Spieß um:

> **Definition**
> Machine Learning ist das Gebiet, in dem Computer aus Daten lernen, eine Aufgabe zu lösen, statt explizit dafür programmiert zu werden. Etwas formaler (Tom Mitchell, 1997): Ein Programm lernt aus Erfahrung \(E\) bezüglich einer Aufgabe \(T\) und eines Leistungsmaßes \(P\), wenn seine an \(P\) gemessene Leistung bei \(T\) mit der Erfahrung \(E\) steigt.

Beim Spam-Filter ist \(T\) „E-Mails als Spam oder Nicht-Spam einordnen“, \(E\) sind tausende E-Mails, die Menschen bereits markiert haben,
 und \(P\) ist zum Beispiel der Anteil korrekt eingeordneter Mails.

### Das Grundvokabular

Stell dir eine Tabelle mit Wohnungen vor. Jede Zeile ist ein Beispiel, jede Spalte eine Eigenschaft:

| Wohnfläche (m²) | Zimmer | Baujahr | Stadtteil | Preis (T€) |
|---|---|---|---|---|
| 54 | 2 | 1985 | Nord | 210 |
| 78 | 3 | 2010 | Mitte | 395 |
| 120 | 5 | 1962 | Süd | 480 |
| 66 | 2 | 2021 | Mitte | ? |

| Begriff | Bedeutung | Im Beispiel |
|---|---|---|
| **Beispiel / Datenpunkt** (sample) | eine Zeile der Tabelle | eine Wohnung |
| **Merkmal** (feature), \(x\) | eine Eingabegröße | Fläche, Zimmer, Baujahr, Stadtteil |
| **Zielgröße / Label** (target), \(y\) | was vorhergesagt werden soll | Preis |
| **Modell**, \(f\) | eine Funktion \(\hat y = f(x)\), die aus Features eine Vorhersage macht | „Preis ≈ 3,1 · Fläche + …“ |
| **Parameter** | Zahlen im Modell, die beim Training gelernt werden | der Faktor 3,1 |
| **Hyperparameter** | Einstellungen, die du vor dem Training wählst | Lernrate, Baumtiefe, k bei kNN |
| **Training** (fit) | Parameter so anpassen, dass das Modell die Daten gut erklärt | aus den bekannten Preisen lernen |
| **Inferenz** (predict) | das fertige Modell auf neue Daten anwenden | Preis der letzten Wohnung schätzen |

Das Dach über \(\hat y\) („y-Dach“) bedeutet immer: geschätzt / vorhergesagt. \(y\) ist der wahre Wert, \(\hat y\) die Vorhersage des Modells.
 Den ganzen Datensatz schreibt man als Matrix \(X\) (eine Zeile pro Beispiel, eine Spalte pro Feature) und die Labels als Vektor \(y\).
 Genau diese Schreibweise benutzt auch scikit-learn: `model.fit(X, y)`, `model.predict(X_neu)`.

### Lernen aus Beispielen – zum Ausprobieren

Hier siehst du ein echtes, wenn auch sehr einfaches Lernverfahren: **k-Nächste-Nachbarn**. Für jeden Ort im Feld schaut es nach,
 welche Klasse die \(k\) nächstgelegenen Trainingspunkte haben, und übernimmt die Mehrheit. Füge Punkte hinzu und beobachte, wie sich die
 Entscheidungsgrenze verändert. Setze auch einen „falschen“ Punkt mitten in die andere Klasse und vergleiche \(k=1\) mit \(k=7\).

> **Beobachtung**
> Bei \(k = 1\) folgt das Modell jedem einzelnen Punkt, auch einem Ausreißer – es überanpasst ( Overfitting ). Bei großem \(k\) wird die Grenze glatter, kann aber feine Strukturen übersehen ( Underfitting ). \(k\) ist ein Hyperparameter : Das Verfahren lernt ihn nicht selbst, du musst ihn wählen. Diesem Spannungsfeld begegnen wir im ganzen Kurs wieder.

### Die drei großen Lernarten

| Lernart | Daten | Ziel | Beispiele (im Kurs) |
|---|---|---|---|
| **Überwacht** | Features + Labels | Abbildung \(x \mapsto y\) lernen | Regression, Logistische Regression, Bäume, Gradient Boosting, SVM, neuronale Netze |
| **Unüberwacht** | nur Features | Struktur finden | k-Means, DBSCAN, PCA, Isolation Forest |
| **Bestärkend** | Belohnungssignal durch Interaktion | Strategie (Policy) lernen | Q-Learning, Policy Gradients |

Dazwischen gibt es Mischformen: **Semi-überwachtes Lernen** (wenige Labels, viele ungelabelte Daten) und **selbstüberwachtes Lernen**
 (self-supervised), bei dem die Labels aus den Daten selbst erzeugt werden – so werden große Sprachmodelle vortrainiert:
 Sie lernen, das jeweils nächste Wort eines Textes vorherzusagen.

#### Klassifikation vs. Regression

Innerhalb des überwachten Lernens unterscheidet man nach der Art des Labels:

- **Regression:** \(y\) ist eine Zahl auf einer kontinuierlichen Skala – Preis, Temperatur, Nachfrage.
- **Klassifikation:** \(y\) ist eine Kategorie – Spam/kein Spam (binär), Ziffer 0–9 (mehrere Klassen).

> **Typische Falle**
> Eine Zahl als Label heißt nicht automatisch Regression. Postleitzahlen oder Produkt-IDs sind Zahlen, aber Kategorien – es gibt kein sinnvolles „Dazwischen“. Umgekehrt wird ein Wert mit klarer Ordnung (Schulnote 1–6) manchmal sinnvoll als Regression behandelt.

### Wie ein ML-Projekt abläuft

1. **Problem formulieren:** Was genau soll vorhergesagt werden, und woran misst man Erfolg? Gibt es eine einfache Basislösung (Baseline)?
2. **Daten sammeln und verstehen:** Explorative Analyse, Verteilungen, fehlende Werte, Ausreißer.
3. **Daten vorbereiten:** Bereinigen, Features bauen, kategoriale Werte kodieren, skalieren.
4. **Daten aufteilen:** Trainings-, Validierungs- und Testdaten – der Test-Satz bleibt bis zum Schluss unangetastet.
5. **Modelle trainieren und vergleichen:** mit Kreuzvalidierung und Hyperparameter-Suche.
6. **Evaluieren:** einmalig auf dem Test-Satz, Fehleranalyse.
7. **Ausliefern und überwachen:** Das Modell läuft in der echten Welt; Daten verändern sich (Data Drift).

Die Schritte 2–6 übst du ab Modul 2 ausführlich mit scikit-learn. Die wichtigste Regel vorweg: **Ein Modell wird immer an Daten bewertet,
 die es beim Training nicht gesehen hat.** Sonst misst du nur, wie gut es auswendig gelernt hat.

### Werkzeuge in diesem Kurs

| Bibliothek | Wofür |
|---|---|
| `numpy` | Rechnen mit Vektoren und Matrizen – die Basis von allem |
| `pandas` | Tabellen laden, säubern, untersuchen |
| `matplotlib` | Diagramme |
| `scikit-learn` | Klassisches ML: fast jedes Modell mit derselben `fit`/`predict`-Schnittstelle |
| `PyTorch` | Neuronale Netze und Deep Learning (ab Modul 9) |

In Modul 1 implementieren wir vieles bewusst selbst mit NumPy. Wenn du später `LinearRegression().fit(X, y)` aufrufst, weißt du dann genau, was darin passiert.

## Vektoren, Matrizen & Daten

Jeder Datenpunkt ist ein Vektor, jeder Datensatz eine Matrix, und fast jedes Modell besteht im Kern aus Skalarprodukten und
 Matrixmultiplikationen. Lineare Algebra ist die Sprache des Machine Learning.

### Lernziele
> Du siehst Datenpunkte als Vektoren und Datensätze als Matrizen. Du kannst Skalarprodukt, Länge (Norm) und Distanz berechnen und geometrisch deuten. Du verstehst Matrix-Vektor- und Matrix-Matrix-Multiplikation – und warum ein lineares Modell \(\hat y = Xw + b\) ist. Du kannst all das in NumPy vektorisiert ausdrücken.

### Datenpunkte sind Vektoren

Eine Wohnung mit 78 m², 3 Zimmern und Baujahr 2010 ist für das Modell einfach eine Liste von Zahlen – ein **Vektor**:

\[ x = \begin{pmatrix} 78 \\ 3 \\ 2010 \end{pmatrix} \in \mathbb{R}^3 \]

Die Anzahl der Features ist die **Dimension**. Zwei Features kann man als Punkt in der Ebene zeichnen, drei im Raum.
 Echte Datensätze haben oft Hunderte oder Millionen Dimensionen – vorstellen kann man sich das nicht mehr, aber die Rechenregeln bleiben exakt dieselben.
 Deshalb üben wir die Intuition in 2D.

Stapeln wir \(n\) Datenpunkte als Zeilen übereinander, erhalten wir die **Datenmatrix** \(X\) mit \(n\) Zeilen und \(d\) Spalten
 (\(X \in \mathbb{R}^{n \times d}\)). In NumPy: `X.shape == (n, d)`.

### Die wichtigsten Rechenoperationen

#### Addition und Skalierung

Vektoren addiert man komponentenweise, und eine Multiplikation mit einer Zahl (einem **Skalar**) streckt einen Vektor:

\[ \begin{pmatrix} 1 \\ 2 \end{pmatrix} + \begin{pmatrix} 3 \\ -1 \end{pmatrix} = \begin{pmatrix} 4 \\ 1 \end{pmatrix}, \qquad 2 \cdot \begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 2 \\ 4 \end{pmatrix} \]

Genau das passiert in jedem Schritt des Gradientenabstiegs (Lektion 5): neue Parameter = alte Parameter − Lernrate · Gradient.

#### Das Skalarprodukt

Das **Skalarprodukt** (dot product) zweier Vektoren multipliziert die Komponenten paarweise und summiert:

\[ a \cdot b = \sum_{i=1}^{d} a_i b_i = a_1 b_1 + a_2 b_2 + \dots + a_d b_d \]

Geometrisch gilt \(a \cdot b = \lVert a \rVert \, \lVert b \rVert \cos\theta\), wobei \(\theta\) der Winkel zwischen den Vektoren ist. Daraus folgt:

- \(a \cdot b > 0\): die Vektoren zeigen in ähnliche Richtung
- \(a \cdot b = 0\): sie stehen senkrecht (**orthogonal**)
- \(a \cdot b < 0\): sie zeigen in entgegengesetzte Richtungen

Die grüne Strecke ist die **Projektion** von \(b\) auf \(a\): der „Schatten“ von \(b\) in Richtung \(a\). Ihre Länge ist \(\frac{a \cdot b}{\lVert a \rVert}\).

> **Warum das im ML überall ist**
> Ein lineares Modell berechnet \(\hat y = w \cdot x + b\): ein Skalarprodukt aus Gewichten und Features. Ein Neuron in einem neuronalen Netz tut dasselbe und wendet danach eine Aktivierungsfunktion an. Die Kosinus-Ähnlichkeit \(\cos\theta = \frac{a \cdot b}{\lVert a \rVert \lVert b \rVert}\) vergleicht Texte, Bilder und Embeddings – z. B. in Suchmaschinen und RAG-Systemen. Der Attention-Mechanismus in Transformern besteht im Kern aus Skalarprodukten zwischen „Queries“ und „Keys“.

#### Länge und Distanz

Die **euklidische Norm** (Länge) eines Vektors ist \(\lVert x \rVert_2 = \sqrt{x \cdot x} = \sqrt{x_1^2 + \dots + x_d^2}\).
 Die Distanz zweier Punkte ist die Länge ihres Differenzvektors. Je nach Anwendung nutzt man verschiedene Distanzmaße:

\[ d_2(p, q) = \sqrt{\sum_i (p_i - q_i)^2} \quad\text{(euklidisch, L2)}, \qquad d_1(p, q) = \sum_i |p_i - q_i| \quad\text{(Manhattan, L1)} \]

> **Achtung: Skalierung**
> Distanzen hängen stark von den Einheiten ab. Misst ein Feature die Fläche in m² (Werte um 100) und ein anderes die Zimmerzahl (Werte um 3), dominiert die Fläche jede Distanz. Distanzbasierte Verfahren wie kNN, k-Means oder SVM brauchen deshalb fast immer skalierte Features (z. B. StandardScaler in scikit-learn – Modul 2). L1 und L2 tauchen außerdem als Regularisierung wieder auf (Lasso und Ridge, Modul 3).

### Matrizen

#### Matrix mal Vektor

Eine Matrix \(A \in \mathbb{R}^{m \times d}\) mal ein Vektor \(x \in \mathbb{R}^d\) ergibt einen Vektor in \(\mathbb{R}^m\).
 Jeder Eintrag des Ergebnisses ist das Skalarprodukt einer **Zeile** von \(A\) mit \(x\):

\[ \begin{pmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{pmatrix} \begin{pmatrix} 10 \\ 1 \end{pmatrix} = \begin{pmatrix} 1\cdot 10 + 2 \cdot 1 \\ 3 \cdot 10 + 4 \cdot 1 \\ 5\cdot 10 + 6 \cdot 1 \end{pmatrix} = \begin{pmatrix} 12 \\ 34 \\ 56 \end{pmatrix} \]

Und das ist der Grund, warum Matrizen im ML so praktisch sind: Ist \(X\) die Datenmatrix und \(w\) der Gewichtsvektor eines linearen Modells,
 dann berechnet **eine einzige** Matrix-Vektor-Multiplikation die Vorhersagen für alle Datenpunkte gleichzeitig:

\[ \hat y = X w + b \qquad (\hat y \in \mathbb{R}^n) \]

#### Matrizen als Abbildungen

Man kann eine Matrix auch als Funktion sehen, die den Raum verformt: dreht, streckt, schert oder spiegelt.
 Die Spalten der Matrix sagen, wohin die Einheitsvektoren \(\hat\imath = (1, 0)\) und \(\hat\jmath = (0, 1)\) wandern.
 Die **Determinante** gibt an, um welchen Faktor sich Flächen ändern; ist sie 0, wird der Raum auf eine Linie „plattgedrückt“ und die Matrix ist nicht invertierbar.

Diese Sichtweise brauchst du später bei der **Hauptkomponentenanalyse** (PCA, Modul 7) und bei neuronalen Netzen: Jede Schicht ist eine solche
 lineare Abbildung, gefolgt von einer nichtlinearen Funktion.

#### Matrix mal Matrix, Transponieren, Inverse

- **Matrixprodukt:** \((AB)_{ij}\) ist das Skalarprodukt der \(i\)-ten Zeile von \(A\) mit der \(j\)-ten Spalte von \(B\).
 Dafür muss die Spaltenzahl von \(A\) der Zeilenzahl von \(B\) entsprechen: \((m \times k)(k \times n) = (m \times n)\).
 Achtung: Im Allgemeinen ist \(AB \neq BA\).
- **Transponierte** \(A^\top\): Zeilen werden zu Spalten. \(X^\top X\) ist eine \(d \times d\)-Matrix, die in der linearen Regression auftaucht.
- **Inverse** \(A^{-1}\): macht eine Abbildung rückgängig, \(A^{-1} A = I\). Existiert nur für quadratische Matrizen mit \(\det A \neq 0\).

> **Ausblick: die Normalengleichung**
> Für die lineare Regression gibt es eine geschlossene Lösung: \(w^* = (X^\top X)^{-1} X^\top y\). Sie nutzt genau die Operationen dieser Lektion. In der Praxis wird sie selten wörtlich so berechnet (numerisch instabil, teuer bei vielen Features) – eine Alternative ist der Gradientenabstieg aus Lektion 5.

### In NumPy: vektorisiert denken

```python
import numpy as np

X = np.array([[54, 2], [78, 3], [120, 5]])   # 3 Wohnungen, 2 Features → shape (3, 2)
w = np.array([3.0, 10.0])                    # Gewichte
b = 20.0

y_hat = X @ w + b          # Matrix-Vektor-Produkt: alle Vorhersagen auf einmal
a, c = X[0], X[1]
a @ c                      # Skalarprodukt  (auch: np.dot(a, c))
np.linalg.norm(a - c)      # euklidische Distanz
X.T @ X                    # (2, 3) @ (3, 2) → (2, 2)
```

Schleifen über Datenpunkte (`for i in range(n)`) sind in Python langsam. NumPy-Operationen laufen in optimiertem C-Code
 und sind oft 100× schneller. **Vektorisieren** heißt: Formuliere die Rechnung mit ganzen Vektoren und Matrizen statt mit Schleifen.

> **Broadcasting**
> In X @ w + b ist X @ w ein Vektor mit 3 Einträgen, b eine einzelne Zahl. NumPy „verteilt“ b automatisch auf alle Einträge. Ebenso funktioniert X - X.mean(axis=0) : Von jeder Zeile wird der Spalten-Mittelwertvektor abgezogen.

## Statistik & Wahrscheinlichkeit

Daten sind verrauscht, Vorhersagen unsicher. Statistik gibt uns Werkzeuge, um Daten zu beschreiben, und Wahrscheinlichkeitsrechnung die Sprache,
 um über Unsicherheit zu reden. Beides steckt in jedem Modell – von Naive Bayes bis zum Sprachmodell, das das wahrscheinlichste nächste Wort wählt.

### Lernziele
> Du kannst Mittelwert, Median, Varianz und Standardabweichung berechnen und deuten. Du verstehst Verteilungen, insbesondere die Normalverteilung, und den Zentralen Grenzwertsatz. Du rechnest mit bedingten Wahrscheinlichkeiten und dem Satz von Bayes. Du kennst Korrelation, Kovarianz – und warum Korrelation keine Kausalität ist. Du verstehst die Idee der Maximum-Likelihood-Schätzung.

### Daten beschreiben: Lage und Streuung

Für Werte \(x_1, \dots, x_n\) sind die wichtigsten Kennzahlen:

\[ \bar x = \mu = \frac{1}{n}\sum_{i=1}^n x_i \qquad \sigma^2 = \frac{1}{n}\sum_{i=1}^n (x_i - \bar x)^2 \qquad \sigma = \sqrt{\sigma^2} \]

- **Mittelwert** \(\mu\) (mean): der Schwerpunkt der Daten.
- **Median**: der mittlere Wert nach dem Sortieren – robust gegen Ausreißer.
- **Varianz** \(\sigma^2\): mittlere quadrierte Abweichung vom Mittelwert. Die **Standardabweichung** \(\sigma\) hat dieselbe Einheit wie die Daten.

> **Probier es aus**
> Ziehe einen Punkt ganz nach rechts. Der Mittelwert wandert mit und die Streuung explodiert, während der Median kaum reagiert. Genau deshalb ist die Wahl der Fehlerfunktion wichtig: Der mittlere quadratische Fehler (Lektion 5) reagiert stark auf Ausreißer, der mittlere absolute Fehler viel weniger.

**Standardisieren:** Zieht man den Mittelwert ab und teilt durch die Standardabweichung, erhält man den **z-Score** \(z = \frac{x - \mu}{\sigma}\).
 Die neuen Werte haben Mittelwert 0 und Standardabweichung 1. Das ist exakt, was `StandardScaler` in scikit-learn tut, und ein
 \(|z| > 3\) ist eine einfache Regel zur Ausreißererkennung (Modul 8).

n oder n − 1?
 Schätzt man die Varianz einer ganzen Population aus einer Stichprobe, teilt man durch \(n-1\) statt \(n\) (Bessel-Korrektur), weil der Stichprobenmittelwert
 selbst geschätzt ist. NumPy nutzt standardmäßig \(n\) (`np.var(x)`), pandas \(n-1\) (`df.var()`). Bei großen Datensätzen ist der Unterschied vernachlässigbar.

### Wahrscheinlichkeit

Eine Wahrscheinlichkeit \(P(A) \in [0, 1]\) misst, wie sicher ein Ereignis \(A\) eintritt. Die wichtigsten Regeln:

- **Gegenereignis:** \(P(\text{nicht } A) = 1 - P(A)\)
- **Bedingte Wahrscheinlichkeit:** \(P(A \mid B) = \frac{P(A \cap B)}{P(B)}\) – die Wahrscheinlichkeit von \(A\), wenn wir wissen, dass \(B\) eingetreten ist.
- **Unabhängigkeit:** \(A\) und \(B\) sind unabhängig, wenn \(P(A \cap B) = P(A)\,P(B)\), also \(P(A \mid B) = P(A)\).

#### Der Satz von Bayes

Aus der Definition der bedingten Wahrscheinlichkeit folgt eine der wichtigsten Formeln der Statistik:

\[ P(A \mid B) = \frac{P(B \mid A)\, P(A)}{P(B)} \]

Lies sie so: Unsere Überzeugung über \(A\) vor den Daten (**Prior** \(P(A)\)) wird mit der **Likelihood** \(P(B \mid A)\) der Beobachtung
 aktualisiert und ergibt die **Posterior** \(P(A \mid B)\). Das klassische Beispiel ist ein medizinischer Test:

Bei einer seltenen Krankheit (1 %) und einem Test, der 95 % der Kranken erkennt (**Sensitivität**) und 95 % der Gesunden korrekt negativ testet (**Spezifität**),
 ist man bei positivem Test nur zu etwa 16 % wirklich krank! Es gibt einfach viel mehr Gesunde, von denen 5 % falsch positiv sind.

\[ P(\text{krank} \mid +) = \frac{0{,}95 \cdot 0{,}01}{0{,}95 \cdot 0{,}01 + 0{,}05 \cdot 0{,}99} \approx 0{,}16 \]

> **Bezug zum ML**
> Genau dieses Phänomen trifft dich bei unbalancierten Daten : Ein Betrugserkennungs-Modell mit 99 % Genauigkeit kann nutzlos sein, wenn nur 0,1 % der Transaktionen Betrug sind. In Modul 2 lernst du dafür Precision und Recall – Precision ist genau die Größe \(P(\text{wirklich positiv} \mid \text{vorhergesagt positiv})\), die wir hier berechnet haben. Der Klassifikator Naive Bayes (Modul 4) wendet den Satz von Bayes direkt an.

### Zufallsvariablen und Verteilungen

Eine **Zufallsvariable** \(X\) ordnet jedem Ausgang eines Zufallsexperiments eine Zahl zu. Ihre **Verteilung** beschreibt, welche Werte wie wahrscheinlich sind.

- **Diskret** (endlich/abzählbar viele Werte): Würfel, Anzahl Klicks. Beschrieben durch \(P(X = k)\). Wichtige Beispiele: Bernoulli (Münzwurf), Binomial, Poisson.
- **Stetig** (kontinuierlich): Körpergröße, Messfehler. Beschrieben durch eine **Dichte** \(p(x)\); Wahrscheinlichkeiten sind Flächen unter der Dichte.

Der **Erwartungswert** \(\mathbb{E}[X]\) ist der langfristige Durchschnitt, die Varianz \(\mathrm{Var}(X) = \mathbb{E}[(X - \mathbb{E}[X])^2]\) die erwartete quadrierte Abweichung.

#### Die Normalverteilung

Die bekannteste stetige Verteilung ist die **Normalverteilung** (Gauß-Verteilung) \(\mathcal{N}(\mu, \sigma^2)\):

\[ p(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right) \]

Faustregel (68-95-99,7): Etwa 68 % der Werte liegen innerhalb von \(\mu \pm \sigma\), 95 % innerhalb \(\mu \pm 2\sigma\), 99,7 % innerhalb \(\mu \pm 3\sigma\).

#### Warum ist die Normalverteilung überall? Der Zentrale Grenzwertsatz

Summiert oder mittelt man viele unabhängige Zufallsgrößen, ist das Ergebnis annähernd normalverteilt – egal, wie die einzelnen Größen verteilt sind.
 Ein einzelner Würfel ist gleichverteilt, aber der Mittelwert aus 10 Würfeln sieht schon wie eine Glocke aus:

Achte auf die Breite: Die Standardabweichung des Mittelwerts schrumpft mit \(\sigma / \sqrt{n}\). Mehr Daten → genauere Schätzungen.
 Weil Messfehler oft Summen vieler kleiner Einflüsse sind, nimmt man sie häufig als normalverteilt an. Daraus folgt (siehe unten), dass der mittlere quadratische Fehler die „natürliche“ Fehlerfunktion für Regression ist.

### Zusammenhänge: Kovarianz und Korrelation

Die **Kovarianz** misst, ob zwei Größen gemeinsam steigen und fallen:

\[ \mathrm{Cov}(X, Y) = \frac{1}{n}\sum_{i=1}^n (x_i - \bar x)(y_i - \bar y) \]

Ihr Betrag hängt von den Einheiten ab. Normiert man mit den Standardabweichungen, erhält man den **Korrelationskoeffizienten** nach Pearson,
 \(r = \frac{\mathrm{Cov}(X,Y)}{\sigma_X \sigma_Y} \in [-1, 1]\). Er misst nur lineare Zusammenhänge: Bei \(y = x^2\) auf symmetrischen Daten ist \(r \approx 0\), obwohl \(y\) vollständig von \(x\) abhängt.

Fasst man alle paarweisen Kovarianzen der Features zusammen, entsteht die **Kovarianzmatrix** \(\Sigma = \frac{1}{n} X_c^\top X_c\) (mit zentriertem \(X_c\)) –
 die Grundlage der PCA in Modul 7.

> **Korrelation ≠ Kausalität**
> Eisverkäufe und Sonnenbrände korrelieren stark – nicht weil Eis Sonnenbrand verursacht, sondern weil beide vom Wetter abhängen (eine Störvariable ). ML-Modelle lernen Korrelationen. Für Vorhersagen reicht das oft, für Entscheidungen („Was passiert, wenn wir X ändern?“) nicht.

### Maximum Likelihood: Wie Modelle aus Daten Parameter schätzen

Angenommen, die Daten stammen aus einer Verteilung mit unbekanntem Parameter \(\theta\). Die **Likelihood** \(L(\theta) = \prod_i p(x_i \mid \theta)\)
 sagt, wie wahrscheinlich die beobachteten Daten unter \(\theta\) sind. Die **Maximum-Likelihood-Schätzung** (MLE) wählt das \(\theta\), das die Daten am wahrscheinlichsten macht.
 Weil Produkte vieler kleiner Zahlen unhandlich sind, maximiert man den Logarithmus (die **Log-Likelihood**) – bzw. minimiert die negative Log-Likelihood.

> **Zwei Ergebnisse, die du wiedersehen wirst**
> Nimmt man an, dass \(y = f(x) + \varepsilon\) mit normalverteiltem Rauschen \(\varepsilon \sim \mathcal{N}(0, \sigma^2)\), dann ist Maximum Likelihood dasselbe wie die Minimierung des mittleren quadratischen Fehlers – denn \(-\log p(y \mid x) = \frac{(y - f(x))^2}{2\sigma^2} + \text{const}\). Bei binären Labels (Bernoulli-Verteilung) wird die negative Log-Likelihood zur Kreuzentropie ( Log Loss ), der Verlustfunktion der logistischen Regression und der meisten neuronalen Klassifikatoren.

Verlustfunktionen sind also nicht willkürlich, sondern folgen aus Annahmen über das Rauschen in den Daten. Wie man sie dann tatsächlich minimiert, zeigen die nächsten zwei Lektionen.

## Ableitungen & Gradienten

Ein Modell zu trainieren heißt, seine Parameter so einzustellen, dass der Fehler möglichst klein wird. Dafür müssen wir wissen,
 in welche Richtung wir jeden Parameter ändern sollen. Genau das sagt uns die Ableitung – und bei vielen Parametern der Gradient.

### Lernziele
> Du verstehst die Ableitung als lokale Steigung und kannst einfache Ableitungen berechnen. Du kannst partielle Ableitungen bilden und den Gradienten als Vektor deuten. Du wendest die Kettenregel an und siehst darin das Prinzip von Backpropagation. Du kannst Ableitungen numerisch überprüfen.

### Die Ableitung: Steigung in einem Punkt

Die Steigung einer Geraden durch zwei Punkte kennst du: „Höhenunterschied durch Abstand“. Für eine Kurve legen wir eine **Sekante** durch
 \(x\) und \(x + h\) und lassen \(h\) immer kleiner werden. Im Grenzfall wird die Sekante zur **Tangente**, ihre Steigung ist die **Ableitung**:

\[ f'(x) = \frac{df}{dx} = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h} \]

Die Ableitung sagt uns, wie stark und in welche Richtung sich \(f\) ändert, wenn wir \(x\) ein winziges Stück erhöhen:

- \(f'(x) > 0\): Die Funktion steigt – um \(f\) zu verkleinern, müssen wir \(x\) **verringern**.
- \(f'(x) < 0\): Die Funktion fällt – wir müssen \(x\) **vergrößern**.
- \(f'(x) = 0\): flache Stelle – ein Minimum, ein Maximum oder ein Sattelpunkt.

> **Die Kernidee für alles Weitere**
> Willst du \(f\) verkleinern, gehe einen kleinen Schritt gegen das Vorzeichen der Ableitung: \(x \leftarrow x - \eta\, f'(x)\). Das ist bereits der Gradientenabstieg – Lektion 5 baut darauf auf.

#### Die Ableitungsregeln, die du brauchst

| Funktion \(f(x)\) | Ableitung \(f'(x)\) | Wo im ML? |
|---|---|---|
| \(c\) (Konstante) | \(0\) | Bias-Terme in der Ableitung nach anderen Parametern |
| \(x^n\) | \(n\,x^{n-1}\) | quadratischer Fehler: \((\ldots)^2 \to 2(\ldots)\) |
| \(e^x\) | \(e^x\) | Softmax, Sigmoid |
| \(\ln x\) | \(1/x\) | Log-Likelihood, Kreuzentropie |
| \(\sigma(x) = \frac{1}{1 + e^{-x}}\) | \(\sigma(x)(1 - \sigma(x))\) | logistische Regression, Neuronen |
| \(\max(0, x)\) (ReLU) | \(1\) für \(x > 0\), sonst \(0\) | die häufigste Aktivierung in Deep Learning |

Dazu die Rechenregeln: **Summenregel** \((f + g)' = f' + g'\), **Faktorregel** \((c f)' = c f'\), **Produktregel** \((fg)' = f'g + fg'\) und
 die wichtigste von allen, die **Kettenregel** (siehe unten).

### Mehrere Variablen: partielle Ableitungen

Modelle haben viele Parameter. Eine lineare Regression mit einem Feature hat schon zwei (\(w\) und \(b\)), ein großes Sprachmodell Milliarden.
 Der Fehler ist also eine Funktion vieler Variablen. Die **partielle Ableitung** \(\frac{\partial f}{\partial x}\) ist die Ableitung nach einer Variablen,
 während alle anderen als Konstanten behandelt werden:

\[ f(x, y) = x^2 + 3xy + y^3 \quad\Rightarrow\quad \frac{\partial f}{\partial x} = 2x + 3y, \qquad \frac{\partial f}{\partial y} = 3x + 3y^2 \]

#### Der Gradient

Schreibt man alle partiellen Ableitungen in einen Vektor, erhält man den **Gradienten**:

\[ \nabla f(x, y) = \begin{pmatrix} \partial f / \partial x \\ \partial f / \partial y \end{pmatrix} \]

Der Gradient hat eine wunderbare geometrische Bedeutung: Er zeigt in die Richtung des **steilsten Anstiegs**, seine Länge ist die Steigung in diese Richtung,
 und er steht senkrecht auf den Höhenlinien. \(-\nabla f\) zeigt folglich in Richtung des steilsten Abstiegs.

> **Warum steilster Anstieg?**
> Die Änderung von \(f\) bei einem kleinen Schritt \(\Delta\) ist näherungsweise \(\nabla f \cdot \Delta\) – ein Skalarprodukt (Lektion 2)! Bei fester Schrittlänge ist es am größten, wenn \(\Delta\) in dieselbe Richtung wie \(\nabla f\) zeigt (\(\cos\theta = 1\)), und null, wenn \(\Delta\) senkrecht dazu steht – also entlang einer Höhenlinie.

### Die Kettenregel

Modelle sind verschachtelte Funktionen: Ein neuronales Netz ist Schicht auf Schicht, eine Verlustfunktion wird auf die Ausgabe des Modells angewendet.
 Für verschachtelte Funktionen \(f(g(x))\) gilt:

\[ \frac{d}{dx} f(g(x)) = f'(g(x)) \cdot g'(x) \qquad\text{oder in Leibniz-Schreibweise}\qquad \frac{df}{dx} = \frac{df}{du} \cdot \frac{du}{dx} \text{ mit } u = g(x) \]

„Äußere Ableitung mal innere Ableitung.“ Am besten versteht man sie in einem **Rechengraphen**:

> **Das ist Backpropagation**
> Ein Rechengraph wird einmal vorwärts ausgewertet. Dann wandert die Ableitung rückwärts, und an jedem Knoten wird mit der lokalen Ableitung multipliziert. So bekommt man die Ableitung des Fehlers nach jedem Parameter in einem einzigen Rückwärtsdurchlauf – egal, wie viele Parameter es sind. PyTorch und TensorFlow machen das automatisch ( Automatic Differentiation ). In Modul 9 rechnen wir es einmal komplett von Hand durch.

#### Ein vollständiges ML-Beispiel

Das einfachste Modell: \(\hat y = w x + b\), und der quadratische Fehler für ein Beispiel \((x, y)\) ist \(L = (\hat y - y)^2\).
 Mit der Kettenregel (\(u = \hat y - y\), \(L = u^2\)):

\[ \frac{\partial L}{\partial w} = \underbrace{2(\hat y - y)}_{\partial L / \partial \hat y} \cdot \underbrace{x}_{\partial \hat y / \partial w}, \qquad
 \frac{\partial L}{\partial b} = 2(\hat y - y) \cdot 1 \]

Lies das in Worten: Ist die Vorhersage zu groß (\(\hat y > y\)), ist der Gradient nach \(b\) positiv – wir sollten \(b\) verkleinern.
 Der Gradient nach \(w\) wird zusätzlich mit \(x\) gewichtet: Beispiele mit großem \(x\) beeinflussen \(w\) stärker. Genau diese Formeln benutzen wir in der nächsten Lektion.

### Ableitungen numerisch prüfen

Selbst hergeleitete Ableitungen enthalten leicht Fehler. Ein einfacher Test ist die **zentrale Differenz** mit kleinem \(h\) (z. B. \(10^{-5}\)):

\[ f'(x) \approx \frac{f(x + h) - f(x - h)}{2h} \]

```python
def numerische_ableitung(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

f  = lambda x: x**3 - 2*x
df = lambda x: 3*x**2 - 2          # analytisch hergeleitet
print(df(1.5), numerische_ableitung(f, 1.5))   # 4.75  4.75000000...
```

Für einen Gradienten macht man das für jede Komponente einzeln (Gradient Checking). Zum Trainieren ist das viel zu langsam
 (zwei Funktionsauswertungen pro Parameter), aber zum Testen unschlagbar.

## Verlustfunktionen & Gradientenabstieg

Jetzt kommt alles zusammen: Vektoren beschreiben Daten und Parameter, Statistik liefert die Fehlerfunktion, und Ableitungen zeigen den Weg bergab.
 Der Gradientenabstieg ist der Algorithmus, mit dem praktisch jedes moderne Modell trainiert wird – von der logistischen Regression bis zu GPT.

### Lernziele
> Du kennst die wichtigsten Verlustfunktionen (MSE, MAE, Kreuzentropie) und weißt, wann man welche nimmt. Du verstehst den Gradientenabstieg und die Rolle der Lernrate. Du kannst Batch-, Stochastischen und Mini-Batch-Gradientenabstieg unterscheiden. Du kennst die typischen Probleme: lokale Minima, schlecht skalierte Features, Divergenz.

### Training = Optimierung

Ein Modell \(f_\theta\) hat Parameter \(\theta\) (bei der linearen Regression \(\theta = (w, b)\)). Eine **Verlustfunktion** \(L(\theta)\)
 (loss function, auch Kostenfunktion) misst, wie schlecht die Vorhersagen auf den Trainingsdaten sind. Training heißt:

\[ \theta^* = \arg\min_\theta L(\theta) \]

Also: Finde die Parameter mit dem kleinsten Verlust. Alles Weitere in dieser Lektion beantwortet zwei Fragen: **Was** minimieren wir? Und **wie**?

### Was minimieren wir? Verlustfunktionen

#### Für Regression

Die Differenz \(y_i - \hat y_i\) zwischen wahrem Wert und Vorhersage heißt **Residuum**. Die beiden wichtigsten Verluste mitteln die Residuen auf unterschiedliche Weise:

\[ \text{MSE} = \frac{1}{n}\sum_{i=1}^n (y_i - \hat y_i)^2 \qquad\qquad \text{MAE} = \frac{1}{n}\sum_{i=1}^n |y_i - \hat y_i| \]

Beim **mittleren quadratischen Fehler** (Mean Squared Error) ist der Name wörtlich zu nehmen – jedes Residuum spannt ein Quadrat auf,
 und wir minimieren deren durchschnittliche Fläche. Versuche, die Gerade so hinzulegen, dass die Quadrate möglichst klein werden:

|  | MSE | MAE |
|---|---|---|
| Ausreißer | werden stark bestraft (quadratisch) | werden nur linear bestraft – robuster |
| Ableitung | glatt: \(2(\hat y - y)\), wird klein nahe am Ziel | Knick bei 0, Betrag des Gradienten immer gleich |
| Statistische Bedeutung | optimal bei normalverteiltem Rauschen, schätzt den **Mittelwert** | schätzt den **Median** |

Eine Mischung aus beiden ist der **Huber-Loss**: quadratisch für kleine, linear für große Residuen. In scikit-learn findest du ihn z. B. in `HuberRegressor`
 und als `loss="huber"` beim Gradient Boosting (Modul 6).

#### Für Klassifikation

Gibt ein Modell eine Wahrscheinlichkeit \(p = P(y = 1 \mid x)\) aus, misst man den Fehler mit der **binären Kreuzentropie** (Log Loss):

\[ L = -\frac{1}{n}\sum_{i=1}^n \Big[ y_i \log p_i + (1 - y_i)\log(1 - p_i) \Big] \]

Ist das Label 1, zählt nur \(-\log p_i\): Bei \(p_i = 0{,}99\) fast kein Verlust, bei \(p_i = 0{,}01\) ein riesiger. Ein Modell, das sich sicher ist und falsch liegt, wird hart bestraft.
 Wie in Lektion 3 gezeigt, folgt die Kreuzentropie aus Maximum Likelihood – ebenso wie MSE. Sie ist die Verlustfunktion der logistischen Regression (Modul 3) und neuronaler Klassifikatoren.

> **Verlust ≠ Metrik**
> Die Verlustfunktion muss sich gut optimieren lassen (glatt, differenzierbar). Die Metrik , mit der du das Modell am Ende bewertest, darf etwas ganz anderes sein – z. B. Accuracy oder F1. Accuracy kann man nicht direkt mit Gradienten optimieren, weil sie stückweise konstant ist (Ableitung fast überall 0).

### Wie minimieren wir? Gradientenabstieg

Stell dir vor, du stehst nachts im Nebel auf einem Berg und willst ins Tal. Du siehst nichts, spürst aber die Neigung unter deinen Füßen.
 Die naheliegende Strategie: Mach einen Schritt in die Richtung, in die es am steilsten bergab geht, und wiederhole das. Das ist der **Gradientenabstieg**
 (Gradient Descent):

\[ \theta_{\text{neu}} = \theta - \eta \, \nabla_\theta L(\theta) \]

\(\eta\) („eta“) ist die **Lernrate** (learning rate): Sie bestimmt die Schrittgröße. Der Algorithmus komplett:

```python
θ = Startwert (zufällig oder 0)
wiederhole, bis der Verlust sich kaum noch ändert:
    g = Gradient von L an der Stelle θ
    θ = θ - η · g
```

#### Die Lernrate

Probiere in der Animation oben mit der Parabel \(f(x) = \tfrac12 x^2\) aus, was passiert:

- **Zu klein** (\(\eta = 0{,}05\)): Es geht sicher bergab, braucht aber sehr viele Schritte.
- **Gut** (\(\eta \approx 0{,}3 \ldots 1\)): schnelle Konvergenz. Bei \(\eta = 1\) landet man hier sogar in einem Schritt im Minimum.
- **Zu groß** (\(1 < \eta < 2\)): Man springt über das Minimum hinweg und pendelt hin und her.
- **Viel zu groß** (\(\eta > 2\)): Jeder Schritt landet höher als der vorherige – das Verfahren **divergiert**.

> **Warum genau 2?**
> Für \(f(x) = \tfrac12 x^2\) ist \(f'(x) = x\), also \(x_{\text{neu}} = x - \eta x = (1 - \eta)\,x\). Jeder Schritt multipliziert \(x\) mit \(1 - \eta\). Das schrumpft nur gegen 0, wenn \(|1 - \eta| < 1\), also \(0 < \eta < 2\). Bei einer steileren Parabel \(\tfrac{k}{2}x^2\) liegt die Grenze bei \(2/k\): Je stärker die Krümmung, desto kleiner muss die Lernrate sein.

Teste auch die Funktion mit zwei Tälern: Je nach Startpunkt landet der Gradientenabstieg in einem anderen **lokalen Minimum**. Er sieht nur die lokale Steigung,
 nie das ganze Gebirge. Bei der linearen Regression ist der Verlust allerdings **konvex** (eine einzige Schüssel) – dort gibt es nur ein Minimum.

#### In mehreren Dimensionen

Mit zwei Parametern wird die Verlustfunktion zu einer Landschaft. Ist das Tal in eine Richtung viel steiler als in die andere, passiert etwas Typisches:

Der Gradient zeigt senkrecht auf die Höhenlinien – und das ist in einem langgezogenen Tal nicht die Richtung zum Minimum. Der Pfad springt zwischen den
 steilen Talwänden hin und her, während er in der flachen Richtung nur langsam vorankommt. Und die steilste Richtung begrenzt die maximale Lernrate.

> **Praxis-Konsequenz: Features skalieren!**
> Langgezogene Täler entstehen vor allem, wenn Features sehr unterschiedliche Größenordnungen haben (Fläche in m² ≈ 100, Zimmer ≈ 3). Werden alle Features standardisiert (Mittelwert 0, Standardabweichung 1), wird die Landschaft runder und der Gradientenabstieg viel schneller. Moderne Optimierer wie Momentum und Adam (Modul 10) dämpfen das Zickzack zusätzlich, indem sie sich frühere Schritte merken.

### Alles zusammen: lineare Regression mit Gradientenabstieg

Für das Modell \(\hat y_i = w x_i + b\) und den MSE-Verlust ergeben sich mit der Kettenregel (Lektion 4) die Gradienten über alle \(n\) Beispiele:

\[ \frac{\partial L}{\partial w} = \frac{2}{n}\sum_{i=1}^n (\hat y_i - y_i)\, x_i \qquad \frac{\partial L}{\partial b} = \frac{2}{n}\sum_{i=1}^n (\hat y_i - y_i) \]

Beobachte, wie die Gerade links und der Punkt in der Verlustlandschaft rechts gemeinsam wandern. Jeder Punkt \((w, b)\) rechts entspricht genau einer Geraden links:

Vektorisiert mit NumPy sind das nur wenige Zeilen – und mit beliebig vielen Features (\(X\) als Matrix, \(w\) als Vektor) sieht der Code genauso aus:

```python
import numpy as np

def train(X, y, lr=0.03, epochs=2000):
    n, d = X.shape
    w, b = np.zeros(d), 0.0
    for epoch in range(epochs):
        y_hat = X @ w + b              # Vorhersagen für alle Beispiele
        err = y_hat - y                # Residuen (mit umgekehrtem Vorzeichen)
        grad_w = 2 / n * X.T @ err     # ∂L/∂w – ein Vektor mit d Einträgen
        grad_b = 2 / n * err.sum()     # ∂L/∂b
        w -= lr * grad_w
        b -= lr * grad_b
    return w, b
```

### Batch, stochastisch, Mini-Batch

Oben haben wir für jeden Schritt den Gradienten über alle Daten berechnet. Bei Millionen Datenpunkten ist das teuer. Die Varianten:

| Variante | Gradient pro Schritt aus … | Eigenschaften |
|---|---|---|
| **Batch-GD** | allen \(n\) Beispielen | exakter Gradient, glatter Pfad, aber langsam pro Schritt |
| **Stochastischer GD (SGD)** | einem zufälligen Beispiel | sehr schnelle, aber verrauschte Schritte; das Rauschen hilft manchmal, flache Stellen zu verlassen |
| **Mini-Batch-GD** | einer kleinen zufälligen Gruppe (z. B. 32–512) | der Standard in der Praxis: guter Kompromiss, ideal für GPUs |

Ein Durchlauf durch alle Trainingsdaten heißt **Epoche**. Im Deep Learning sagt man meist „SGD“, meint aber Mini-Batch-GD.
 In scikit-learn nutzen `SGDRegressor` und `SGDClassifier` stochastischen Gradientenabstieg; `LinearRegression` dagegen löst das Problem direkt
 (per Kleinste-Quadrate-Verfahren), ganz ohne Lernrate.

### Wann ist man fertig?

- **Feste Anzahl Epochen** – einfach, aber man muss eine gute Zahl kennen.
- **Konvergenzkriterium**: Abbruch, wenn sich der Verlust kaum noch ändert (`tol` in scikit-learn) oder der Gradient sehr klein ist.
- **Early Stopping**: Abbruch, wenn der Fehler auf separaten Validierungsdaten wieder steigt – ein wirksamer Schutz gegen Overfitting (Modul 2 und 10).

Zeichne immer die **Lernkurve** (Verlust über Epochen). Fällt sie nicht, ist die Lernrate zu klein oder es gibt einen Bug; springt sie oder steigt sie,
 ist die Lernrate zu groß. Das übst du im Mini-Projekt.

## 🛠 Mini-Projekt: Regression von Hand

Du baust eine lineare Regression mit Gradientenabstieg komplett selbst – nur mit NumPy – und trainierst sie auf einem echten medizinischen Datensatz.
 Am Ende vergleichst du dein Modell mit scikit-learn. Wenn deine Zahlen übereinstimmen, hast du Modul 1 wirklich verstanden.

### Was du anwendest
> Daten als Matrix \(X\) und Vektor \(y\), vektorisierte Vorhersage \(\hat y = Xw + b\) (Lektion 2) Standardisierung mit Mittelwert und Standardabweichung (Lektion 3) Gradienten des MSE über die Kettenregel, geprüft mit numerischen Ableitungen (Lektion 4) Gradientenabstieg, Lernrate, Lernkurven, Mini-Batches (Lektion 5)

### Der Datensatz

Der **Diabetes-Datensatz** ist in scikit-learn enthalten (kein Download nötig): 442 Patientinnen und Patienten, 10 Merkmale
 (Alter, Geschlecht, BMI, Blutdruck und sechs Blutwerte) und als Zielgröße ein Maß für das Fortschreiten der Krankheit ein Jahr später.

```python
from sklearn.datasets import load_diabetes
X, y = load_diabetes(return_X_y=True, scaled=False)   # X.shape == (442, 10)
```

### Aufgaben

1. **Erkunden:** Berechne Mittelwert und Standardabweichung jedes Features. Welches Feature korreliert am stärksten mit \(y\)? Zeichne ein Streudiagramm.
2. **Aufteilen:** Teile die Daten zufällig in 80 % Training und 20 % Test – mit NumPy (`np.random.default_rng(42).permutation`), ohne scikit-learn.
3. **Standardisieren:** Schreibe eine Funktion, die Mittelwert und Standardabweichung **nur auf den Trainingsdaten** berechnet und dann Training und Test damit transformiert.
 Warum nur auf den Trainingsdaten? (Stichwort Data Leakage)
4. **Modell 1D:** Trainiere eine Regression nur mit dem BMI. Zeichne Daten und gelernte Gerade.
5. **Gradient prüfen:** Implementiere `mse_gradient(X, y, w, b)` und vergleiche ihn mit numerischen Ableitungen. Die Abweichung sollte unter \(10^{-6}\) liegen.
6. **Modell mit allen Features:** Trainiere mit Batch-Gradientenabstieg. Zeichne die Lernkurve für die Lernraten 0,001 / 0,01 / 0,1 / 1,0 in ein Diagramm. Welche divergiert?
7. **Mini-Batch:** Implementiere Mini-Batch-GD (Batchgröße 32, Daten in jeder Epoche neu mischen). Vergleiche die Lernkurve mit Batch-GD.
8. **Vergleich mit scikit-learn:** Trainiere `LinearRegression` auf denselben standardisierten Daten. Stimmen Gewichte und Test-MSE mit deinen überein?
9. **Ohne Standardisierung:** Wiederhole Schritt 6 mit den unskalierten Daten. Welche Lernrate funktioniert jetzt noch? Erkläre das mit der Animation aus Lektion 5.
10. **Deuten:** Welche drei Features haben die betragsmäßig größten Gewichte? Warum darf man Gewichte nur bei standardisierten Features so vergleichen?

### Erfolgskriterien

- Dein Gradient stimmt mit dem numerischen Gradienten überein.
- Deine Gewichte weichen um weniger als 1 % von `LinearRegression` ab.
- Mit dem Split aus Aufgabe 2 (Seed 42) liegt der Test-MSE bei etwa 2 600 (\(R^2 \approx 0{,}59\)). Die Baseline „immer den Mittelwert vorhersagen“ liegt bei etwa 6 400.
- Du kannst in eigenen Worten erklären, warum auf unskalierten Daten nur winzige Lernraten stabil sind – und warum das Training dann trotzdem kaum vorankommt.

> **Hinweise**
> Fang klein an: Erst 1 Feature, dann alle. Erst prüfen, dann trainieren. Druck in den ersten Epochen den Verlust aus. Steigt er, ist die Lernrate zu groß oder das Vorzeichen des Gradienten falsch. Ein \(R^2\) von knapp 0,6 heißt: 40 % der Streuung erklärt das Modell nicht – der Datensatz ist verrauscht, und das ist realistisch. Vergleiche immer mit einer Baseline: Was ist der MSE, wenn du stur den Mittelwert von \(y\) vorhersagst?

### Rückblick auf Modul 1

Du hast jetzt das Fundament, auf dem alle weiteren Module stehen:

| Gelernt | Kommt wieder in … |
|---|---|
| Skalarprodukt, Matrixmultiplikation | lineare Modelle, SVM, neuronale Netze, Attention |
| Distanzen & Skalierung | kNN, k-Means, DBSCAN, SVM mit RBF-Kernel |
| Wahrscheinlichkeit, Bayes, Maximum Likelihood | Naive Bayes, logistische Regression, Gaussian Mixtures, Sprachmodelle |
| Varianz, Kovarianz | Bias-Varianz-Tradeoff, PCA, Random Forest (Varianzreduktion) |
| Gradient, Kettenregel | Backpropagation, Gradient Boosting (das „Gradient“ im Namen!) |
| Verlustfunktionen, Gradientenabstieg | praktisch jedes Modell ab Modul 3 |

In **Modul 2** geht es um den professionellen Workflow mit scikit-learn: Pipelines, Kreuzvalidierung, Metriken und die Frage, wie man zuverlässig misst, ob ein Modell gut ist.
