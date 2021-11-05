import random
from copy import copy
from typing import List
import numpy as np
from .environment import Environment
from .trainer import Trainer


class Agent:
    def __init__(self, env:Environment, sym:int) -> None:
        self.trainer = Trainer(env=env, sym=sym)
        self.env = env
        self.symbol = sym
        self.action_history = []
        self.epsilon = 0.4

    def step(self) -> None:
        current_state = self.env.get_current_state()
        available_actions = self.env.get_available_actions(state=current_state)
        p_action = self.get_action_to_perform(c_state=current_state, actions=available_actions)
        next_state = self.perform_action(c_state=current_state, action=p_action)
        self.action_history.append(p_action)
        self.trainer.update_q_values(c_state=current_state, p_act=p_action, n_state=next_state)
        self.env.board = next_state

    def get_action_to_perform(self, c_state, actions) -> List:
        search_probability = round(random.uniform(0,1),1)
        if search_probability <= self.epsilon:
            action = self.get_explore_action(a_list=actions)
        else:
            action = self.get_exploit_action(c_s=c_state, a_list=actions)
        return action

    def get_explore_action(self, a_list) -> List:
        return random.choice(a_list)

    def get_exploit_action(self, c_s, a_list) -> List:
        act = self.trainer.get_best_action(c_s, a_list)
        return act

    def perform_action(self, c_state, action) -> np.ndarray:
        x_val = action[0]
        y_val = action[1]
        c_state_copy = copy(c_state)
        c_state_copy[x_val][y_val] = c_state_copy[x_val][y_val] + self.symbol
        return c_state_copy
