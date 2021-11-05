import random
import numpy as np
from .environment import Environment


class Trainer:
    def __init__(self, env:Environment,sym:int=None) -> None:
        self.env = env
        self.sym = sym
        self.q_values = {}
        self.learning_param = 0.1
        self.discount_factor = 1

    def update_q_values(self, c_state, p_act, n_state) -> None:
        state_hash = self.env.get_state_hash(state=c_state)
        action_hash = self.env.get_action_hash(act=p_act)
        current_q_value = self.get_q_value(s_hash=state_hash, a_hash=action_hash)
        next_available_actions = self.env.get_available_actions(state=n_state)

        immediate_reward = self.env.get_reward(p_act=p_act, n_s=n_state,
                                               n_acts=next_available_actions, sym=self.sym)
        next_max_q_value, _ = self.get_max_q(state=n_state,
                                             actions=next_available_actions)

        new_q_value = (1 - self.learning_param) * current_q_value
        new_q_value += self.learning_param * (immediate_reward + \
                                             (self.discount_factor * next_max_q_value))

        state_action_hash = self.env.get_state_action_hash(s_h=state_hash, a_h=action_hash)
        self.q_values[state_action_hash] = round(new_q_value,4)

    def get_q_value(self, s_hash, a_hash) -> float:
        s_a_hash = self.env.get_state_action_hash(s_h=s_hash, a_h=a_hash)
        if s_a_hash not in self.q_values:
            self.q_values[s_a_hash] = 0.0
        return self.q_values.get(s_a_hash)

    def get_max_q(self, state, actions):
        s_a_q_values = []
        state_hash = self.env.get_state_hash(state=state)

        if len(actions) == 0:
            return 0, []

        for each_action in actions:
            action_hash = self.env.get_action_hash(each_action)
            s_a_q_values.append(self.get_q_value(state_hash, action_hash))
        return max(s_a_q_values), s_a_q_values

    def get_best_action(self, state, actions):
        max_q_value, state_action_q_value_list = self.get_max_q(state, actions)

        if all(q_val == 0.0 for q_val in state_action_q_value_list):
            return random.choice(actions)

        max_val_index = state_action_q_value_list.index(max_q_value)
        return actions[max_val_index]
