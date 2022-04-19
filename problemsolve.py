# How to solve a problem:
    # Figure out what the input and its type are
    # Set up a function
    # Figure out what the output and its type are
    # Gather Your Knowledge
    # Gathers Your Constraints
    # Determine a Logical way to solve the problem
        # Write each step out English
        # Write each step out in Python-esse
    # Invoke and Test Your Function


# ex
    # given an integer age 
    # Write a function to return a string based on the age
    # if that age is old enough to smoke(18) return "Can Smoke, Can't Drink"
    # if that age is not old enough to smoke return "Can't do anything"
    # If that age is old enough to drink "Can Party"

def what_can_I_buy(age):
    '''Takes an integer and returns a string that says what that age can do'''
    #Check the age and if it is in a certain range I'll return its respective string.

    #if they are 21 and over I'll return "can party"
    if age >= 21:
        return "Can Party"
    #if they are under 18 return "can't do anything"
    elif age < 18:
        return "Can't So Anything"
    #if they are between 18 inclusive and 21 exclusive then return "can smoke can't drink"
    elif 18<=age<21:
        return "Can Smoke, Can't Drink"

print(what_can_I_buy(17))
print(what_can_I_buy(18))
print(what_can_I_buy(19))
print(what_can_I_buy(20))
print(what_can_I_buy(21))
