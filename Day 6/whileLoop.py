#in Reeborg, change the code in the hurdle example from a for loop to a while loop

#use 'for' loop when you need to iterate over multiple items and need to do something with each item
#use 'while' loop when you don't care where you are in a sequence

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
    jump()

number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1