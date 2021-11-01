#! /usr/bin/env python
import numpy as np
import random


class Environment:
    def __init__(self):
        self.rows = 3
        self.columns = 3
        self.board = np.zeros([self.rows, self.columns])
        self.end_game = False
        self.state_hash_matrix = np.array([[10**1, 10**2, 10**3],
                                           [10**4, 10**5, 10**6],
                                           [10**7, 10**8, 10**9]])
        self.action_hash_matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])

    def get_current_state(self):
        return self.board

    def get_available_actions(self):
        return np.argwhere(self.board == 0)
    
    def get_state_hash(self, state):
        hash_val = 0
        product = np.multiply(state, self.state_hash_matrix)
        state_hash = np.sum(product)
        return hash_val

    def get_action_hash(self, action):
        hash_val = 0
        x_val = action[0]
        y_val = action[1]
        hash_val = self.action_hash_matrix[x_val][y_val]
        return hash_val
    
    def get_state_action_hash(self, state, action):
        return state * action

    def check_game_end():
        pass

    def reset_environment():
        pass