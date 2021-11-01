from environment import Environment
import numpy as np
import random


class Trainer:
    def __init__(self, env: Environment):
        self.env = env
        self.Q_values = {}
    
    def get_best_exploit_move(self, state, av_actions):
        state_hash = self.env.get_state_hash(state)
        Q_values = []
        for action in av_actions:
            action_hash = self.env.get_action_hash(action)
            state_action_hash = self.env.get_state_action_hash(state=state_hash,
                                                               action=action_hash)
            s_a_Q_value = self.get_Q_value(state_action_hash)
            Q_values.append(s_a_Q_value)
        
        if all(q_val == 0 for q_val in Q_values):
            return random.choice(av_actions)

        max_val_ind = Q_values.index(max(Q_values))
        return av_actions[max_val_ind]
    
    def get_Q_value(self, s_a_pair):
        if s_a_pair in self.Q_values:
            return self.Q_values.get(s_a_pair)
        else:
            return 0

    def get_max_Q():
        pass

    def update_Q_values(state, action):
        pass




    
