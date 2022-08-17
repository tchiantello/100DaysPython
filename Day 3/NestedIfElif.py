#can nest multiple conditions within each other

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print ("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

        wants_photo = input("Do you want a photo taken? Y or N. ")
        if wants_photo == 'Y':
            #Add $3 to bill
            bill += 3
        
        print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")

#elif statements allow you to do multiple "ifs" in one block
#if/elif/else statements will match with the first and execute the code block
#can use multiple 'if' statements to match many items and execute many blocks of code

