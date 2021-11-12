import pickle
import numpy as np
from src.environment import Environment
from src.agent import Agent

class Game:
    def __init__(self, player = 'x', computer = 'o'):
        self.env = Environment()
        self.agent = Agent(env=self.env, sym=2)
        self.player = player
        self.computer = computer
        self.board = board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def calculate_move(self):
        self.env.board = np.reshape(self.board,(3,3))
        self.env.board[self.env.board == 'x'] = 1
        self.env.board[self.env.board == 'o'] = 2
        self.env.board[self.env.board == ' '] = 0
        self.env.board = self.env.board.astype(int)
        
        self.agent.trainer.q_values = self.load_q_values()
        curr_state = self.agent.env.get_current_state()
        available_actions = self.agent.env.get_available_actions(state=curr_state)
        p_action = self.agent.get_action_to_perform(c_state=curr_state, actions=available_actions)
        
        move = self.env.get_action_hash(act=p_action)
        return move - 1

    def load_q_values(self, filename='Q_values.txt'):
        with open(filename, "rb") as f:
            dict = pickle.load(f)
            return dict