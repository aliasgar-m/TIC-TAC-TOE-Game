#! /usr/bin/env python
from environment import Environment
import numpy as np
import random


class Agent():
    def __init__(self, env: Environment, sym: int):
        # super().__init__()
        self.env = env
        self.symbol = sym
        self.epsilon = 1.0

    def step(self):
        current_state = self.env.get_current_state()
        # print(current_state)
        action = self.get_action(current_state)
        self.perform_action(current_state, action)
        # current_state = new_state

    def get_action(self, curr_state):
        available_actions = self.get_available_actions(curr_state)
        # print(available_actions)
        search_prob = round(random.uniform(0,1),2)
        if search_prob <= self.epsilon:
            act = self.get_random_action(available_actions)
        else:
            act = self.get_best_action(available_actions)
        # print(act)
        return act

    def get_available_actions(self, state):
        return np.argwhere(state == 0)

    def get_random_action(self, actions):
        return random.choice(actions)
    
    def get_best_action(self, actions):
        return "Best choice selected"

    def perform_action(self, curr_state, action):
        x = action[0]
        y = action[1]
        curr_state[x][y] = curr_state[x][y] + self.symbol
        print(action)
        print(curr_state)
        reward = 0
        # return new_state, reward

    def reset_agent(self):
        pass


if __name__ == "__main__":
    env = Environment()
    p1 = Agent(env, sym=1)
    p2 = Agent(env, sym=2)
    p1.step()
    p2.step()