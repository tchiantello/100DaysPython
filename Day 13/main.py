from art import logo, vs
from game_data import data
import random

#make game repeatable

#Pull items from dictionary
def format_data(person):
    """Format person information"""
    person_name = person["name"]
    person_desc = person["description"]
    person_country = person["country"]
    return(f"{person_name}, a {person_desc}, from {person_country}.")

def check_answer(guess, a_followers, b_followers):
    """Use if statement to check if user is correct"""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        game_should_continue = False
        return guess == 'b'

#print logo
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    person_a = account_b
    person_b = random.choice(data)

    if person_a == person_b:
        person_b = random.choice(data)

    print(f"Compare A: {format_data(person_a)}")
    print(vs)
    print(f"Against B: {format_data(person_b)}")

    #ask user for guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #get follower count for each person
    a_follower_count = person_a['follower_count']
    b_follower_count = person_b['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    #Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score {score}")

