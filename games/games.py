import guessGame
import hangmanGame
import random


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def welcome():
    print(BColors.OKCYAN)
    print("********************")
    print("* Choose the game! *")
    print("********************", end=f'\n\n{BColors.ENDC}')


def select_game(games):
    while True:
        print(BColors.BOLD)
        for i, game in enumerate(games):
            print(f"({i + 1}) {game}")
        print(BColors.ENDC)

        game = int(input("Select the game: "))

        if game == 1:
            return guessGame
        elif game == 2:
            return hangmanGame
        else:
            print(f"{BColors.FAIL}\n\nInvalid game!", end=f'\n\n{BColors.ENDC}')
            continue
        break


def play(game):
   game.main()


def main():
    welcome()

    games = ["Guess Game", "Hangman Game"]

    game = select_game(games)

    play(game)

main()

if __name__ == "__main__":
    main()