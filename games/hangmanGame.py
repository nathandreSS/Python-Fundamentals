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


def main():

    welcome()

    secret_word = load_secret_word()

    correct_letters = initialize_correct_letters(secret_word)

    play(secret_word, correct_letters)


def welcome():
    print(BColors.OKCYAN)
    print("********************************")
    print("* Welcome to the hangman game! *")
    print("********************************", end=f'\n\n{BColors.ENDC}')


def load_secret_word():
    secret_word_file = open('secret_word.txt', 'r')
    words = []

    for line in secret_word_file:
        words.append(line.strip().upper())

    secret_word_file.close()
    return words[random.randrange(0, len(words))]


def initialize_correct_letters(secret_word):
    return ['_' for letter in secret_word]


def play(secret_word, correct_letters):
    hanged = False
    completed = False
    misses = 0

    while not hanged and not completed:
        guessed_char = input("Type a letter: ").strip().upper()

        if guessed_char in secret_word:
            update_correct_letters(correct_letters, secret_word, guessed_char)
        else:
            misses += 1
            draw_hang(misses)
        print(correct_letters)

        hanged = misses == 7
        completed = '_' not in correct_letters

    if completed:
        print_win_message()
    else:
        print_lost_message(secret_word)


def update_correct_letters(correct_letters, secret_word, guessed_char):
    for index, letter in enumerate(secret_word):
        if letter.upper() == guessed_char.upper():
            correct_letters[index] = letter
    return correct_letters


def draw_hang(misses):
    print("  _______     ")
    print(" |/      |    ")

    if(misses == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(misses == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(misses == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(misses == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(misses == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(misses == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (misses == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def print_win_message():
    print("Congratulations, you win!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def print_lost_message(secret_word):
    print("Damn, You were hanged!")
    print(f"The word was {secret_word}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if __name__ == "__main__":
    main()
