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

# done = False
# total = 0
# user_num = ""

# while not done:
#     user_num = input("enter a number or type q to end: ")
#     if user_num != "q":
#         total += int(user_num)
#     else:
#         done = True

# print(f"Total = {total}")
# Python follows duck typing, ie: if it walks and talks like a duck, it is a duck.

# Print the numbers 1-10

# for number in range(1,11):
#     print(number)

# # print even numbers one thru ten

# for number in range(2,11,2):
#     print(number)

# Print all the odd numbers between 5 and some user given upper bound inclsively.

# user_num = int(input(""))
# for number in range(5,user_num+1,2):
#     print(number)


# Find the sum of user entered values until the user types q for done.
# Indeterminate range => while loop

# "m" + "a" outputs "ma"
# This is called string concatonation
# "6" + "7" + "8" outputs "678"
# A string is called a collection data type-- it is a collection of data. m is data, a is data.

# x = "hello world"
# print(x[8])

# x = "hello world"
# print(x[2:8])

word = "hello world"
for letter in word:
    print(letter)

x = "123"
for number in x:
    print(number)







