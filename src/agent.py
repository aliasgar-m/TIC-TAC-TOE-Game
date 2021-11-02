#! /usr/bin/env python
from environment import Environment
from trainer import Trainer
from copy import copy
import numpy as np
import random


class Agent():
    def __init__(self, env: Environment, sym: int):
        self.trainer = Trainer(env)
        self.env = env
        self.symbol = sym
        self.epsilon = 1.0

    def step(self):
        current_state = self.env.get_current_state()
        available_actions = self.env.get_available_actions()
        action = self.get_action(current_state, available_actions)
        next_state = self.perform_action(current_state, action)
        self.trainer.update_Q_values(current_state, action)
        self.env.board = next_state
    
    def get_action(self, curr_state, av_actions):
        search_prob = round(random.uniform(0,1),2)
        if search_prob <= self.epsilon:
            act = self.get_random_action(av_actions)
        else:
            act = self.get_best_action(curr_state, av_actions)
        return act
    
    def get_random_action(self, actions):
        return random.choice(actions)

    def get_best_action(self, state, actions):
        act = self.trainer.get_best_exploit_move(state, actions)
        return act

    def perform_action(self, curr_state, action):
        x_val = action[0]
        y_val = action[1]
        curr_state_copy = copy(curr_state)
        curr_state_copy[x_val][y_val] = curr_state_copy[x_val][y_val] + self.symbol
        return curr_state_copy

    def reset_agent(self): # complete function
        pass