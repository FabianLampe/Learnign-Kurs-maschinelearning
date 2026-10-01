# Video-Prompts für alle Kursthemen

So benutzt du die Datei:

1. Kopiere **einen** der beiden System-Prompts unten in LM Studio (Feld „System Prompt“).
   - **A** liefert ein Drehbuch (Szenen, Sprechertext, Bildbeschreibung). Das kannst du in einem Video-Tool umsetzen oder einsprechen.
   - **B** liefert direkt Manim-Python-Code, aus dem du ein Animationsvideo renderst (`manim -qm datei.py Szene`).
2. Schicke danach pro Video **einen** Themen-Prompt als Nachricht. Jeder Prompt steht für sich allein.

Tipp: Kleine lokale Modelle (7–8B) verlieren bei langen Antworten oft den Faden. Bei Manim-Code mit 20B+ Parametern arbeiten
und den Code immer erst testen.

---

## System-Prompt A: Drehbuch

```
Du bist Drehbuchautor für Erklärvideos über Machine Learning im Stil von 3Blue1Brown und StatQuest.
Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen, Ziel ist echtes Verständnis.
Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch in Klammern beim ersten Auftreten.
Aufbau: Intuition und Alltagsbeispiel zuerst, dann die Mathematik, dann ein kurzes Praxisbeispiel (Python/scikit-learn), am Ende 3 Kernaussagen.
Ausgabeformat: nummerierte Szenen. Pro Szene: Dauer in Sekunden, SPRECHERTEXT (wörtlich, gesprochene Sprache, kurze Sätze),
VISUELL (was genau animiert wird: Achsen, Punkte, Pfeile, Farben, Formeln), EINBLENDUNG (kurzer Bildschirmtext/Formel).
Formeln als Klartext (z. B. "w_neu = w - η · Gradient"). Keine Fakten erfinden; vereinfache, aber bleib korrekt.
```

## System-Prompt B: Manim-Code

```
Du schreibst Manim Community Edition (Version 0.18+) Python-Code für Erklärvideos über Machine Learning.
Regeln: eine Klasse pro Video, die von Scene erbt; kein LaTeX (Text statt MathTex/Tex); Schrift "DejaVu Sans";
dunkler Hintergrund #0f1115, Farben: Blau #3987e5, Orange #d95926, Grün #199e70, Text #eceef2.
Deutsche Texteinblendungen, Fachbegriff auf Englisch in Klammern. Länge 60–120 Sekunden.
Aufbau: Titel → Intuition → Mathematik Schritt für Schritt animiert → Fazit-Einblendung.
Zufallsdaten nur mit festem Seed (np.random.default_rng(0)). Gib nur lauffähigen Code aus, mit kurzen Kommentaren.
```

---

## Modul 1 – Grundlagen & Mathe

**1.1 Was ist Machine Learning?**
```
Erklärvideo „Was ist Machine Learning?“: klassisches Programmieren (Daten + Regeln → Antworten) vs. ML (Daten + Antworten → Regeln/Modell). Begriffe Feature, Label, Modell ŷ = f(x), Parameter vs. Hyperparameter, Training vs. Inferenz. Beispiel: Spamfilter und Wohnungspreise.
```

**1.2 Die drei Lernarten**
```
Erklärvideo „Überwachtes, unüberwachtes und bestärkendes Lernen“: Labels vs. keine Labels vs. Belohnung. Klassifikation vs. Regression. Kurz: semi- und selbstüberwachtes Lernen (so werden Sprachmodelle vortrainiert). Je ein Alltagsbeispiel.
```

**1.3 Der ML-Workflow**
```
Erklärvideo „Wie ein ML-Projekt abläuft“: Problem formulieren, Baseline, Daten erkunden, vorbereiten, Train/Validierung/Test-Split, Modelle vergleichen, einmalig auf Testdaten bewerten, ausliefern, überwachen. Kernregel: nie auf Trainingsdaten bewerten.
```

**1.4 Vektoren & Skalarprodukt**
```
Erklärvideo „Vektoren und Skalarprodukt“: Datenpunkt als Vektor, Datensatz als Matrix X (n × d). Skalarprodukt a·b = Σ aᵢbᵢ = ‖a‖‖b‖cos θ, Projektion, Kosinus-Ähnlichkeit. Warum es überall im ML steckt: lineare Modelle, Neuronen, Embeddings, Attention.
```

**1.5 Distanzen & Skalierung**
```
Erklärvideo „Distanzen und warum man Features skaliert“: euklidische (L2) und Manhattan-Distanz (L1), Beispiel Wohnfläche (m²) vs. Zimmerzahl dominiert die Distanz, Standardisierung z = (x − μ)/σ dreht das Ergebnis um. Bezug zu kNN, k-Means, SVM.
```

**1.6 Matrizen als Abbildungen**
```
Erklärvideo „Was eine Matrix mit dem Raum macht“: Matrix-Vektor-Produkt, Spalten = Bilder der Einheitsvektoren, Drehung, Scherung, Streckung, Determinante als Flächenfaktor, det = 0 heißt nicht invertierbar. Vorhersagen aller Datenpunkte auf einmal: ŷ = Xw + b.
```

**1.7 Mittelwert, Median, Varianz**
```
Erklärvideo „Daten beschreiben“: Mittelwert, Median, Varianz, Standardabweichung, Wirkung eines Ausreißers (Gehalt der Chefin), z-Score und StandardScaler, Bessel-Korrektur n−1 in einem Satz.
```

**1.8 Normalverteilung & Zentraler Grenzwertsatz**
```
Erklärvideo „Warum ist alles normalverteilt?“: Normalverteilung mit μ und σ, 68-95-99,7-Regel, Würfel-Experiment: Mittelwerte vieler Würfel werden glockenförmig, Breite schrumpft mit σ/√n.
```

**1.9 Satz von Bayes**
```
Erklärvideo „Satz von Bayes am medizinischen Test“: 1000 Personen, 1 % krank, Test 95 % sensitiv und 95 % spezifisch → bei positivem Test nur ca. 16 % wirklich krank. Prior, Likelihood, Posterior. Bezug: unbalancierte Daten, Precision, Naive Bayes.
```

**1.10 Korrelation & Kausalität**
```
Erklärvideo „Korrelation ist nicht Kausalität“: Kovarianz, Pearson-Korrelation r zwischen −1 und 1, misst nur lineare Zusammenhänge (y = x² ergibt r ≈ 0), Eis und Sonnenbrand mit Störvariable Wetter, Kovarianzmatrix als Ausblick auf PCA.
```

**1.11 Maximum Likelihood**
```
Erklärvideo „Maximum Likelihood“: Welche Parameter machen die beobachteten Daten am wahrscheinlichsten? Log-Likelihood, normalverteiltes Rauschen → MSE, Bernoulli → Kreuzentropie. Verlustfunktionen sind nicht willkürlich.
```

**1.12 Ableitungen**
```
Erklärvideo „Ableitung = Steigung“: Sekante durch x und x+h, h → 0 ergibt Tangente, Vorzeichen der Ableitung sagt, in welche Richtung x geändert werden muss, um f zu verkleinern. Wichtige Regeln inkl. Sigmoid und ReLU.
```

**1.13 Gradient**
```
Erklärvideo „Der Gradient“: partielle Ableitungen, Gradient als Vektor, zeigt in Richtung des steilsten Anstiegs, steht senkrecht auf Höhenlinien, −∇f zeigt bergab. Begründung über Skalarprodukt ∇f · Δ.
```

**1.14 Kettenregel & Rechengraph**
```
Erklärvideo „Die Kettenregel als Rechengraph“: f(x) = (3x+1)² bei x = 2, Vorwärtsrechnung (u = 7, f = 49), Rückwärtsrechnung mit lokalen Ableitungen 14 · 3 = 42. Das ist das Prinzip von Backpropagation und Autograd.
```

**1.15 Verlustfunktionen**
```
Erklärvideo „Verlustfunktionen“: Residuen, MSE als echte Quadrate, MAE, Huber-Loss, Kreuzentropie (sicher und falsch wird hart bestraft). Unterschied Verlust vs. Metrik: warum man nicht direkt auf Accuracy trainiert.
```

**1.16 Gradientenabstieg & Lernrate**
```
Erklärvideo „Gradientenabstieg“: Wanderer im Nebel, Update θ ← θ − η∇L, Lernrate zu klein/gut/zu groß/divergent an f(x) = x²/2 (Grenze η < 2), lokale Minima, Zickzack in langgezogenen Tälern, warum Feature-Skalierung hilft.
```

**1.17 Batch, SGD, Mini-Batch**
```
Erklärvideo „Batch, stochastischer und Mini-Batch-Gradientenabstieg“: Gradient aus allen Daten, einem Beispiel oder einer kleinen Gruppe; Epoche; Rauschen vs. Geschwindigkeit; Lernkurve lesen; Abbruch per Konvergenz oder Early Stopping.
```

## Modul 2 – Daten & der scikit-learn-Workflow

**2.1 Die scikit-learn-API**
```
Erklärvideo „Die scikit-learn-API“: Estimator, fit / predict / transform / fit_transform, score, Hyperparameter im Konstruktor, gelernte Attribute mit Unterstrich (coef_). Warum alle Modelle dieselbe Schnittstelle haben.
```

**2.2 Train/Test-Split & Data Leakage**
```
Erklärvideo „Train/Test-Split und Data Leakage“: warum getrennte Testdaten, stratify, Zeitreihen nicht zufällig mischen, typische Leaks (Skalierung vor dem Split, Zukunftsinformationen, Duplikate). Beispiel mit zu guten Ergebnissen.
```

**2.3 Vorverarbeitung**
```
Erklärvideo „Daten vorbereiten“: StandardScaler, MinMaxScaler, One-Hot- und Ordinal-Encoding, fehlende Werte mit SimpleImputer, Ausreißer. Welche Modelle Skalierung brauchen (kNN, SVM, lineare) und welche nicht (Bäume).
```

**2.4 Pipelines & ColumnTransformer**
```
Erklärvideo „Pipelines in scikit-learn“: Vorverarbeitung und Modell als eine Einheit, ColumnTransformer für numerische vs. kategoriale Spalten, verhindert Leakage in der Kreuzvalidierung, Codebeispiel.
```

**2.5 Kreuzvalidierung**
```
Erklärvideo „Kreuzvalidierung“: k-Fold animiert (5 Folds rotieren), Mittelwert und Streuung des Scores, StratifiedKFold, TimeSeriesSplit, warum ein einzelner Split täuschen kann.
```

**2.6 Klassifikationsmetriken**
```
Erklärvideo „Accuracy, Precision, Recall, F1“: Konfusionsmatrix (TP, FP, FN, TN), Accuracy-Falle bei unbalancierten Daten (99 % durch "immer negativ"), Precision vs. Recall am Spam- und Krebs-Beispiel, F1.
```

**2.7 ROC-Kurve & AUC**
```
Erklärvideo „ROC und AUC“: Schwellenwert verschieben, True-Positive-Rate vs. False-Positive-Rate, AUC als Wahrscheinlichkeit, dass ein positives Beispiel höher bewertet wird als ein negatives, Precision-Recall-Kurve bei seltenen Klassen.
```

**2.8 Regressionsmetriken**
```
Erklärvideo „MSE, RMSE, MAE und R²“: Bedeutung und Einheiten, R² als Anteil erklärter Varianz gegenüber der Mittelwert-Baseline, negatives R², Wahl der Metrik nach Fragestellung.
```

**2.9 Bias-Varianz-Tradeoff**
```
Erklärvideo „Overfitting, Underfitting und der Bias-Varianz-Tradeoff“: Polynome Grad 1, 4, 15 an verrauschte Daten, Trainings- vs. Testfehler über die Modellkomplexität (U-Kurve), Lernkurven, Gegenmittel.
```

**2.10 Hyperparameter-Suche**
```
Erklärvideo „Hyperparameter finden“: GridSearchCV vs. RandomizedSearchCV (warum Zufall oft besser ist), verschachtelte Kreuzvalidierung, Testdaten erst ganz am Ende, kurzer Ausblick auf Bayes'sche Optimierung (Optuna).
```

## Modul 3 – Lineare Modelle

**3.1 Lineare Regression**
```
Erklärvideo „Lineare Regression“: Modell ŷ = Xw + b, kleinste Quadrate, Normalengleichung w = (XᵀX)⁻¹Xᵀy vs. Gradientenabstieg, Interpretation der Koeffizienten, Annahmen und Residuenplot.
```

**3.2 Polynomielle Features**
```
Erklärvideo „Polynomielle Regression“: nichtlineare Zusammenhänge mit linearem Modell durch Features x, x², x³, PolynomialFeatures, Overfitting bei hohem Grad, Bezug zum Bias-Varianz-Tradeoff.
```

**3.3 Ridge, Lasso, Elastic Net**
```
Erklärvideo „Regularisierung: Ridge, Lasso, Elastic Net“: Strafterm λ‖w‖² vs. λ‖w‖₁, geometrisch Kreis vs. Raute (warum Lasso Gewichte exakt auf 0 setzt), Multikollinearität, Wahl von alpha per Kreuzvalidierung.
```

**3.4 Logistische Regression**
```
Erklärvideo „Logistische Regression“: Sigmoid macht aus w·x + b eine Wahrscheinlichkeit, Entscheidungsgrenze ist eine Gerade, Kreuzentropie als Verlust, Odds und Log-Odds, Koeffizienten deuten, Schwellenwert.
```

**3.5 Softmax-Regression**
```
Erklärvideo „Mehrklassen-Klassifikation mit Softmax“: ein Score pro Klasse, Softmax macht daraus Wahrscheinlichkeiten, kategoriale Kreuzentropie, One-vs-Rest im Vergleich, Grundlage der Ausgabeschicht neuronaler Netze.
```

**3.6 SGDClassifier & SGDRegressor**
```
Erklärvideo „Lineare Modelle für große Daten mit SGD“: SGDClassifier/SGDRegressor, verschiedene loss-Parameter (hinge, log_loss, squared_error), partial_fit für Daten, die nicht in den Speicher passen, Skalierung ist Pflicht.
```

## Modul 4 – Nachbarn & Wahrscheinlichkeiten

**4.1 k-Nächste-Nachbarn**
```
Erklärvideo „k-Nächste-Nachbarn“: Klassifikation durch Mehrheitsentscheid der k nächsten Punkte, Einfluss von k (k=1 Overfitting), Distanzgewichtung, kNN-Regression, faules Lernen: Training kostet nichts, Vorhersage viel.
```

**4.2 Fluch der Dimensionalität**
```
Erklärvideo „Der Fluch der Dimensionalität“: in hohen Dimensionen sind alle Punkte fast gleich weit entfernt, Volumen wandert in die Ecken des Würfels, Datenbedarf explodiert. Folgen für kNN und Clustering, Gegenmittel Feature-Auswahl und PCA.
```

**4.3 Naive Bayes**
```
Erklärvideo „Naive Bayes“: Satz von Bayes für Klassifikation, naive Unabhängigkeitsannahme, Gauß-, Multinomial- und Bernoulli-Variante, Spamfilter Schritt für Schritt mit Wortwahrscheinlichkeiten, Laplace-Glättung.
```

**4.4 LDA & QDA**
```
Erklärvideo „Lineare und quadratische Diskriminanzanalyse“: jede Klasse als Normalverteilung, gemeinsame Kovarianz → lineare Grenze (LDA), eigene Kovarianz → quadratische Grenze (QDA), LDA auch zur Dimensionsreduktion.
```

## Modul 5 – Support Vector Machines

**5.1 Maximaler Rand (Hard Margin)**
```
Erklärvideo „Support Vector Machines: der maximale Rand“: viele trennende Geraden möglich, SVM wählt die mit dem breitesten Korridor, Stützvektoren bestimmen allein die Grenze, Randbreite 2/‖w‖.
```

**5.2 Soft Margin & Parameter C**
```
Erklärvideo „Soft Margin und der Parameter C“: Schlupfvariablen erlauben Fehler, großes C = harte Grenze/Overfitting, kleines C = breiter Rand/mehr Fehler, Hinge Loss max(0, 1 − y·f(x)) im Vergleich zur Kreuzentropie.
```

**5.3 Der Kernel-Trick**
```
Erklärvideo „Der Kernel-Trick“: Kreis-Daten in 2D nicht linear trennbar, Abbildung in 3D (z = x² + y²) macht sie trennbar, Kernel berechnet Skalarprodukte im hohen Raum ohne ihn zu betreten, polynomialer Kernel.
```

**5.4 RBF-Kernel & gamma**
```
Erklärvideo „RBF-Kernel und gamma“: Ähnlichkeit als Glockenkurve um jeden Stützvektor, kleines gamma = glatte Grenze, großes gamma = Inseln/Overfitting, Zusammenspiel von C und gamma, Grid Search, Skalierung zwingend.
```

**5.5 Support Vector Regression**
```
Erklärvideo „Support Vector Regression“: ε-Schlauch um die Funktion, Punkte im Schlauch kosten nichts, nur Punkte außerhalb sind Stützvektoren, Kernel für nichtlineare Regression, Parameter epsilon und C.
```

## Modul 6 – Entscheidungsbäume & Ensembles

**6.1 Entscheidungsbaum**
```
Erklärvideo „Entscheidungsbäume“: Daten durch Ja/Nein-Fragen aufteilen, achsenparallele Grenzen, Gini-Unreinheit und Entropie, Information Gain, wie der beste Split gesucht wird, Regressionsbaum mit Varianzreduktion.
```

**6.2 Pruning & Baumtiefe**
```
Erklärvideo „Bäume zähmen“: ein unbegrenzter Baum lernt jeden Punkt auswendig, max_depth, min_samples_leaf, Cost-Complexity-Pruning (ccp_alpha), Instabilität einzelner Bäume als Motivation für Ensembles.
```

**6.3 Bagging & Random Forest**
```
Erklärvideo „Random Forest“: Bootstrap-Stichproben, viele Bäume, Mehrheitsentscheid; zusätzliche Zufallsauswahl von Features pro Split (max_features) entkoppelt die Bäume; Mitteln reduziert Varianz; Out-of-Bag-Fehler.
```

**6.4 Extra Trees**
```
Erklärvideo „Extremely Randomized Trees“: Split-Schwellen zufällig statt optimal, noch weniger Varianz, schneller zu trainieren, Vergleich mit Random Forest an einem Beispiel.
```

**6.5 AdaBoost**
```
Erklärvideo „AdaBoost Schritt für Schritt“: schwache Lerner (Baumstümpfe) nacheinander, falsch klassifizierte Punkte bekommen mehr Gewicht, jeder Lerner erhält ein Stimmgewicht, gewichtete Abstimmung am Ende. Mit 3 Runden animiert.
```

**6.6 Gradient Boosting**
```
Erklärvideo „Gradient Boosting“: Start mit dem Mittelwert, jeder neue Baum lernt die Residuen des bisherigen Modells, Lernrate (Shrinkage) dämpft jeden Schritt; Residuen sind der negative Gradient des MSE – daher der Name; andere Losses (Log Loss, Huber) über ihren Gradienten. Mit 4 Runden animiert.
```

**6.7 Gradient Boosting in der Praxis**
```
Erklärvideo „HistGradientBoosting, XGBoost, LightGBM, CatBoost“: Histogramm-Binning für Geschwindigkeit, wichtige Hyperparameter (learning_rate, n_estimators, max_depth, subsample), Early Stopping, Regularisierung, Besonderheiten der vier Bibliotheken, warum sie Tabellendaten dominieren.
```

**6.8 Stacking & Voting**
```
Erklärvideo „Modelle kombinieren: Voting und Stacking“: harte und weiche Abstimmung, Stacking mit einem Meta-Modell auf Out-of-Fold-Vorhersagen, warum unterschiedliche Modelle sich ergänzen.
```

**6.9 Feature Importance**
```
Erklärvideo „Welche Features sind wichtig?“: Impurity-basierte Importance und ihre Schwächen (bevorzugt Features mit vielen Werten), Permutation Importance auf Testdaten, korrelierte Features teilen sich die Wichtigkeit.
```

## Modul 7 – Unüberwachtes Lernen

**7.1 k-Means & k-Means++**
```
Erklärvideo „k-Means“: Zentren zufällig setzen, Punkte dem nächsten Zentrum zuordnen, Zentren neu berechnen, wiederholen (animiert); Inertia; schlechte Starts und k-Means++; Elbow-Methode; Grenzen bei nicht-runden Clustern.
```

**7.2 Hierarchisches Clustering**
```
Erklärvideo „Hierarchisches Clustering“: agglomerativ von unten, Linkage-Varianten (single, complete, average, Ward), Dendrogramm lesen und an einer Höhe abschneiden.
```

**7.3 DBSCAN & HDBSCAN**
```
Erklärvideo „DBSCAN“: dichtebasierte Cluster, Parameter eps und min_samples, Kern-, Rand- und Rauschpunkte, findet beliebige Formen (Halbmonde) und Ausreißer, HDBSCAN für unterschiedliche Dichten.
```

**7.4 Gaussian Mixture Models & EM**
```
Erklärvideo „Gaussian Mixture Models und der EM-Algorithmus“: Daten als Mischung von Glockenkurven, weiche Zuordnung, E-Schritt (Wahrscheinlichkeiten) und M-Schritt (Parameter) im Wechsel animiert, Vergleich mit k-Means, Modellwahl mit BIC.
```

**7.5 PCA**
```
Erklärvideo „Hauptkomponentenanalyse (PCA)“: Richtung maximaler Varianz finden, Projektion auf wenige Achsen, Eigenvektoren der Kovarianzmatrix, erklärte Varianz, Daten vorher standardisieren, Anwendung Visualisierung und Kompression.
```

**7.6 t-SNE & UMAP**
```
Erklärvideo „t-SNE und UMAP“: nichtlineare Einbettung, Nachbarschaften erhalten statt Distanzen, Perplexity bzw. n_neighbors, Fallen beim Interpretieren (Clustergrößen und Abstände bedeuten nichts), MNIST-Beispiel.
```

**7.7 Cluster bewerten**
```
Erklärvideo „Wie gut sind meine Cluster?“: Silhouette-Koeffizient Schritt für Schritt (a und b eines Punktes), Davies-Bouldin, Calinski-Harabasz, Adjusted Rand Index wenn Labels bekannt sind, warum es keine absolute Wahrheit gibt.
```

## Modul 8 – Anomalieerkennung

**8.1 Statistische Ausreißererkennung**
```
Erklärvideo „Ausreißer statistisch finden“: z-Score mit Schwelle 3, IQR-Regel und Boxplot (1,5 · IQR), robuste Variante mit Median und MAD, Grenzen bei mehreren Dimensionen.
```

**8.2 Isolation Forest: die Idee**
```
Erklärvideo „Isolation Forest: wie Isolation funktioniert“: zufälliges Feature und zufälliger Schnitt zwischen Min und Max, so lange teilen, bis ein Punkt allein ist; Ausreißer werden nach wenigen Schnitten isoliert, normale Punkte brauchen viele. Einen Ausreißer und einen normalen Punkt nebeneinander animiert isolieren.
```

**8.3 Isolation Forest: Pfadlänge & Score**
```
Erklärvideo „Isolation Forest: Pfadlänge und Anomalie-Score“: viele Isolationsbäume auf Teilstichproben (max_samples = 256), mittlere Pfadlänge h(x), Normierung mit c(n), Score s = 2^(−E[h(x)]/c(n)) – nahe 1 = Anomalie, ≤ 0,5 = normal; contamination-Parameter; Stärken und Schwächen.
```

**8.4 Local Outlier Factor**
```
Erklärvideo „Local Outlier Factor (LOF)“: lokale Dichte eines Punktes im Vergleich zu seinen Nachbarn, Erreichbarkeitsdistanz, LOF ≈ 1 normal, deutlich > 1 Ausreißer; findet lokale Ausreißer neben dichten Clustern, wo globale Methoden versagen.
```

**8.5 One-Class SVM**
```
Erklärvideo „One-Class SVM“: nur normale Daten lernen, Grenze um die Datenwolke mit RBF-Kernel, Parameter nu als Obergrenze für den Ausreißeranteil, Skalierung nötig, Vergleich mit Isolation Forest.
```

**8.6 Elliptic Envelope**
```
Erklärvideo „Elliptic Envelope“: Daten als Normalverteilung annehmen, robuste Kovarianzschätzung (Minimum Covariance Determinant), Mahalanobis-Distanz statt euklidischer Distanz, funktioniert nur für ungefähr ellipsenförmige Daten.
```

**8.7 Projekt Kreditkartenbetrug**
```
Erklärvideo „Betrug erkennen – ein Projekt von Anfang bis Ende“: extrem unbalancierte Daten (0,17 % Betrug), warum Accuracy nutzlos ist, Isolation Forest vs. überwachtes Gradient Boosting, Precision-Recall-Kurve, Schwellenwert nach Kosten von Fehlalarm vs. übersehenem Betrug wählen.
```

## Modul 9 – Neuronale Netze

**9.1 Perzeptron & Neuron**
```
Erklärvideo „Das künstliche Neuron“: gewichtete Summe plus Bias, Aktivierungsfunktion, Perzeptron-Lernregel, Grenze: XOR ist nicht linear trennbar – Motivation für mehrere Schichten.
```

**9.2 Aktivierungsfunktionen**
```
Erklärvideo „Aktivierungsfunktionen“: warum Nichtlinearität nötig ist (sonst kollabieren alle Schichten zu einer linearen Abbildung), Sigmoid, tanh, ReLU, Leaky ReLU, GELU, verschwindende Gradienten, Softmax am Ausgang.
```

**9.3 Forward Pass**
```
Erklärvideo „Wie ein neuronales Netz rechnet“: Schichten als Matrixmultiplikation plus Aktivierung, ein kleines Netz 2-3-1 mit konkreten Zahlen durchrechnen, wie Schichten den Raum schrittweise verformen, bis die Daten linear trennbar sind.
```

**9.4 Backpropagation**
```
Erklärvideo „Backpropagation Schritt für Schritt“: Verlust berechnen, Kettenregel rückwärts durch das Netz, lokale Gradienten an jedem Knoten, Gradient für jedes Gewicht, Update mit Gradientenabstieg. Ein Mini-Netz mit konkreten Zahlen.
```

**9.5 MLPClassifier in scikit-learn**
```
Erklärvideo „Neuronale Netze mit scikit-learn“: MLPClassifier und MLPRegressor, hidden_layer_sizes, Aktivierung, Solver adam, alpha (L2), Early Stopping, Skalierung, Grenzen gegenüber PyTorch.
```

**9.6 Einführung in PyTorch**
```
Erklärvideo „PyTorch in 10 Minuten“: Tensoren, autograd mit requires_grad und backward, nn.Module, Optimizer, die Trainingsschleife (zero_grad, forward, loss, backward, step), DataLoader, GPU.
```

## Modul 10 – Deep Learning

**10.1 Optimierer**
```
Erklärvideo „SGD, Momentum, RMSProp, Adam“: Momentum als rollende Kugel dämpft Zickzack, adaptive Lernraten pro Parameter, Adam kombiniert beides, Lernraten-Schedules und Warmup, Pfade im langgezogenen Tal im Vergleich.
```

**10.2 Initialisierung, BatchNorm, Dropout**
```
Erklärvideo „Tiefe Netze stabil trainieren“: Xavier- und He-Initialisierung, explodierende und verschwindende Gradienten, Batch- und Layer-Normalisierung, Dropout als Regularisierung, Weight Decay, Residualverbindungen.
```

**10.3 CNNs**
```
Erklärvideo „Convolutional Neural Networks“: Faltungsfilter gleitet über das Bild (animiert), Feature Maps, Padding und Stride, Pooling, Hierarchie von Kanten zu Formen zu Objekten, Parameterteilung, LeNet bis ResNet.
```

**10.4 RNNs, LSTM & GRU**
```
Erklärvideo „Rekurrente Netze, LSTM und GRU“: versteckter Zustand trägt Information durch die Sequenz, Ausrollen über die Zeit, verschwindende Gradienten, Gates der LSTM (Vergessen, Eingabe, Ausgabe), GRU als vereinfachte Form.
```

**10.5 Transfer Learning**
```
Erklärvideo „Transfer Learning“: vortrainiertes Netz (z. B. auf ImageNet) wiederverwenden, frühe Schichten einfrieren, neuen Kopf trainieren, Fine-Tuning mit kleiner Lernrate, warum das mit wenig Daten funktioniert.
```

**10.6 Autoencoder & VAEs**
```
Erklärvideo „Autoencoder und Variational Autoencoder“: Encoder komprimiert, Decoder rekonstruiert, Flaschenhals als Merkmalsraum, Anomalieerkennung über den Rekonstruktionsfehler, VAE mit Verteilung im latenten Raum und Reparametrisierungs-Trick, neue Daten erzeugen.
```

**10.7 GANs & Diffusionsmodelle**
```
Erklärvideo „Wie KI Bilder erzeugt: GANs und Diffusion“: Generator gegen Diskriminator, Mode Collapse; Diffusion: Bild schrittweise verrauschen und ein Netz lernt das Entrauschen, Text-Konditionierung, warum Diffusion heute dominiert.
```

## Modul 11 – Moderne KI: Transformer & LLMs

**11.1 Word Embeddings**
```
Erklärvideo „Word Embeddings“: Wörter als Vektoren, ähnliche Bedeutung = ähnliche Richtung, König − Mann + Frau ≈ Königin, Word2Vec-Idee (Wort aus Kontext vorhersagen), Kosinus-Ähnlichkeit, kontextabhängige Embeddings.
```

**11.2 Attention**
```
Erklärvideo „Der Attention-Mechanismus“: Query, Key, Value; Skalarprodukt Query·Key als Relevanz, Softmax zu Gewichten, gewichtete Summe der Values; Beispiel "Die Bank am Fluss" vs. "die Bank gibt Kredit"; Skalierung mit √d.
```

**11.3 Transformer-Architektur**
```
Erklärvideo „Der Transformer“: Self-Attention, Multi-Head-Attention, Positionskodierung, Feed-Forward-Schicht, Residualverbindungen und LayerNorm, Encoder vs. Decoder, kausale Maske, warum parallelisierbar im Gegensatz zu RNNs.
```

**11.4 Tokenisierung**
```
Erklärvideo „Tokenisierung“: Text in Tokens zerlegen, Byte-Pair-Encoding Schritt für Schritt, Vokabulargröße, warum LLMs mit Buchstaben zählen und seltenen Wörtern Probleme haben, Tokens und Kosten.
```

**11.5 Pretraining, Fine-Tuning, RLHF**
```
Erklärvideo „Wie ein Sprachmodell entsteht“: Pretraining durch Vorhersage des nächsten Tokens auf riesigen Textmengen, Supervised Fine-Tuning mit Beispieldialogen, RLHF/Präferenzlernen, Parameter-effizientes Fine-Tuning (LoRA).
```

**11.6 LLMs & Prompting**
```
Erklärvideo „Large Language Models nutzen“: Erzeugung Token für Token, Temperatur und Sampling, Kontextfenster, Halluzinationen, Prompting-Techniken (Rolle, Beispiele, Schritt-für-Schritt), Grenzen.
```

**11.7 RAG**
```
Erklärvideo „Retrieval Augmented Generation (RAG)“: Dokumente in Abschnitte teilen, Embeddings in einer Vektordatenbank, ähnlichste Abschnitte zur Frage suchen, in den Prompt geben, Antwort mit Quellen; typische Fehlerquellen und Bewertung.
```

## Modul 12 – Reinforcement Learning

**12.1 Agent, Umgebung, Belohnung**
```
Erklärvideo „Reinforcement Learning: die Grundidee“: Agent, Zustand, Aktion, Belohnung, Policy, Episode, Exploration vs. Exploitation (ε-greedy), Mehrarmiger Bandit als einfachstes Beispiel.
```

**12.2 Markov-Entscheidungsprozesse**
```
Erklärvideo „Markov-Entscheidungsprozesse“: Zustände, Übergangswahrscheinlichkeiten, Belohnungen, Diskontfaktor γ, Return, Wertfunktion V und Q, Bellman-Gleichung an einer kleinen Gitterwelt.
```

**12.3 Q-Learning**
```
Erklärvideo „Q-Learning“: Q-Tabelle, Update Q ← Q + α(r + γ·max Q' − Q), Agent lernt in einer Gitterwelt den Weg zum Ziel und meidet Fallen (animiert über Episoden), Off-Policy-Lernen.
```

**12.4 Deep Q-Networks**
```
Erklärvideo „Deep Q-Networks“: neuronales Netz statt Tabelle für große Zustandsräume, Experience Replay, Target Network, Atari-Beispiel, Instabilitäten.
```

**12.5 Policy Gradients**
```
Erklärvideo „Policy Gradients“: Policy direkt als Netz, Wahrscheinlichkeit guter Aktionen erhöhen (REINFORCE), Baseline zur Varianzreduktion, Actor-Critic, PPO in einem Satz, Bezug zu RLHF bei Sprachmodellen.
```

## Modul 13 – ML in der Praxis (MLOps)

**13.1 Feature Engineering**
```
Erklärvideo „Feature Engineering“: Domänenwissen in Features übersetzen, Datums- und Zeitfeatures, zyklische Kodierung mit sin/cos, Interaktionen, Verhältnisse, Aggregationen, Target-Encoding und seine Leakage-Gefahr.
```

**13.2 Unbalancierte Daten**
```
Erklärvideo „Unbalancierte Daten“: Klassengewichte (class_weight), Under- und Oversampling, SMOTE, Schwellenwert anpassen statt Daten verändern, passende Metriken (PR-AUC), Resampling nur auf Trainingsdaten.
```

**13.3 Interpretierbarkeit mit SHAP**
```
Erklärvideo „Modelle erklären mit SHAP“: Shapley-Werte aus der Spieltheorie (fairer Anteil jedes Features), lokale Erklärung einer Vorhersage (Wasserfall), globale Übersicht (Beeswarm), Partial Dependence, Grenzen bei korrelierten Features.
```

**13.4 Modelle speichern & ausliefern**
```
Erklärvideo „Ein Modell in Produktion bringen“: Pipeline mit joblib speichern, Versionen fixieren, REST-API mit FastAPI, Docker, Batch- vs. Echtzeit-Vorhersagen, ONNX, Modell- und Datenversionierung.
```

**13.5 Monitoring & Data Drift**
```
Erklärvideo „Wenn sich die Welt ändert: Data Drift“: Data Drift vs. Concept Drift, Verteilungen vergleichen (PSI, Kolmogorov-Smirnov), Performance überwachen wenn Labels verzögert kommen, Retraining-Strategien.
```

**13.6 Fairness & Ethik**
```
Erklärvideo „Fairness in Machine Learning“: Verzerrungen in Daten (historisch, Stichprobe, Messung), Fairness-Definitionen (Demographic Parity, Equalized Odds) und warum sie sich widersprechen, Proxy-Variablen, Datenschutz, EU AI Act in einem Satz.
```
