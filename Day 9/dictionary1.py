programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    }

#to pull info out of the dictionary, put the key in brackets to pull the value of that key
print(programming_dictionary["Bug"])

#to add info to the dicdtionary
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

#create a new dictionary
new_dictionary = {}

#edit item in dictionary
programming_dictionary["Bug"] = "A moth in your computer"

#loop through a dictionary
#loop through dictonary getting just the keys
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


#can wipe an existing dictionary
programming_dictionary = {}