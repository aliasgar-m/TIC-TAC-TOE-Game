from copy import copy
import numpy as np


class Environment:
    def __init__(self) -> None:
        self.rows = 3
        self.columns = 3
        self.board = np.zeros([self.rows, self.columns])
        self.end_game = False
        self.state_hash_matrix = np.array([[10**1, 10**2, 10**3],
                                           [10**4, 10**5, 10**6],
                                           [10**7, 10**8, 10**9]])
        self.action_hash_matrix = np.array([[1,2,3],
                                            [4,5,6],
                                            [7,8,9]])
        self.summary = {"Games Played: ":0,
                        "Player 1 wins: ":0,
                        "Player 2 wins: ":0,
                        "Draw: ":0}

    def check_draw(self) -> bool:
        curr_state = self.get_current_state()
        if len(self.get_available_actions(state=curr_state)) == 0:
            return True
        return False

    def get_current_state(self) -> np.ndarray:
        return self.board

    def get_available_actions(self, state=None) -> np.ndarray:
        return np.argwhere(state == 0)

    def get_state_hash(self, state) -> int:
        hash_val = 0
        hash_val = np.sum(np.multiply(state, self.state_hash_matrix))
        return hash_val

    def get_action_hash(self, act) -> int:
        hash_val = 0
        hash_val = self.action_hash_matrix[act[0]][act[1]]
        return hash_val

    def get_state_action_hash(self, s_h, a_h) -> int:
        return s_h * a_h

    def get_reward(self, p_act, n_s, n_acts, sym) -> int:
        if self.check_winner(sym, n_s) is True:
            return 1
        if self.missed_block_move(n_s, n_acts, sym) is True:
            return -10
        if self.missed_winning_move(p_act, sym) is True:
            return -100
        return 0

    def missed_block_move(self, n_s, n_acts, sym) -> bool:
        if sym == 1:
            sym = 2
        else:
            sym = 1

        for each_action in n_acts:
            x = each_action[0]
            y = each_action[1]
            n_s_copy = copy(n_s)
            n_s_copy[x][y] = n_s_copy[x][y] + sym
            win_bool = self.check_winner(sym, n_s_copy)

            if win_bool is True:
                return True
        return False

    def missed_winning_move(self, p_act, sym) -> bool:
        curr_state = self.get_current_state()
        av_actions = self.get_available_actions(state=curr_state).tolist()

        av_actions = np.array(av_actions)
        for each_action in av_actions:
            if each_action.tolist() != p_act.tolist():
                x = each_action[0]
                y = each_action[1]
                n_s_copy = copy(curr_state)
                n_s_copy[x][y] = n_s_copy[x][y] + sym
                win_bool = self.check_winner(sym, n_s_copy)

                if win_bool is True:
                    return True
        return False

    def check_winner(self, sym, state=None) -> bool:
        if self.check_row(sym, curr_state=state) or \
        self.check_col(sym, curr_state=state) or \
        self.check_diagonal(sym, curr_state=state):
            return True
        return False

    def check_row(self, sym, curr_state=None) -> bool:
        if np.any(np.all(curr_state == sym, axis=1)):
            return True
        return False

    def check_col(self, sym, curr_state=None) -> bool:
        if np.any(np.all(curr_state == sym, axis=0)):
            return True
        return False

    def check_diagonal(self, sym, curr_state=None) -> bool:
        if np.all(np.diagonal(curr_state) == sym) or \
            np.all(np.fliplr(curr_state).diagonal() == sym):
            return True
        return False

    def reset_environment(self) -> None:
        self.board = np.zeros([self.rows, self.columns])
        self.end_game = False

    def update_summary(self, draw=False, player=None) -> None:
        if draw:
            self.summary["Games Played: "] += 1
            self.summary["Draw: "] += 1

        if player is not None:
            self.summary["Games Played: "] += 1
            if player.symbol == 1:
                player.wins += 1
                self.summary["Player 1 wins: "] += 1
            else:
                player.wins += 1
                self.summary["Player 2 wins: "] += 1
