#can use the round function to round floats to whole numbers
print(round(8/3))
#can specify how many places to round to
print(round(8/3, 2))

#if you want to divide and get an int instead of a float use two //
print(8//3)
print(type(8//3))

#can save math results in variables
result = 4/2
#divide result by 2 again
result /=2
print(result)

#increase variables, eg if user scores points
score = 0
#user scores point
score += 1
print(score)

#fstrings
score = 0
height = 1.8
isWinning = True
#add 'f' before your string and you can add different values to it without first converting to a string
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")