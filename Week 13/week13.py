# Error Handling!

# The errors we've encountered so far are programmer errors, compile-time (ish)

# Now what if someone isn't using this the way you intended? We need a way to manage these situations.

# A compile-time error may look like print"hell world'
# This is of the fault of the programmer
# run time errors are errors that result from the user using the program incorrectly.
'''
try: 
    #block of code
    # If something goes wrong in here, an error will be raised and sent to the except statement.
except (code similar to an if statement):
    # block of code
except NameError:
    # Handle this type of error.
    print("This is a name error.")
except ValueError:
    print("This is a value error.")
except TypeError:
    print("This is a type error.")'''

# First, we write the code to work. 


# Then we try to break the code.
# We try to anticipate everything that the user could enter that would make the program crash.
'''print("Program start")
try:
    age = int(input("Enter your age: "))
    print(f"Your age is {age}.")
    print(f"Next year, your age will be {age + 1}.")
except ValueError:
    print("value error: you must pick an integer age.")

print("program ended normally")'''


print("Enter a number to divide ten by. ")
user_input = input("Your number: ")

done = False
while not done:
    try:
        user_number = int(user_input)
        result = 10 / user_number
        print(f"The result is {result}")
        done = True
    except ZeroDivisionError:
        print("Please enter a non-zero integer.")
        user_input = input("Your number: ")
    except ValueError:
        print("Value error: Please enter a non-zero integer.")
        user_input = input("Your number: ")

print("program ended normally")