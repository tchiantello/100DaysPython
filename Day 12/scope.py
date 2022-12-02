################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope
# variable exists only within a function

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()

# Global Scope
# variable exists everywhere and is available anywhere (defined outside of a function)
player_health = 10

# Python does not have a Block Scope
# Defining a variable within an if statement, it exists in the if statement scope
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

# Modifying Global Scope
# Best practice to not name global and local varaibles the same
# We need to explicitly say we are modifying a global variable within a function
enemies = 1

def increase_enemies():
    global enemies
    enemies += 1

# Global Constants
# Variables you define and are never going to change
# Usually define Global Constants with all caps
PI = 3.14
URL = "https:www.google.com"

