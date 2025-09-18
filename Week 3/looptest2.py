# number = 1
# while number <= 10:
#     print(number)
#     number += 1

# # print the even nums between 1 and 10:

# number = 2
# while number <= 10:
#     print(number)
#     number += 2


# number = 1
# while number<=10:
#     if number%2 == 0:
#         print(number)
#     number += 1

# number = int(input(""))
# while number<=10:
#     if number%2 == 1:
#        number += 1
#     print(number)
#     number += 2


# # Print all odd numbers between 5 and user number

# user_num = int(input("Enter a number greater than 5: "))
# number = 5
# while 5 <= number <= user_num:
#     if number%2 == 1:
#         print(number)
#     number += 1

# A break is an escape method that will terminate the loop and say 'don't run anything else, just run the False path'.
# A continue is a statement that will say 'don't run anything ese, go back to evaluate the condition and run again'.

# #Print all even numbers that are not divisible by 3
# number = 0
# while number < 50:
#     number += 1
#     if number % 2 == 0:
#         if number % 3 == 0: # We want it to do nothing and skip the rest of the code if this is True.
#             continue
#         print(number)
    
# # Matt prefers to write code with flags, not break/continue statements.

# # Write a program that adds numbers until the user says stop.
# # We'll need to keep the iteration going but also accumulate numbers. 
# # We'll use an "accumulation design pattern". a design pattern is just like a method that works very well so we keep doing it.

# total = 0
# user_num = (input("Enter a number or type q to end: "))

# while user_num != "q":
#     total += int(user_num) # Assuming valid inputs
#     user_num = input("Enter a number or type q to end:")

# print(f"Total = {total}")

#Here is an example of a 'flag'.

done = False
total = 0
user_num = ""

while not done:
    user_num = input("enter a number or type q to end: ")
    if user_num != "q":
        total += int(user_num)
    else:
        done = True

print(f"Total = {total}")


