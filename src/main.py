import numpy as np
from tqdm import tqdm
from environment import Environment
from agent import Agent
from trainer import Trainer

def main():
    game = Environment()
    p1 = Agent(env=game, sym=1)
    p2 = Agent(env=game, sym=2)
    train = Trainer(env=game)
    current_player = p1
    # print("Starting State")
    # print(game.board)

    for i in tqdm(range(1), desc="Progress: "): #replace 1000 by train.iterations
        while game.end_game is False:
            current_player.step()
            # print("State after action")
            # print(game.board)
            # print()
            game.check_winner()

            if game.end_game:
                game.reset_environment()
                p1.reset_agent()
                p2.reset_agent()
                return

            if current_player.symbol == 1:
                current_player = p2
            else:
                current_player = p1

def main2():
    arr = np.array([[1,1,1],[0,2,0],[0,0,2]])
    ans = np.all(arr == 1, axis=1)
    print(arr)
    print(ans)
    if ans.any():
        print("TRue")

    # arr = np.array([[1,0,0],[1,2,0],[1,0,2]])
    # ans = np.all(arr == 1, axis=0)
    # print(arr)
    # print(ans)

if __name__ == "__main__":
    main2()
