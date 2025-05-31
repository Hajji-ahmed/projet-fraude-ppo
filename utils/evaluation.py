from sklearn.metrics import classification_report

def evaluate_model(model, X_test, y_test):
    preds = []
    env = model.get_env().envs[0]
    env.X = X_test
    env.y = y_test
    obs = env.reset()
    done = False
    while not done:
        action, _ = model.predict(obs)
        preds.append(int(action[0]))
        obs, _, done, _ = env.step(action[0])
    print("\n🧪 Rapport d'évaluation PPO :\n")
    print(classification_report(y_test, preds))
