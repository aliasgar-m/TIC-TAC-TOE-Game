import pickle
from tqdm import tqdm
from src.environment import Environment
from src.agent import Agent


def main() -> None:
    game = Environment()
    player_1 = Agent(env=game, sym=1)
    player_2 = Agent(env=game, sym=2)
    iterations = 500000
    current_player = player_1
    previous_player = None

    for i in tqdm(range(iterations)):
        while game.end_game is False:

            current_player.step()
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


    print("Agent 1 Q values: ", player_1.trainer.q_values)
    print()
    print("Agent 2 Q values: ", player_2.trainer.q_values)
    print(game.summary)
    print()

    if player_1.wins > player_2.wins:
        save_q_values(agent=player_1, filename='Q_values.txt')
    else:
        save_q_values(agent=player_2, filename='Q_values.txt')

def save_q_values(agent:Agent, filename:str) -> None:
    with open(filename, 'wb') as dict_items_save:
        pickle.dump(agent.trainer.q_values, dict_items_save)


if __name__ == "__main__":
    main()
