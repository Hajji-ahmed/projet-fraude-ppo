import gym
import numpy as np
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import DummyVecEnv
from gym import spaces

class FraudEnv(gym.Env):
    def __init__(self, X, y):
        super(FraudEnv, self).__init__()
        self.X = X
        self.y = y
        self.index = 0
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(X.shape[1],), dtype=np.float32)
        self.action_space = spaces.Discrete(2)

    def reset(self):
        self.index = 0
        return self.X[self.index]

    def step(self, action):
        label = self.y[self.index]
        reward = 1 if action == label else -1
        self.index += 1
        done = self.index >= len(self.X)
        obs = self.X[self.index] if not done else np.zeros_like(self.X[0])
        return obs, reward, done, {}

def train_ppo(X_train, y_train):
    env = DummyVecEnv([lambda: FraudEnv(X_train, y_train)])
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=10000)
    return model
model.learn(total_timesteps=10000)
model.save("ppo_fraud_model")  # Sauvegarde le modèle pour Streamlit
