# NotebookLM: Video-Prompts für alle Kursthemen

96 Prompts, einer pro Thema, für die **Video-Übersicht** in NotebookLM. Sie funktionieren genauso für die **Audio-Übersicht**.

## So gehst du vor

1. **Ein Notebook pro Modul anlegen** und die Quellen aus der Tabelle unten hinzufügen. Mit Quellen zu nur einem Modul bleibt das Video beim Thema.
2. In den NotebookLM-Einstellungen die **Ausgabesprache auf Deutsch** stellen.
3. Im Studio-Bereich bei **Video-Übersicht** auf **Anpassen** (Stiftsymbol) gehen und **einen** Prompt aus dieser Datei einfügen.
4. Generieren, und für das nächste Thema eine neue Video-Übersicht mit dem nächsten Prompt starten.

Warum jeder Prompt so beginnt: Ohne Eingrenzung fasst NotebookLM *alle* Quellen des Notebooks zusammen. Der Satz
„ausschließlich zum Thema …“ sorgt dafür, dass pro Video genau ein Thema erklärt wird.

## Quellen pro Modul

| Modul | Quellen |
|---|---|
| Modul 1 | Datei `notebooklm/quellen/modul-01.md` hochladen (kompletter Lektionstext dieses Kurses). |
| Modul 2 | https://scikit-learn.org/stable/modules/preprocessing.html · https://scikit-learn.org/stable/modules/compose.html · https://scikit-learn.org/stable/modules/cross_validation.html · https://scikit-learn.org/stable/modules/model_evaluation.html · https://scikit-learn.org/stable/modules/grid_search.html · https://scikit-learn.org/stable/modules/learning_curve.html |
| Modul 3 | https://scikit-learn.org/stable/modules/linear_model.html |
| Modul 4 | https://scikit-learn.org/stable/modules/neighbors.html · https://scikit-learn.org/stable/modules/naive_bayes.html · https://scikit-learn.org/stable/modules/lda_qda.html |
| Modul 5 | https://scikit-learn.org/stable/modules/svm.html |
| Modul 6 | https://scikit-learn.org/stable/modules/tree.html · https://scikit-learn.org/stable/modules/ensemble.html · https://scikit-learn.org/stable/modules/permutation_importance.html |
| Modul 7 | https://scikit-learn.org/stable/modules/clustering.html · https://scikit-learn.org/stable/modules/mixture.html · https://scikit-learn.org/stable/modules/decomposition.html · https://scikit-learn.org/stable/modules/manifold.html |
| Modul 8 | https://scikit-learn.org/stable/modules/outlier_detection.html (enthält Isolation Forest, LOF, One-Class SVM, Elliptic Envelope) |
| Modul 9 | https://scikit-learn.org/stable/modules/neural_networks_supervised.html · https://pytorch.org/tutorials/beginner/basics/intro.html |
| Modul 10 | „Quellen entdecken“ mit der Suche: *Deep Learning Optimierer Adam, Batch Normalization, Dropout, CNN, LSTM, Autoencoder, Diffusionsmodelle Einführung* |
| Modul 11 | „Quellen entdecken“ mit der Suche: *Word Embeddings, Attention, Transformer-Architektur, Tokenisierung BPE, RLHF, Retrieval Augmented Generation Einführung* |
| Modul 12 | „Quellen entdecken“ mit der Suche: *Reinforcement Learning Einführung, Markov-Entscheidungsprozess, Q-Learning, Deep Q-Network, Policy Gradient* |
| Modul 13 | https://scikit-learn.org/stable/inspection.html · https://scikit-learn.org/stable/model_persistence.html · dazu „Quellen entdecken“: *SHAP, Data Drift, Fairness Machine Learning* |

Die scikit-learn-Seiten fügst du als **Website**-Quelle per Link hinzu. Sobald weitere Module im Kurs fertig sind, kommen dafür eigene
Quelldateien in `notebooklm/quellen/` dazu (erzeugt mit `python tools/export_quellen.py`).

---

## Modul 1 – Grundlagen & Mathe

**1.1 Was ist Machine Learning?**
```
Erstelle die Übersicht ausschließlich zum Thema „Was ist Machine Learning?“ und lass andere Themen aus den Quellen weg. Behandle: klassisches Programmieren (Daten + Regeln → Antworten) vs. ML (Daten + Antworten → Regeln/Modell). Begriffe Feature, Label, Modell ŷ = f(x), Parameter vs. Hyperparameter, Training vs. Inferenz. Beispiel: Spamfilter und Wohnungspreise. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**1.2 Die drei Lernarten**
```
Erstelle die Übersicht ausschließlich zum Thema „Überwachtes, unüberwachtes und bestärkendes Lernen“ und lass andere Themen aus den Quellen weg. Behandle: Labels vs. keine Labels vs. Belohnung. Klassifikation vs. Regression. Kurz: semi- und selbstüberwachtes Lernen (so werden Sprachmodelle vortrainiert). Je ein Alltagsbeispiel. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**1.3 Der ML-Workflow**
```
Erstelle die Übersicht ausschließlich zum Thema „Wie ein ML-Projekt abläuft“ und lass andere Themen aus den Quellen weg. Behandle: Problem formulieren, Baseline, Daten erkunden, vorbereiten, Train/Validierung/Test-Split, Modelle vergleichen, einmalig auf Testdaten bewerten, ausliefern, überwachen. Kernregel: nie auf Trainingsdaten bewerten. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**1.4 Vektoren & Skalarprodukt**
```
Erstelle die Übersicht ausschließlich zum Thema „Vektoren und Skalarprodukt“ und lass andere Themen aus den Quellen weg. Behandle: Datenpunkt als Vektor, Datensatz als Matrix X (n × d). Skalarprodukt a·b = Σ aᵢbᵢ = ‖a‖‖b‖cos θ, Projektion, Kosinus-Ähnlichkeit. Warum es überall im ML steckt: lineare Modelle, Neuronen, Embeddings, Attention. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**1.5 Distanzen & Skalierung**
```
Erstelle die Übersicht ausschließlich zum Thema „Distanzen und warum man Features skaliert“ und lass andere Themen aus den Quellen weg. Behandle: euklidische (L2) und Manhattan-Distanz (L1), Beispiel Wohnfläche (m²) vs. Zimmerzahl dominiert die Distanz, Standardisierung z = (x − μ)/σ dreht das Ergebnis um. Bezug zu kNN, k-Means, SVM. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**1.6 Matrizen als Abbildungen**
```
Erstelle die Übersicht ausschließlich zum Thema „Was eine Matrix mit dem Raum macht“ und lass andere Themen aus den Quellen weg. Behandle: Matrix-Vektor-Produkt, Spalten = Bilder der Einheitsvektoren, Drehung, Scherung, Streckung, Determinante als Flächenfaktor, det = 0 heißt nicht invertierbar. Vorhersagen aller Datenpunkte auf einmal: ŷ = Xw + b. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**1.7 Mittelwert, Median, Varianz**
```
Erstelle die Übersicht ausschließlich zum Thema „Daten beschreiben“ und lass andere Themen aus den Quellen weg. Behandle: Mittelwert, Median, Varianz, Standardabweichung, Wirkung eines Ausreißers (Gehalt der Chefin), z-Score und StandardScaler, Bessel-Korrektur n−1 in einem Satz. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**1.8 Normalverteilung & Zentraler Grenzwertsatz**
```
Erstelle die Übersicht ausschließlich zum Thema „Warum ist alles normalverteilt?“ und lass andere Themen aus den Quellen weg. Behandle: Normalverteilung mit μ und σ, 68-95-99,7-Regel, Würfel-Experiment: Mittelwerte vieler Würfel werden glockenförmig, Breite schrumpft mit σ/√n. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**1.9 Satz von Bayes**
```
Erstelle die Übersicht ausschließlich zum Thema „Satz von Bayes am medizinischen Test“ und lass andere Themen aus den Quellen weg. Behandle: 1000 Personen, 1 % krank, Test 95 % sensitiv und 95 % spezifisch → bei positivem Test nur ca. 16 % wirklich krank. Prior, Likelihood, Posterior. Bezug: unbalancierte Daten, Precision, Naive Bayes. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**1.10 Korrelation & Kausalität**
```
Erstelle die Übersicht ausschließlich zum Thema „Korrelation ist nicht Kausalität“ und lass andere Themen aus den Quellen weg. Behandle: Kovarianz, Pearson-Korrelation r zwischen −1 und 1, misst nur lineare Zusammenhänge (y = x² ergibt r ≈ 0), Eis und Sonnenbrand mit Störvariable Wetter, Kovarianzmatrix als Ausblick auf PCA. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**1.11 Maximum Likelihood**
```
Erstelle die Übersicht ausschließlich zum Thema „Maximum Likelihood“ und lass andere Themen aus den Quellen weg. Behandle: Welche Parameter machen die beobachteten Daten am wahrscheinlichsten? Log-Likelihood, normalverteiltes Rauschen → MSE, Bernoulli → Kreuzentropie. Verlustfunktionen sind nicht willkürlich. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**1.12 Ableitungen**
```
Erstelle die Übersicht ausschließlich zum Thema „Ableitung = Steigung“ und lass andere Themen aus den Quellen weg. Behandle: Sekante durch x und x+h, h → 0 ergibt Tangente, Vorzeichen der Ableitung sagt, in welche Richtung x geändert werden muss, um f zu verkleinern. Wichtige Regeln inkl. Sigmoid und ReLU. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**1.13 Gradient**
```
Erstelle die Übersicht ausschließlich zum Thema „Der Gradient“ und lass andere Themen aus den Quellen weg. Behandle: partielle Ableitungen, Gradient als Vektor, zeigt in Richtung des steilsten Anstiegs, steht senkrecht auf Höhenlinien, −∇f zeigt bergab. Begründung über Skalarprodukt ∇f · Δ. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**1.14 Kettenregel & Rechengraph**
```
Erstelle die Übersicht ausschließlich zum Thema „Die Kettenregel als Rechengraph“ und lass andere Themen aus den Quellen weg. Behandle: f(x) = (3x+1)² bei x = 2, Vorwärtsrechnung (u = 7, f = 49), Rückwärtsrechnung mit lokalen Ableitungen 14 · 3 = 42. Das ist das Prinzip von Backpropagation und Autograd. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**1.15 Verlustfunktionen**
```
Erstelle die Übersicht ausschließlich zum Thema „Verlustfunktionen“ und lass andere Themen aus den Quellen weg. Behandle: Residuen, MSE als echte Quadrate, MAE, Huber-Loss, Kreuzentropie (sicher und falsch wird hart bestraft). Unterschied Verlust vs. Metrik: warum man nicht direkt auf Accuracy trainiert. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**1.16 Gradientenabstieg & Lernrate**
```
Erstelle die Übersicht ausschließlich zum Thema „Gradientenabstieg“ und lass andere Themen aus den Quellen weg. Behandle: Wanderer im Nebel, Update θ ← θ − η∇L, Lernrate zu klein/gut/zu groß/divergent an f(x) = x²/2 (Grenze η < 2), lokale Minima, Zickzack in langgezogenen Tälern, warum Feature-Skalierung hilft. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**1.17 Batch, SGD, Mini-Batch**
```
Erstelle die Übersicht ausschließlich zum Thema „Batch, stochastischer und Mini-Batch-Gradientenabstieg“ und lass andere Themen aus den Quellen weg. Behandle: Gradient aus allen Daten, einem Beispiel oder einer kleinen Gruppe; Epoche; Rauschen vs. Geschwindigkeit; Lernkurve lesen; Abbruch per Konvergenz oder Early Stopping. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

## Modul 2 – Daten & der scikit-learn-Workflow

**2.1 Die scikit-learn-API**
```
Erstelle die Übersicht ausschließlich zum Thema „Die scikit-learn-API“ und lass andere Themen aus den Quellen weg. Behandle: Estimator, fit / predict / transform / fit_transform, score, Hyperparameter im Konstruktor, gelernte Attribute mit Unterstrich (coef_). Warum alle Modelle dieselbe Schnittstelle haben. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**2.2 Train/Test-Split & Data Leakage**
```
Erstelle die Übersicht ausschließlich zum Thema „Train/Test-Split und Data Leakage“ und lass andere Themen aus den Quellen weg. Behandle: warum getrennte Testdaten, stratify, Zeitreihen nicht zufällig mischen, typische Leaks (Skalierung vor dem Split, Zukunftsinformationen, Duplikate). Beispiel mit zu guten Ergebnissen. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**2.3 Vorverarbeitung**
```
Erstelle die Übersicht ausschließlich zum Thema „Daten vorbereiten“ und lass andere Themen aus den Quellen weg. Behandle: StandardScaler, MinMaxScaler, One-Hot- und Ordinal-Encoding, fehlende Werte mit SimpleImputer, Ausreißer. Welche Modelle Skalierung brauchen (kNN, SVM, lineare) und welche nicht (Bäume). Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**2.4 Pipelines & ColumnTransformer**
```
Erstelle die Übersicht ausschließlich zum Thema „Pipelines in scikit-learn“ und lass andere Themen aus den Quellen weg. Behandle: Vorverarbeitung und Modell als eine Einheit, ColumnTransformer für numerische vs. kategoriale Spalten, verhindert Leakage in der Kreuzvalidierung, Codebeispiel. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**2.5 Kreuzvalidierung**
```
Erstelle die Übersicht ausschließlich zum Thema „Kreuzvalidierung“ und lass andere Themen aus den Quellen weg. Behandle: k-Fold an einem Beispiel mit 5 Folds, in dem jeder Fold einmal Testdaten ist, Mittelwert und Streuung des Scores, StratifiedKFold, TimeSeriesSplit, warum ein einzelner Split täuschen kann. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**2.6 Klassifikationsmetriken**
```
Erstelle die Übersicht ausschließlich zum Thema „Accuracy, Precision, Recall, F1“ und lass andere Themen aus den Quellen weg. Behandle: Konfusionsmatrix (TP, FP, FN, TN), Accuracy-Falle bei unbalancierten Daten (99 % durch "immer negativ"), Precision vs. Recall am Spam- und Krebs-Beispiel, F1. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**2.7 ROC-Kurve & AUC**
```
Erstelle die Übersicht ausschließlich zum Thema „ROC und AUC“ und lass andere Themen aus den Quellen weg. Behandle: Schwellenwert verschieben, True-Positive-Rate vs. False-Positive-Rate, AUC als Wahrscheinlichkeit, dass ein positives Beispiel höher bewertet wird als ein negatives, Precision-Recall-Kurve bei seltenen Klassen. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**2.8 Regressionsmetriken**
```
Erstelle die Übersicht ausschließlich zum Thema „MSE, RMSE, MAE und R²“ und lass andere Themen aus den Quellen weg. Behandle: Bedeutung und Einheiten, R² als Anteil erklärter Varianz gegenüber der Mittelwert-Baseline, negatives R², Wahl der Metrik nach Fragestellung. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**2.9 Bias-Varianz-Tradeoff**
```
Erstelle die Übersicht ausschließlich zum Thema „Overfitting, Underfitting und der Bias-Varianz-Tradeoff“ und lass andere Themen aus den Quellen weg. Behandle: Polynome Grad 1, 4, 15 an verrauschte Daten, Trainings- vs. Testfehler über die Modellkomplexität (U-Kurve), Lernkurven, Gegenmittel. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**2.10 Hyperparameter-Suche**
```
Erstelle die Übersicht ausschließlich zum Thema „Hyperparameter finden“ und lass andere Themen aus den Quellen weg. Behandle: GridSearchCV vs. RandomizedSearchCV (warum Zufall oft besser ist), verschachtelte Kreuzvalidierung, Testdaten erst ganz am Ende, kurzer Ausblick auf Bayes'sche Optimierung (Optuna). Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

## Modul 3 – Lineare Modelle

**3.1 Lineare Regression**
```
Erstelle die Übersicht ausschließlich zum Thema „Lineare Regression“ und lass andere Themen aus den Quellen weg. Behandle: Modell ŷ = Xw + b, kleinste Quadrate, Normalengleichung w = (XᵀX)⁻¹Xᵀy vs. Gradientenabstieg, Interpretation der Koeffizienten, Annahmen und Residuenplot. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**3.2 Polynomielle Features**
```
Erstelle die Übersicht ausschließlich zum Thema „Polynomielle Regression“ und lass andere Themen aus den Quellen weg. Behandle: nichtlineare Zusammenhänge mit linearem Modell durch Features x, x², x³, PolynomialFeatures, Overfitting bei hohem Grad, Bezug zum Bias-Varianz-Tradeoff. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**3.3 Ridge, Lasso, Elastic Net**
```
Erstelle die Übersicht ausschließlich zum Thema „Regularisierung: Ridge, Lasso, Elastic Net“ und lass andere Themen aus den Quellen weg. Behandle: Strafterm λ‖w‖² vs. λ‖w‖₁, geometrisch Kreis vs. Raute (warum Lasso Gewichte exakt auf 0 setzt), Multikollinearität, Wahl von alpha per Kreuzvalidierung. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**3.4 Logistische Regression**
```
Erstelle die Übersicht ausschließlich zum Thema „Logistische Regression“ und lass andere Themen aus den Quellen weg. Behandle: Sigmoid macht aus w·x + b eine Wahrscheinlichkeit, Entscheidungsgrenze ist eine Gerade, Kreuzentropie als Verlust, Odds und Log-Odds, Koeffizienten deuten, Schwellenwert. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**3.5 Softmax-Regression**
```
Erstelle die Übersicht ausschließlich zum Thema „Mehrklassen-Klassifikation mit Softmax“ und lass andere Themen aus den Quellen weg. Behandle: ein Score pro Klasse, Softmax macht daraus Wahrscheinlichkeiten, kategoriale Kreuzentropie, One-vs-Rest im Vergleich, Grundlage der Ausgabeschicht neuronaler Netze. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**3.6 SGDClassifier & SGDRegressor**
```
Erstelle die Übersicht ausschließlich zum Thema „Lineare Modelle für große Daten mit SGD“ und lass andere Themen aus den Quellen weg. Behandle: SGDClassifier/SGDRegressor, verschiedene loss-Parameter (hinge, log_loss, squared_error), partial_fit für Daten, die nicht in den Speicher passen, Skalierung ist Pflicht. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

## Modul 4 – Nachbarn & Wahrscheinlichkeiten

**4.1 k-Nächste-Nachbarn**
```
Erstelle die Übersicht ausschließlich zum Thema „k-Nächste-Nachbarn“ und lass andere Themen aus den Quellen weg. Behandle: Klassifikation durch Mehrheitsentscheid der k nächsten Punkte, Einfluss von k (k=1 Overfitting), Distanzgewichtung, kNN-Regression, faules Lernen: Training kostet nichts, Vorhersage viel. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**4.2 Fluch der Dimensionalität**
```
Erstelle die Übersicht ausschließlich zum Thema „Der Fluch der Dimensionalität“ und lass andere Themen aus den Quellen weg. Behandle: in hohen Dimensionen sind alle Punkte fast gleich weit entfernt, Volumen wandert in die Ecken des Würfels, Datenbedarf explodiert. Folgen für kNN und Clustering, Gegenmittel Feature-Auswahl und PCA. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**4.3 Naive Bayes**
```
Erstelle die Übersicht ausschließlich zum Thema „Naive Bayes“ und lass andere Themen aus den Quellen weg. Behandle: Satz von Bayes für Klassifikation, naive Unabhängigkeitsannahme, Gauß-, Multinomial- und Bernoulli-Variante, Spamfilter Schritt für Schritt mit Wortwahrscheinlichkeiten, Laplace-Glättung. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**4.4 LDA & QDA**
```
Erstelle die Übersicht ausschließlich zum Thema „Lineare und quadratische Diskriminanzanalyse“ und lass andere Themen aus den Quellen weg. Behandle: jede Klasse als Normalverteilung, gemeinsame Kovarianz → lineare Grenze (LDA), eigene Kovarianz → quadratische Grenze (QDA), LDA auch zur Dimensionsreduktion. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

## Modul 5 – Support Vector Machines

**5.1 Maximaler Rand (Hard Margin)**
```
Erstelle die Übersicht ausschließlich zum Thema „Support Vector Machines: der maximale Rand“ und lass andere Themen aus den Quellen weg. Behandle: viele trennende Geraden möglich, SVM wählt die mit dem breitesten Korridor, Stützvektoren bestimmen allein die Grenze, Randbreite 2/‖w‖. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**5.2 Soft Margin & Parameter C**
```
Erstelle die Übersicht ausschließlich zum Thema „Soft Margin und der Parameter C“ und lass andere Themen aus den Quellen weg. Behandle: Schlupfvariablen erlauben Fehler, großes C = harte Grenze/Overfitting, kleines C = breiter Rand/mehr Fehler, Hinge Loss max(0, 1 − y·f(x)) im Vergleich zur Kreuzentropie. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**5.3 Der Kernel-Trick**
```
Erstelle die Übersicht ausschließlich zum Thema „Der Kernel-Trick“ und lass andere Themen aus den Quellen weg. Behandle: Kreis-Daten in 2D nicht linear trennbar, Abbildung in 3D (z = x² + y²) macht sie trennbar, Kernel berechnet Skalarprodukte im hohen Raum ohne ihn zu betreten, polynomialer Kernel. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**5.4 RBF-Kernel & gamma**
```
Erstelle die Übersicht ausschließlich zum Thema „RBF-Kernel und gamma“ und lass andere Themen aus den Quellen weg. Behandle: Ähnlichkeit als Glockenkurve um jeden Stützvektor, kleines gamma = glatte Grenze, großes gamma = Inseln/Overfitting, Zusammenspiel von C und gamma, Grid Search, Skalierung zwingend. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**5.5 Support Vector Regression**
```
Erstelle die Übersicht ausschließlich zum Thema „Support Vector Regression“ und lass andere Themen aus den Quellen weg. Behandle: ε-Schlauch um die Funktion, Punkte im Schlauch kosten nichts, nur Punkte außerhalb sind Stützvektoren, Kernel für nichtlineare Regression, Parameter epsilon und C. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

## Modul 6 – Entscheidungsbäume & Ensembles

**6.1 Entscheidungsbaum**
```
Erstelle die Übersicht ausschließlich zum Thema „Entscheidungsbäume“ und lass andere Themen aus den Quellen weg. Behandle: Daten durch Ja/Nein-Fragen aufteilen, achsenparallele Grenzen, Gini-Unreinheit und Entropie, Information Gain, wie der beste Split gesucht wird, Regressionsbaum mit Varianzreduktion. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**6.2 Pruning & Baumtiefe**
```
Erstelle die Übersicht ausschließlich zum Thema „Bäume zähmen“ und lass andere Themen aus den Quellen weg. Behandle: ein unbegrenzter Baum lernt jeden Punkt auswendig, max_depth, min_samples_leaf, Cost-Complexity-Pruning (ccp_alpha), Instabilität einzelner Bäume als Motivation für Ensembles. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**6.3 Bagging & Random Forest**
```
Erstelle die Übersicht ausschließlich zum Thema „Random Forest“ und lass andere Themen aus den Quellen weg. Behandle: Bootstrap-Stichproben, viele Bäume, Mehrheitsentscheid; zusätzliche Zufallsauswahl von Features pro Split (max_features) entkoppelt die Bäume; Mitteln reduziert Varianz; Out-of-Bag-Fehler. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**6.4 Extra Trees**
```
Erstelle die Übersicht ausschließlich zum Thema „Extremely Randomized Trees“ und lass andere Themen aus den Quellen weg. Behandle: Split-Schwellen zufällig statt optimal, noch weniger Varianz, schneller zu trainieren, Vergleich mit Random Forest an einem Beispiel. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**6.5 AdaBoost**
```
Erstelle die Übersicht ausschließlich zum Thema „AdaBoost Schritt für Schritt“ und lass andere Themen aus den Quellen weg. Behandle: schwache Lerner (Baumstümpfe) nacheinander, falsch klassifizierte Punkte bekommen mehr Gewicht, jeder Lerner erhält ein Stimmgewicht, gewichtete Abstimmung am Ende. Gehe 3 Runden an einem kleinen Beispiel durch. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**6.6 Gradient Boosting**
```
Erstelle die Übersicht ausschließlich zum Thema „Gradient Boosting“ und lass andere Themen aus den Quellen weg. Behandle: Start mit dem Mittelwert, jeder neue Baum lernt die Residuen des bisherigen Modells, Lernrate (Shrinkage) dämpft jeden Schritt; Residuen sind der negative Gradient des MSE – daher der Name; andere Losses (Log Loss, Huber) über ihren Gradienten. Gehe 4 Runden an einem kleinen Zahlenbeispiel durch. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**6.7 Gradient Boosting in der Praxis**
```
Erstelle die Übersicht ausschließlich zum Thema „HistGradientBoosting, XGBoost, LightGBM, CatBoost“ und lass andere Themen aus den Quellen weg. Behandle: Histogramm-Binning für Geschwindigkeit, wichtige Hyperparameter (learning_rate, n_estimators, max_depth, subsample), Early Stopping, Regularisierung, Besonderheiten der vier Bibliotheken, warum sie Tabellendaten dominieren. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**6.8 Stacking & Voting**
```
Erstelle die Übersicht ausschließlich zum Thema „Modelle kombinieren: Voting und Stacking“ und lass andere Themen aus den Quellen weg. Behandle: harte und weiche Abstimmung, Stacking mit einem Meta-Modell auf Out-of-Fold-Vorhersagen, warum unterschiedliche Modelle sich ergänzen. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**6.9 Feature Importance**
```
Erstelle die Übersicht ausschließlich zum Thema „Welche Features sind wichtig?“ und lass andere Themen aus den Quellen weg. Behandle: Impurity-basierte Importance und ihre Schwächen (bevorzugt Features mit vielen Werten), Permutation Importance auf Testdaten, korrelierte Features teilen sich die Wichtigkeit. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

## Modul 7 – Unüberwachtes Lernen

**7.1 k-Means & k-Means++**
```
Erstelle die Übersicht ausschließlich zum Thema „k-Means“ und lass andere Themen aus den Quellen weg. Behandle: Zentren zufällig setzen, Punkte dem nächsten Zentrum zuordnen, Zentren neu berechnen, wiederholen, an einem kleinen Beispiel Runde für Runde; Inertia; schlechte Starts und k-Means++; Elbow-Methode; Grenzen bei nicht-runden Clustern. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**7.2 Hierarchisches Clustering**
```
Erstelle die Übersicht ausschließlich zum Thema „Hierarchisches Clustering“ und lass andere Themen aus den Quellen weg. Behandle: agglomerativ von unten, Linkage-Varianten (single, complete, average, Ward), Dendrogramm lesen und an einer Höhe abschneiden. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**7.3 DBSCAN & HDBSCAN**
```
Erstelle die Übersicht ausschließlich zum Thema „DBSCAN“ und lass andere Themen aus den Quellen weg. Behandle: dichtebasierte Cluster, Parameter eps und min_samples, Kern-, Rand- und Rauschpunkte, findet beliebige Formen (Halbmonde) und Ausreißer, HDBSCAN für unterschiedliche Dichten. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**7.4 Gaussian Mixture Models & EM**
```
Erstelle die Übersicht ausschließlich zum Thema „Gaussian Mixture Models und der EM-Algorithmus“ und lass andere Themen aus den Quellen weg. Behandle: Daten als Mischung von Glockenkurven, weiche Zuordnung, E-Schritt (Wahrscheinlichkeiten) und M-Schritt (Parameter) im Wechsel an einem Beispiel, Vergleich mit k-Means, Modellwahl mit BIC. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**7.5 PCA**
```
Erstelle die Übersicht ausschließlich zum Thema „Hauptkomponentenanalyse (PCA)“ und lass andere Themen aus den Quellen weg. Behandle: Richtung maximaler Varianz finden, Projektion auf wenige Achsen, Eigenvektoren der Kovarianzmatrix, erklärte Varianz, Daten vorher standardisieren, Anwendung Visualisierung und Kompression. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**7.6 t-SNE & UMAP**
```
Erstelle die Übersicht ausschließlich zum Thema „t-SNE und UMAP“ und lass andere Themen aus den Quellen weg. Behandle: nichtlineare Einbettung, Nachbarschaften erhalten statt Distanzen, Perplexity bzw. n_neighbors, Fallen beim Interpretieren (Clustergrößen und Abstände bedeuten nichts), MNIST-Beispiel. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**7.7 Cluster bewerten**
```
Erstelle die Übersicht ausschließlich zum Thema „Wie gut sind meine Cluster?“ und lass andere Themen aus den Quellen weg. Behandle: Silhouette-Koeffizient Schritt für Schritt (a und b eines Punktes), Davies-Bouldin, Calinski-Harabasz, Adjusted Rand Index wenn Labels bekannt sind, warum es keine absolute Wahrheit gibt. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

## Modul 8 – Anomalieerkennung

**8.1 Statistische Ausreißererkennung**
```
Erstelle die Übersicht ausschließlich zum Thema „Ausreißer statistisch finden“ und lass andere Themen aus den Quellen weg. Behandle: z-Score mit Schwelle 3, IQR-Regel und Boxplot (1,5 · IQR), robuste Variante mit Median und MAD, Grenzen bei mehreren Dimensionen. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**8.2 Isolation Forest: die Idee**
```
Erstelle die Übersicht ausschließlich zum Thema „Isolation Forest: wie Isolation funktioniert“ und lass andere Themen aus den Quellen weg. Behandle: zufälliges Feature und zufälliger Schnitt zwischen Min und Max, so lange teilen, bis ein Punkt allein ist; Ausreißer werden nach wenigen Schnitten isoliert, normale Punkte brauchen viele. Vergleiche Schritt für Schritt, wie ein Ausreißer und ein normaler Punkt isoliert werden. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**8.3 Isolation Forest: Pfadlänge & Score**
```
Erstelle die Übersicht ausschließlich zum Thema „Isolation Forest: Pfadlänge und Anomalie-Score“ und lass andere Themen aus den Quellen weg. Behandle: viele Isolationsbäume auf Teilstichproben (max_samples = 256), mittlere Pfadlänge h(x), Normierung mit c(n), Score s = 2^(−E[h(x)]/c(n)) – nahe 1 = Anomalie, ≤ 0,5 = normal; contamination-Parameter; Stärken und Schwächen. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**8.4 Local Outlier Factor**
```
Erstelle die Übersicht ausschließlich zum Thema „Local Outlier Factor (LOF)“ und lass andere Themen aus den Quellen weg. Behandle: lokale Dichte eines Punktes im Vergleich zu seinen Nachbarn, Erreichbarkeitsdistanz, LOF ≈ 1 normal, deutlich > 1 Ausreißer; findet lokale Ausreißer neben dichten Clustern, wo globale Methoden versagen. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**8.5 One-Class SVM**
```
Erstelle die Übersicht ausschließlich zum Thema „One-Class SVM“ und lass andere Themen aus den Quellen weg. Behandle: nur normale Daten lernen, Grenze um die Datenwolke mit RBF-Kernel, Parameter nu als Obergrenze für den Ausreißeranteil, Skalierung nötig, Vergleich mit Isolation Forest. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**8.6 Elliptic Envelope**
```
Erstelle die Übersicht ausschließlich zum Thema „Elliptic Envelope“ und lass andere Themen aus den Quellen weg. Behandle: Daten als Normalverteilung annehmen, robuste Kovarianzschätzung (Minimum Covariance Determinant), Mahalanobis-Distanz statt euklidischer Distanz, funktioniert nur für ungefähr ellipsenförmige Daten. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**8.7 Projekt Kreditkartenbetrug**
```
Erstelle die Übersicht ausschließlich zum Thema „Betrug erkennen – ein Projekt von Anfang bis Ende“ und lass andere Themen aus den Quellen weg. Behandle: extrem unbalancierte Daten (0,17 % Betrug), warum Accuracy nutzlos ist, Isolation Forest vs. überwachtes Gradient Boosting, Precision-Recall-Kurve, Schwellenwert nach Kosten von Fehlalarm vs. übersehenem Betrug wählen. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

## Modul 9 – Neuronale Netze

**9.1 Perzeptron & Neuron**
```
Erstelle die Übersicht ausschließlich zum Thema „Das künstliche Neuron“ und lass andere Themen aus den Quellen weg. Behandle: gewichtete Summe plus Bias, Aktivierungsfunktion, Perzeptron-Lernregel, Grenze: XOR ist nicht linear trennbar – Motivation für mehrere Schichten. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**9.2 Aktivierungsfunktionen**
```
Erstelle die Übersicht ausschließlich zum Thema „Aktivierungsfunktionen“ und lass andere Themen aus den Quellen weg. Behandle: warum Nichtlinearität nötig ist (sonst kollabieren alle Schichten zu einer linearen Abbildung), Sigmoid, tanh, ReLU, Leaky ReLU, GELU, verschwindende Gradienten, Softmax am Ausgang. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**9.3 Forward Pass**
```
Erstelle die Übersicht ausschließlich zum Thema „Wie ein neuronales Netz rechnet“ und lass andere Themen aus den Quellen weg. Behandle: Schichten als Matrixmultiplikation plus Aktivierung, ein kleines Netz 2-3-1 mit konkreten Zahlen durchrechnen, wie Schichten den Raum schrittweise verformen, bis die Daten linear trennbar sind. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**9.4 Backpropagation**
```
Erstelle die Übersicht ausschließlich zum Thema „Backpropagation Schritt für Schritt“ und lass andere Themen aus den Quellen weg. Behandle: Verlust berechnen, Kettenregel rückwärts durch das Netz, lokale Gradienten an jedem Knoten, Gradient für jedes Gewicht, Update mit Gradientenabstieg. Ein Mini-Netz mit konkreten Zahlen. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**9.5 MLPClassifier in scikit-learn**
```
Erstelle die Übersicht ausschließlich zum Thema „Neuronale Netze mit scikit-learn“ und lass andere Themen aus den Quellen weg. Behandle: MLPClassifier und MLPRegressor, hidden_layer_sizes, Aktivierung, Solver adam, alpha (L2), Early Stopping, Skalierung, Grenzen gegenüber PyTorch. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**9.6 Einführung in PyTorch**
```
Erstelle die Übersicht ausschließlich zum Thema „PyTorch in 10 Minuten“ und lass andere Themen aus den Quellen weg. Behandle: Tensoren, autograd mit requires_grad und backward, nn.Module, Optimizer, die Trainingsschleife (zero_grad, forward, loss, backward, step), DataLoader, GPU. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

## Modul 10 – Deep Learning

**10.1 Optimierer**
```
Erstelle die Übersicht ausschließlich zum Thema „SGD, Momentum, RMSProp, Adam“ und lass andere Themen aus den Quellen weg. Behandle: Momentum als rollende Kugel dämpft Zickzack, adaptive Lernraten pro Parameter, Adam kombiniert beides, Lernraten-Schedules und Warmup, Pfade im langgezogenen Tal im Vergleich. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**10.2 Initialisierung, BatchNorm, Dropout**
```
Erstelle die Übersicht ausschließlich zum Thema „Tiefe Netze stabil trainieren“ und lass andere Themen aus den Quellen weg. Behandle: Xavier- und He-Initialisierung, explodierende und verschwindende Gradienten, Batch- und Layer-Normalisierung, Dropout als Regularisierung, Weight Decay, Residualverbindungen. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**10.3 CNNs**
```
Erstelle die Übersicht ausschließlich zum Thema „Convolutional Neural Networks“ und lass andere Themen aus den Quellen weg. Behandle: Faltungsfilter gleitet über das Bild (mit kleinem Zahlenbeispiel), Feature Maps, Padding und Stride, Pooling, Hierarchie von Kanten zu Formen zu Objekten, Parameterteilung, LeNet bis ResNet. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**10.4 RNNs, LSTM & GRU**
```
Erstelle die Übersicht ausschließlich zum Thema „Rekurrente Netze, LSTM und GRU“ und lass andere Themen aus den Quellen weg. Behandle: versteckter Zustand trägt Information durch die Sequenz, Ausrollen über die Zeit, verschwindende Gradienten, Gates der LSTM (Vergessen, Eingabe, Ausgabe), GRU als vereinfachte Form. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**10.5 Transfer Learning**
```
Erstelle die Übersicht ausschließlich zum Thema „Transfer Learning“ und lass andere Themen aus den Quellen weg. Behandle: vortrainiertes Netz (z. B. auf ImageNet) wiederverwenden, frühe Schichten einfrieren, neuen Kopf trainieren, Fine-Tuning mit kleiner Lernrate, warum das mit wenig Daten funktioniert. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**10.6 Autoencoder & VAEs**
```
Erstelle die Übersicht ausschließlich zum Thema „Autoencoder und Variational Autoencoder“ und lass andere Themen aus den Quellen weg. Behandle: Encoder komprimiert, Decoder rekonstruiert, Flaschenhals als Merkmalsraum, Anomalieerkennung über den Rekonstruktionsfehler, VAE mit Verteilung im latenten Raum und Reparametrisierungs-Trick, neue Daten erzeugen. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**10.7 GANs & Diffusionsmodelle**
```
Erstelle die Übersicht ausschließlich zum Thema „Wie KI Bilder erzeugt: GANs und Diffusion“ und lass andere Themen aus den Quellen weg. Behandle: Generator gegen Diskriminator, Mode Collapse; Diffusion: Bild schrittweise verrauschen und ein Netz lernt das Entrauschen, Text-Konditionierung, warum Diffusion heute dominiert. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

## Modul 11 – Moderne KI: Transformer & LLMs

**11.1 Word Embeddings**
```
Erstelle die Übersicht ausschließlich zum Thema „Word Embeddings“ und lass andere Themen aus den Quellen weg. Behandle: Wörter als Vektoren, ähnliche Bedeutung = ähnliche Richtung, König − Mann + Frau ≈ Königin, Word2Vec-Idee (Wort aus Kontext vorhersagen), Kosinus-Ähnlichkeit, kontextabhängige Embeddings. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**11.2 Attention**
```
Erstelle die Übersicht ausschließlich zum Thema „Der Attention-Mechanismus“ und lass andere Themen aus den Quellen weg. Behandle: Query, Key, Value; Skalarprodukt Query·Key als Relevanz, Softmax zu Gewichten, gewichtete Summe der Values; Beispiel "Die Bank am Fluss" vs. "die Bank gibt Kredit"; Skalierung mit √d. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**11.3 Transformer-Architektur**
```
Erstelle die Übersicht ausschließlich zum Thema „Der Transformer“ und lass andere Themen aus den Quellen weg. Behandle: Self-Attention, Multi-Head-Attention, Positionskodierung, Feed-Forward-Schicht, Residualverbindungen und LayerNorm, Encoder vs. Decoder, kausale Maske, warum parallelisierbar im Gegensatz zu RNNs. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**11.4 Tokenisierung**
```
Erstelle die Übersicht ausschließlich zum Thema „Tokenisierung“ und lass andere Themen aus den Quellen weg. Behandle: Text in Tokens zerlegen, Byte-Pair-Encoding Schritt für Schritt, Vokabulargröße, warum LLMs mit Buchstaben zählen und seltenen Wörtern Probleme haben, Tokens und Kosten. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**11.5 Pretraining, Fine-Tuning, RLHF**
```
Erstelle die Übersicht ausschließlich zum Thema „Wie ein Sprachmodell entsteht“ und lass andere Themen aus den Quellen weg. Behandle: Pretraining durch Vorhersage des nächsten Tokens auf riesigen Textmengen, Supervised Fine-Tuning mit Beispieldialogen, RLHF/Präferenzlernen, Parameter-effizientes Fine-Tuning (LoRA). Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**11.6 LLMs & Prompting**
```
Erstelle die Übersicht ausschließlich zum Thema „Large Language Models nutzen“ und lass andere Themen aus den Quellen weg. Behandle: Erzeugung Token für Token, Temperatur und Sampling, Kontextfenster, Halluzinationen, Prompting-Techniken (Rolle, Beispiele, Schritt-für-Schritt), Grenzen. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**11.7 RAG**
```
Erstelle die Übersicht ausschließlich zum Thema „Retrieval Augmented Generation (RAG)“ und lass andere Themen aus den Quellen weg. Behandle: Dokumente in Abschnitte teilen, Embeddings in einer Vektordatenbank, ähnlichste Abschnitte zur Frage suchen, in den Prompt geben, Antwort mit Quellen; typische Fehlerquellen und Bewertung. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

## Modul 12 – Reinforcement Learning

**12.1 Agent, Umgebung, Belohnung**
```
Erstelle die Übersicht ausschließlich zum Thema „Reinforcement Learning: die Grundidee“ und lass andere Themen aus den Quellen weg. Behandle: Agent, Zustand, Aktion, Belohnung, Policy, Episode, Exploration vs. Exploitation (ε-greedy), Mehrarmiger Bandit als einfachstes Beispiel. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**12.2 Markov-Entscheidungsprozesse**
```
Erstelle die Übersicht ausschließlich zum Thema „Markov-Entscheidungsprozesse“ und lass andere Themen aus den Quellen weg. Behandle: Zustände, Übergangswahrscheinlichkeiten, Belohnungen, Diskontfaktor γ, Return, Wertfunktion V und Q, Bellman-Gleichung an einer kleinen Gitterwelt. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**12.3 Q-Learning**
```
Erstelle die Übersicht ausschließlich zum Thema „Q-Learning“ und lass andere Themen aus den Quellen weg. Behandle: Q-Tabelle, Update Q ← Q + α(r + γ·max Q' − Q), Agent lernt in einer Gitterwelt den Weg zum Ziel und meidet Fallen und wird von Episode zu Episode besser, Off-Policy-Lernen. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**12.4 Deep Q-Networks**
```
Erstelle die Übersicht ausschließlich zum Thema „Deep Q-Networks“ und lass andere Themen aus den Quellen weg. Behandle: neuronales Netz statt Tabelle für große Zustandsräume, Experience Replay, Target Network, Atari-Beispiel, Instabilitäten. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**12.5 Policy Gradients**
```
Erstelle die Übersicht ausschließlich zum Thema „Policy Gradients“ und lass andere Themen aus den Quellen weg. Behandle: Policy direkt als Netz, Wahrscheinlichkeit guter Aktionen erhöhen (REINFORCE), Baseline zur Varianzreduktion, Actor-Critic, PPO in einem Satz, Bezug zu RLHF bei Sprachmodellen. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

## Modul 13 – ML in der Praxis (MLOps)

**13.1 Feature Engineering**
```
Erstelle die Übersicht ausschließlich zum Thema „Feature Engineering“ und lass andere Themen aus den Quellen weg. Behandle: Domänenwissen in Features übersetzen, Datums- und Zeitfeatures, zyklische Kodierung mit sin/cos, Interaktionen, Verhältnisse, Aggregationen, Target-Encoding und seine Leakage-Gefahr. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**13.2 Unbalancierte Daten**
```
Erstelle die Übersicht ausschließlich zum Thema „Unbalancierte Daten“ und lass andere Themen aus den Quellen weg. Behandle: Klassengewichte (class_weight), Under- und Oversampling, SMOTE, Schwellenwert anpassen statt Daten verändern, passende Metriken (PR-AUC), Resampling nur auf Trainingsdaten. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**13.3 Interpretierbarkeit mit SHAP**
```
Erstelle die Übersicht ausschließlich zum Thema „Modelle erklären mit SHAP“ und lass andere Themen aus den Quellen weg. Behandle: Shapley-Werte aus der Spieltheorie (fairer Anteil jedes Features), lokale Erklärung einer Vorhersage (Wasserfall), globale Übersicht (Beeswarm), Partial Dependence, Grenzen bei korrelierten Features. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**13.4 Modelle speichern & ausliefern**
```
Erstelle die Übersicht ausschließlich zum Thema „Ein Modell in Produktion bringen“ und lass andere Themen aus den Quellen weg. Behandle: Pipeline mit joblib speichern, Versionen fixieren, REST-API mit FastAPI, Docker, Batch- vs. Echtzeit-Vorhersagen, ONNX, Modell- und Datenversionierung. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**13.5 Monitoring & Data Drift**
```
Erstelle die Übersicht ausschließlich zum Thema „Wenn sich die Welt ändert: Data Drift“ und lass andere Themen aus den Quellen weg. Behandle: Data Drift vs. Concept Drift, Verteilungen vergleichen (PSI, Kolmogorov-Smirnov), Performance überwachen wenn Labels verzögert kommen, Retraining-Strategien. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```

**13.6 Fairness & Ethik**
```
Erstelle die Übersicht ausschließlich zum Thema „Fairness in Machine Learning“ und lass andere Themen aus den Quellen weg. Behandle: Verzerrungen in Daten (historisch, Stichprobe, Messung), Fairness-Definitionen (Demographic Parity, Equalized Odds) und warum sie sich widersprechen, Proxy-Variablen, Datenschutz, EU AI Act in einem Satz. Aufbau: zuerst Intuition mit einem Alltagsbeispiel, dann die Mathematik Schritt für Schritt, zum Schluss die drei wichtigsten Kernaussagen. Zielgruppe: Lernende mit Programmier- und Abitur-Mathe-Kenntnissen. Sprache: Deutsch, Fachbegriffe zusätzlich auf Englisch.
```
