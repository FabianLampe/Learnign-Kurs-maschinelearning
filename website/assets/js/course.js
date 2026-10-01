// Kursstruktur: einzige Quelle für Navigation, Übersicht und Fortschritt.
// status: "fertig" = Inhalte vorhanden, "geplant" = kommt in einer späteren Ausbaustufe.
window.COURSE = {
  title: "Machine Learning – von vorne bis hinten",
  modules: [
    {
      id: "m01",
      nr: 1,
      title: "Grundlagen & Mathe",
      subtitle: "Was ML ist, und die Mathematik, auf der alles aufbaut",
      status: "fertig",
      dir: "modul-01",
      lessons: [
        { id: "m01-l01", file: "lektion-01.html", title: "Was ist Machine Learning?", minutes: 25 },
        { id: "m01-l02", file: "lektion-02.html", title: "Vektoren, Matrizen & Daten", minutes: 35 },
        { id: "m01-l03", file: "lektion-03.html", title: "Statistik & Wahrscheinlichkeit", minutes: 40 },
        { id: "m01-l04", file: "lektion-04.html", title: "Ableitungen & Gradienten", minutes: 35 },
        { id: "m01-l05", file: "lektion-05.html", title: "Verlustfunktionen & Gradientenabstieg", minutes: 45 },
        { id: "m01-p01", file: "projekt.html", title: "Mini-Projekt: Regression von Hand", minutes: 60, project: true }
      ]
    },
    {
      id: "m02", nr: 2, title: "Daten & der scikit-learn-Workflow", status: "geplant",
      subtitle: "Vom Rohdatensatz zur sauberen, reproduzierbaren Pipeline",
      topics: ["Die scikit-learn-API: fit / predict / transform", "Train/Test-Split, Data Leakage", "Skalierung, Encoding, fehlende Werte",
        "Pipelines & ColumnTransformer", "Kreuzvalidierung (Cross-Validation)", "Metriken: Accuracy, Precision, Recall, F1, ROC-AUC, MSE, R²",
        "Bias-Varianz-Tradeoff, Over-/Underfitting", "Hyperparameter-Suche: GridSearchCV, RandomizedSearchCV"]
    },
    {
      id: "m03", nr: 3, title: "Lineare Modelle", status: "geplant",
      subtitle: "Die Arbeitspferde des Machine Learning",
      topics: ["Lineare Regression (Normalengleichung vs. Gradient Descent)", "Polynomielle Features", "Regularisierung: Ridge (L2), Lasso (L1), Elastic Net",
        "Logistische Regression & Sigmoid", "Softmax-Regression (Multiklassen)", "SGDClassifier / SGDRegressor"]
    },
    {
      id: "m04", nr: 4, title: "Nachbarn & Wahrscheinlichkeiten", status: "geplant",
      subtitle: "Instanzbasierte und probabilistische Modelle",
      topics: ["k-Nächste-Nachbarn (kNN)", "Distanzmaße & Fluch der Dimensionalität", "Naive Bayes (Gauß, Multinomial, Bernoulli)",
        "Lineare & Quadratische Diskriminanzanalyse (LDA/QDA)"]
    },
    {
      id: "m05", nr: 5, title: "Support Vector Machines", status: "geplant",
      subtitle: "Maximale Trennränder und der Kernel-Trick",
      topics: ["Hard & Soft Margin", "Hinge Loss", "Kernel-Trick: polynomial, RBF", "SVR (Regression)", "Parameter C und gamma"]
    },
    {
      id: "m06", nr: 6, title: "Entscheidungsbäume & Ensembles", status: "geplant",
      subtitle: "Bäume, Wälder und Boosting – im Detail",
      topics: ["Entscheidungsbaum: Gini, Entropie, Information Gain", "Pruning & Baumtiefe", "Bagging & Random Forest", "Extra Trees",
        "AdaBoost Schritt für Schritt", "Gradient Boosting: Residuen, Shrinkage, Loss-Gradienten", "HistGradientBoosting, XGBoost, LightGBM, CatBoost",
        "Stacking & Voting", "Feature Importance & Permutation Importance"]
    },
    {
      id: "m07", nr: 7, title: "Unüberwachtes Lernen", status: "geplant",
      subtitle: "Struktur in Daten ohne Labels finden",
      topics: ["k-Means & k-Means++", "Hierarchisches Clustering", "DBSCAN & HDBSCAN", "Gaussian Mixture Models & EM-Algorithmus",
        "PCA (Hauptkomponentenanalyse)", "t-SNE & UMAP", "Silhouette-Score & Cluster-Bewertung"]
    },
    {
      id: "m08", nr: 8, title: "Anomalieerkennung", status: "geplant",
      subtitle: "Ausreißer und Betrug finden",
      topics: ["Statistische Verfahren (z-Score, IQR)", "Isolation Forest: wie genau die Isolation funktioniert", "Pfadlänge & Anomalie-Score",
        "Local Outlier Factor (LOF)", "One-Class SVM", "Elliptic Envelope", "Projekt: Kreditkartenbetrug erkennen"]
    },
    {
      id: "m09", nr: 9, title: "Neuronale Netze", status: "geplant",
      subtitle: "Vom Perzeptron zum Multi-Layer-Netz",
      topics: ["Perzeptron & Neuron", "Aktivierungsfunktionen", "Forward Pass", "Backpropagation Schritt für Schritt", "MLPClassifier in scikit-learn",
        "Einführung in PyTorch"]
    },
    {
      id: "m10", nr: 10, title: "Deep Learning", status: "geplant",
      subtitle: "Tiefe Netze trainieren und verstehen",
      topics: ["Optimierer: SGD, Momentum, Adam", "Initialisierung, BatchNorm, Dropout", "CNNs: Faltung, Pooling, Feature Maps",
        "RNNs, LSTM & GRU", "Transfer Learning", "Autoencoder & VAEs", "GANs & Diffusionsmodelle (Überblick)"]
    },
    {
      id: "m11", nr: 11, title: "Moderne KI: Transformer & LLMs", status: "geplant",
      subtitle: "Attention is all you need",
      topics: ["Word Embeddings", "Attention-Mechanismus", "Transformer-Architektur", "Tokenisierung", "Pretraining, Fine-Tuning, RLHF",
        "Large Language Models & Prompting", "RAG (Retrieval Augmented Generation)"]
    },
    {
      id: "m12", nr: 12, title: "Reinforcement Learning", status: "geplant",
      subtitle: "Lernen durch Belohnung",
      topics: ["Agent, Umgebung, Belohnung", "Markov-Entscheidungsprozesse", "Q-Learning", "Deep Q-Networks", "Policy Gradients"]
    },
    {
      id: "m13", nr: 13, title: "ML in der Praxis (MLOps)", status: "geplant",
      subtitle: "Modelle in die echte Welt bringen",
      topics: ["Feature Engineering", "Unbalancierte Daten", "Modell-Interpretierbarkeit: SHAP", "Modelle speichern & ausliefern",
        "Monitoring & Data Drift", "Fairness & Ethik"]
    }
  ]
};
