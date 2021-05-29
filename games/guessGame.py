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
    print("******************************")
    print("* Welcome to the guess game! *")
    print("******************************", end=f'\n\n{BColors.ENDC}')


def change_color(remaining_attempts):
    if remaining_attempts > 10:
        print(BColors.OKCYAN)
    elif remaining_attempts > 5:
        print(BColors.WARNING)
    elif remaining_attempts > 0:
        print(BColors.FAIL)


def select_level(levels):
    while True:
        print(BColors.BOLD)
        for i, level in enumerate(levels):
            print(f"({i + 1}) {level}")
        print(BColors.ENDC)

        level = int(input("Select the Level: "))

        if level == 1:
            print(f"{BColors.OKCYAN}\n\nEASY", end=f"\n\n{BColors.ENDC}")
            return 20
        elif level == 2:
            print(f"{BColors.WARNING}\n\nINTERMEDIATE", end=f"\n\n{BColors.ENDC}")
            return 10
        elif level == 3:
            print(f"{BColors.FAIL}\n\nHARD", end=f"\n\n{BColors.ENDC}")
            return 5
        else:
            print(f"{BColors.FAIL}\n\nInvalid level!", end=f'\n\n{BColors.ENDC}')
            continue
        break


def play(total_attempts, number):
    score = 100
    for current_attempt in range(1, total_attempts + 1):

        print(f"Attempt {current_attempt} of {total_attempts}")
        guess = int(input("Type a number between 1 and 100: "))
        if guess < 1 or guess > 100:
            print("Invalid guessing number!")
            continue

        hit = guess == number
        higher_guess = guess > number
        smaller_guess = guess < number
        last_chance = current_attempt == total_attempts
        if hit:
            print(f"{BColors.OKGREEN}CONGRATULATIONS! YOU ARE A MONSTER OF GUESSING!", end=f"\n\n{BColors.ENDC}")
            print(f"SCORE: {score}")
            break
        else:
            score = round(score - abs(number - guess) / 2)
            print(BColors.FAIL)
            if last_chance:
                score = 0
                print(f"\n\nYOU LOSE! THE SECRET NUMBER WAS {number}!", end=f"\n\n")
            elif higher_guess:
                print(f"\nYou missed! your guess was higher than the secret number.", end=f"\n\n")
            elif smaller_guess:
                print(f"\nYou missed! your guess was smaller than the secret number.", end=f"\n\n")
            print(BColors.ENDC)


def main():
    number = random.randrange(1, 101)
    welcome()

    levels = ["Easy", "Intermediate", "Hard"]

    total_attempts = select_level(levels)

    play(total_attempts, number)

    print(f"Game Over!")


if __name__ == "__main__":
    main()