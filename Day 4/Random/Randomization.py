#need to import the random module
import random

#modules refer to other code, created my_module.py and we can reference it
import my_module

#can then print values from our imported module
print(my_module.pi)

#generate a random integer with randint
random_integer = random.randint(1, 10)
print(random_integer)

#generate random float with random
random_float = random.random()
print(random_float)

random_int_float = random.randint(1,5) + random.random()
print(random_int_float)