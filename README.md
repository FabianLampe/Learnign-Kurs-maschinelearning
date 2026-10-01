# Machine Learning – von vorne bis hinten

Ein deutschsprachiger Kurs von den mathematischen Grundlagen über scikit-learn und jedes klassische Modell (inkl. Gradient Boosting
und Isolation Forest) bis zu Deep Learning, Transformern und Reinforcement Learning.

Jede Lektion folgt demselben Muster: **Intuition & Animation → Mathematik → Code**.

| Baustein | Wo |
|---|---|
| 🌐 Lektionen mit interaktiven Animationen, Formeln und Quizzen | `website/` |
| 🎬 Erklärvideos (Manim) | in die Lektionen eingebettet, Quellcode in `videos/` |
| 💻 Übungs-Notebooks mit Lückencode | `notebooks/modul-XX/` |
| ✅ Lösungen (ausgeführt, mit Ausgaben) | `notebooks/modul-XX/loesungen/` |
| 🛠 Mini-Projekt pro Modul | Projektseite + Notebook |
| 📝 Notizbuch mit automatischem Inhaltsverzeichnis | Seitenleiste auf jeder Seite |
| 🎥 Video-Prompts für alle 96 Themen (z. B. für LM Studio) | `prompts/video-prompts.md` |

## Loslegen

### 1. Website öffnen

Öffne einfach `website/index.html` im Browser (Doppelklick). Es wird kein Internet benötigt – Formeln (KaTeX) und Videos liegen lokal.
Dein Fortschritt (erledigte Lektionen, Quiz-Ergebnisse) wird im Browser gespeichert.

**Notizen:** Über „📝 Notizen“ oben rechts (oder <kbd>Strg</kbd>+<kbd>Shift</kbd>+<kbd>N</kbd>) öffnest du auf jeder Seite dein Notizbuch.
Zeilen wie `1. Titel`, `2. Titel` oder `1.1 Unterpunkt` werden automatisch zum anklickbaren Inhaltsverzeichnis.
„+ Lektion als Überschrift“ fügt die aktuelle Lektion als nächste Nummer ein. Die Notizen liegen nur in deinem Browser –
sichere sie ab und zu mit „Exportieren“ als Markdown-Datei.

> Falls dein Browser den Fortschritt bei `file://`-Seiten nicht speichert (manche Firefox-Einstellungen), starte einen lokalen Server:
> ```bash
> cd website
> python -m http.server 8000
> ```
> und öffne <http://localhost:8000>.

### 2. Python-Umgebung für die Notebooks

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook notebooks/
```

Arbeite die Notebooks parallel zu den Lektionen durch. Zellen mit `# TODO` sind deine Aufgaben; steckst du fest, hilft die Lösung im Ordner `loesungen/`.

## Lehrplan

| Modul | Thema | Status |
|---|---|---|
| 1 | **Grundlagen & Mathe** – Was ist ML, Vektoren & Matrizen, Statistik & Wahrscheinlichkeit, Ableitungen & Gradienten, Verlustfunktionen & Gradientenabstieg | ✅ verfügbar |
| 2 | Daten & der scikit-learn-Workflow – Pipelines, Kreuzvalidierung, Metriken, Bias-Varianz, Hyperparameter-Suche | geplant |
| 3 | Lineare Modelle – lineare & logistische Regression, Ridge, Lasso, Elastic Net, Softmax | geplant |
| 4 | Nachbarn & Wahrscheinlichkeiten – kNN, Naive Bayes, LDA/QDA | geplant |
| 5 | Support Vector Machines – Margin, Hinge Loss, Kernel-Trick, SVR | geplant |
| 6 | Entscheidungsbäume & Ensembles – Bäume, Random Forest, AdaBoost, **Gradient Boosting**, XGBoost/LightGBM/CatBoost, Stacking | geplant |
| 7 | Unüberwachtes Lernen – k-Means, hierarchisch, DBSCAN, GMM, PCA, t-SNE/UMAP | geplant |
| 8 | Anomalieerkennung – **Isolation Forest** im Detail, LOF, One-Class SVM, Projekt Betrugserkennung | geplant |
| 9 | Neuronale Netze – Perzeptron, Backpropagation, MLP, Einführung PyTorch | geplant |
| 10 | Deep Learning – Optimierer, Regularisierung, CNNs, RNNs/LSTM, Autoencoder, GANs & Diffusion | geplant |
| 11 | Moderne KI – Embeddings, Attention, Transformer, LLMs, RAG | geplant |
| 12 | Reinforcement Learning – MDPs, Q-Learning, DQN, Policy Gradients | geplant |
| 13 | ML in der Praxis – Feature Engineering, unbalancierte Daten, SHAP, Deployment, Monitoring, Fairness | geplant |

Die vollständige Themenliste je Modul steht in `website/assets/js/course.js` und auf der Startseite der Website.

## Projektstruktur

```
website/
  index.html                 Kursübersicht mit Fortschritt
  modul-01/                  Lektionen + Projektseite
  assets/css/style.css       Design (Dark/Light)
  assets/js/app.js           Navigation, Fortschritt, Quiz-Engine, Plot-Helfer
  assets/js/course.js        Kursstruktur (eine Quelle für alles)
  assets/js/anim/            interaktive Animationen pro Lektion
  assets/videos/             gerenderte Erklärvideos
  assets/vendor/katex/       Formelsatz (lokal, MIT-Lizenz)
notebooks/modul-01/          Übungen + loesungen/
videos/modul-01/szenen.py    Manim-Quellcode der Videos
tools/                       Generator für die Notebooks
```

## Für Mitwirkende: Notebooks neu erzeugen

Übungs- und Lösungsnotebooks werden aus **einer** Quelle erzeugt (`tools/modul01_notebooks.py`), damit sie nie auseinanderlaufen:

```bash
pip install -r requirements.txt nbconvert
python tools/build_all.py --execute   # erzeugt alle Notebooks und führt die Lösungen zur Kontrolle aus
```

In der Quelle markiert `# >>> Aufgabentext` … `# <<<` einen Lösungsblock; Zeilen mit `#!` erscheinen nur in der Übungsversion.
