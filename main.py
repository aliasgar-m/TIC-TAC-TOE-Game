import numpy as np
from tqdm import tqdm
from src.environment import Environment
from src.agent import Agent


def main():
    game = Environment()
    player_1 = Agent(env=game, sym=1)
    player_2 = Agent(env=game, sym=2)
    iterations = 1
    current_player = player_1
    previous_player = None
    print("Starting State: ")
    print(game.board)
    print()

    for i in range(iterations):
        while game.end_game is False:

            current_player.step()
            print("Current Player: ", current_player.symbol)
            print("Action taken: ", current_player.action_history[-1])
            print("New State: ")
            print(game.board)
            print()
            game.end_game = game.check_winner(sym=current_player.symbol, state=game.board)
            previous_player = current_player

            if current_player.symbol == 1:
                current_player = player_2
            else:
                current_player = player_1

            if game.end_game is True:
                game.update_summary(player=previous_player)

            if game.check_draw() is True and game.end_game is False:
                game.update_summary(draw=True)
                game.end_game = True

        game.reset_environment()

    print(game.summary)
    print()
    print("Agent 1 Q values: ", player_1.trainer.q_values)
    print()
    print()
    print("Agent 2 Q values: ", player_2.trainer.q_values)

if __name__ == "__main__":
    main()