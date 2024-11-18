# user_input.py

# Asking the user for their name, age, and location
name = input("Please enter your name:")
fathersAge = int(input("Please enter your fathers age: "))
sonsAge = int(input("Please enter your sons age: "))
result = fathersAge - sonsAge
# Printing a personalized message
print("Hello {}, your father's age {} removed from your son's age {} is {}.".format(name, fathersAge, sonsAge, result))
