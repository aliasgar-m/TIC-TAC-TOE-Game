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
        self.board = board = ['x', 'o', 'o', 'x', ' ', ' ', ' ', ' ', ' ']

    def calculate_move(self):
        self.env.board = np.reshape(self.board,(3,3))
        self.env.board[self.env.board == 'x'] = 1
        self.env.board[self.env.board == 'o'] = 2
        print(self.env.board)




def main():
    c = Game()
    c.calculate_move()

if __name__ == "__main__":
    main()