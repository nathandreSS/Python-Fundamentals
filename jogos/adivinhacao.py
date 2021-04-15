print("*********************************")
print("Welcome to the guess game!")
print("*********************************")

number = 75
total_attempts = 3
current_attempt = 1

for current_attempt in range(1, total_attempts + 1):
    print(f"Attempt {current_attempt} of {total_attempts}")
    guess = int(input("Type the  between 1 and 100: "))
    if guess < 1 or guess > 100:
        print("Invalid guessing number!")
        continue

    hit = guess == number
    higher_guess = guess > number
    smaller_guess = guess < number
    if hit:
        print("Crongratulations! You are a monster of guessing!")
        break
    else:
        if higher_guess:
            print("You missed, your guess was higher than the secret number.")
        elif smaller_guess:
            print("You missed, your guess was smaller than the secret number.")


print("Game Over!")