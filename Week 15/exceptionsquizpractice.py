

user_input = input("Please choose a number to divide ten by: ")
done = False

while not done:
    try:
        user_number = int(user_input)
        result = 10/user_number
        print(result)
        done = True
    except ValueError:
        print("Value Error.")
        user_input = input("Please choose a number to divide ten by: ")
    except ZeroDivisionError:
        print("Stop")
        user_input = input("Please choose a number to divide ten by: ")









