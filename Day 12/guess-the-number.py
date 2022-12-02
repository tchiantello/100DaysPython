#Following along with instructions
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Funciton to check users guess against actual answer
def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns number of turns remianing"""
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

#Make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    #Choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        #Let user guess a number
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

#Track number of turns and reduce by 1 if they get it wrong

# Repeat the guessing functionality if they get it wrong

game()