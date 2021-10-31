#! /usr/bin/env python
import numpy as np
import random


class Environment:
    def __init__(self):
        self.rows = 3
        self.columns = 3
        self.board = np.zeros([self.rows, self.columns])
        self.end_game = False
        # self.player1 = agent1
        # self.player2 = agent2
    
    def check_game_end():
        pass

    def reset_environment():
        pass

    def get_current_state(self):
        return self.board
