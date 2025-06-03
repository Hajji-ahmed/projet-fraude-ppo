# Système de Détection de Fraude en Temps Réel par PPO

## 1. Présentation du Projet

Ce projet vise à concevoir un système intelligent de détection de fraude financière en temps réel en utilisant un algorithme d’apprentissage par renforcement : **Proximal Policy Optimization (PPO)**.
L'objectif est de permettre à un agent d'apprendre les schémas typiques des transactions frauduleuses et d’améliorer progressivement sa capacité de détection, tout en minimisant les faux positifs.

Le système repose sur des données réelles de transactions financières labellisées (fraude / non fraude), et se structure en modules indépendants pour faciliter l’analyse, l'entraînement et l’évaluation du modèle.

---

## 2. Objectifs

* Identifier et analyser les caractéristiques des transactions financières.
* Appliquer des techniques de prétraitement et de feature engineering.
* Former un agent PPO pour détecter les comportements frauduleux.
* Évaluer les performances du modèle (précision, taux de faux positifs).
* Développer une interface utilisateur simple pour tester les prédictions en temps réel.

---

## 3. Architecture du Projet

Le projet suit une architecture modulaire orientée vers la réutilisabilité du code.

```
PROJET_ML2/
│
├── utils/
│   ├── data_processor.py         # Chargement et nettoyage des données
│   ├── evaluation.py             # Métriques d'évaluation du modèle
│   ├── feature_engineering.py    # Création de nouvelles caractéristiques
│   ├── ppo_model.py              # Entraînement PPO avec Stable Baselines3
│   ├── visualization.py          # Graphiques et visualisation de données
│
├── app.py                        # Interface Streamlit pour tester le modèle
├── data_scaler.joblib            # Scaler sauvegardé pour normalisation
├── requirements.txt              # Dépendances Python
├── shema.txt                     # Structure et description des données
├── .gitignore                    # Fichiers/dossiers ignorés par Git
└── venv/                         # Environnement virtuel Python
```

---

## 4. Fonctionnalités du Système

### 4.1 Prétraitement et Analyse Exploratoire

* Chargement de jeux de données de transactions labellisées.
* Nettoyage des données, traitement des valeurs manquantes, encodage des variables.
* Visualisation des distributions (montant, pays, type de transaction...).

### 4.2 Feature Engineering

* Transformation de données temporelles.
* Génération de nouvelles variables comportementales (fréquence, récence, etc.).
* Standardisation des données avec sauvegarde du scaler.

### 4.3 Apprentissage avec PPO

* Définition d’un environnement personnalisé pour l'agent PPO.
* Implémentation de l’algorithme PPO via `Stable-Baselines3`.
* Entraînement sur les épisodes simulés pour apprendre à détecter les fraudes.


### 4.4 Évaluation du Modèle

* Calcul des métriques : précision, rappel, F1-score, courbe ROC.
* Analyse du taux de détection vs. taux de faux positifs.
* Visualisation des performances.

### 4.5 Interface Utilisateur (Streamlit)

* Interface conviviale permettant de charger des données et obtenir des prédictions en direct.
* Visualisation en temps réel des résultats du modèle.![Uploading Capture d'écran 2025-06-02 131733.png…]()



## 5. Installation et Exécution

### 5.1 Prérequis

* Python 3.10 ou supérieur
* pip

### 5.2 Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/nom-utilisateur/projet-ppo-fraude.git
cd projet-ppo-fraude

# 2. Créer un environnement virtuel
python -m venv venv
source venv/bin/activate         # Sur Windows : venv\Scripts\activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer l'application
streamlit run app.py
```

## 7. Auteurs

Projet réalisé dans le cadre d’un projet académique :

* Ayoub Lamkaddem
* Ahmed Hajji
* Abdelmalek Belga
* Aymane Bouabdallah

---


Vous pouvez insérer ces captures dans le README pour enrichir la présentation visuelle du projet.

---

Souhaites-tu que je te crée ce fichier `README.md` prêt à l’emploi avec les liens de captures inclus et t’aide à le pousser sur GitHub ?
