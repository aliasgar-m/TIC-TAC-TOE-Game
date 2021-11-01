#! /usr/bin/env python
from environment import Environment
import numpy as np
import random


class Agent():
    def __init__(self, env: Environment, sym: int):
        self.env = env
        self.symbol = sym
        self.epsilon = 1.0

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
        return random.choice(actions)

    def get_best_action(self, state, actions):
        state_hash = self.env.get_state_hash(state)
        av_action_hash = self.env.get_action_hash(actions)
        return "Best choice selected"

    def perform_action(self, curr_state, action):
        x = action[0]
        y = action[1]
        curr_state[x][y] = curr_state[x][y] + self.symbol

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
#     print(env.board)
#     p2.step()
#     print(env.board)