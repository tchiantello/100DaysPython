import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
final_number = random.randint(1,100)
guesses_remaining = 0
is_game_over = False

if mode == 'easy':
    guesses_remaining = 10
else:
    guesses_remaining = 5



print(f"You have {guesses_remaining} attempts remaining to guess the number.")

while guesses_remaining > 0:
    player_guess = int(input("Make a guess: "))
    if player_guess == final_number:
        print("Correct! You win!")
    elif player_guess < final_number:
        print("Too low, guess again")
    elif player_guess > final_number:
        print("Too high, guess again")
    guesses_remaining -= 1
    print(f"You have {guesses_remaining} attempts remaining to guess the number.")



    