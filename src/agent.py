#! /usr/bin/env python
from environment import Environment
from train import Trainer
import numpy as np
import random


class Agent():
    def __init__(self, env: Environment, sym: int):
        self.trainer = Trainer(env)
        self.env = env
        self.symbol = sym
        self.epsilon = 0.5

    def step(self):
        current_state = self.env.get_current_state()
        action = self.get_action(current_state)
        self.perform_action(current_state, action)
    
    def get_action(self, curr_state):
        available_actions = self.env.get_available_actions()
        search_prob = round(random.uniform(0,1),2)
        if search_prob <= self.epsilon:
            act = self.get_random_action(available_actions)
        else:
            act = self.get_best_action(curr_state, available_actions)
        return act
    
    def get_random_action(self, actions):
        print("Random action")
        return random.choice(actions)

    def get_best_action(self, state, actions):
        print("Best Action")
        act = self.trainer.get_best_exploit_move(state, actions)
        return act

    def perform_action(self, curr_state, action):
        x_val = action[0]
        y_val = action[1]
        curr_state[x_val][y_val] = curr_state[x_val][y_val] + self.symbol

    def reset_agent(self):
        pass


if __name__ == "__main__":
    env = Environment()
    p1 = Agent(env, sym=1)
    p2 = Agent(env, sym=2)
    print(env.board)
    p1.step()
    print(env.board)
    p2.step()
    print(env.board)
    p1.step()
    print(env.board)
#     p2.step()
#     print(env.board)