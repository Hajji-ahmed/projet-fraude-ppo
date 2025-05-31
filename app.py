import streamlit as st
import numpy as np
import joblib
from stable_baselines3 import PPO
from utils.ppo_model import FraudEnv
import pandas as pd

# Chargement du scaler et du modèle
scaler = joblib.load("data_scaler.joblib")
model = PPO.load("ppo_fraud_model.zip")  # Sauvegarde à faire après entraînement

st.title("🕵️ Détection de Fraude en Temps Réel")

# Entrée utilisateur
st.subheader("Entrez les données de la transaction :")

amount = st.number_input("Montant", min_value=0.0, step=1.0)
transaction_type = st.selectbox("Type de transaction", ["purchase", "withdrawal", "transfer"])
country = st.selectbox("Pays", ["USA", "FR", "DE", "MA", "IN", "CN", "Other"])

# Feature engineering simple
type_map = {"purchase": 0, "withdrawal": 1, "transfer": 2}
country_map = {"USA": 0, "FR": 1, "DE": 2, "MA": 3, "IN": 4, "CN": 5, "Other": 6}

features = np.array([
    amount,
    type_map[transaction_type],
    country_map[country],
]).reshape(1, -1)

features_scaled = scaler.transform(features)

# Créer un environnement temporaire
env = FraudEnv(features_scaled, np.array([0]))  # Valeur arbitraire pour y
obs = env.reset()

# Prédiction
if st.button("Analyser la transaction"):
    action, _ = model.predict(obs)
    if action[0] == 1:
        st.error("⚠️ Transaction potentiellement frauduleuse !")
    else:
        st.success("✅ Transaction normale.")
