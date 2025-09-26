# Ask the user for two integers named larger and smaller. Determine (and output) how many times
# larger can be halved while still be greater than smaller.
# smaller = int(input("Enter an integer: "))
# larger = int(input("Enter a larger integer: "))
# count = 0

# while (larger/2) > smaller:
#     count += 1
#     larger /= 2
# print(count)

# # Write a program that asks the user for a word and then, using a loop, prints every other letter of the
# # word starting with the second letter.
result = ""
word = input("Enter a word: ")

for letter in range(1,len(word),2):
    result += word[letter]
print(result)

# # Using a loop, write a program that prints every even number between 37 and 1050 (inclusively)

# for number in range(38,1051,2):
#     print(number)

# # Write a program to create a word one letter at a time. You should prompt the user to enter a single
# # letter one at a time until they type done. Done they type done, output their newly created word.
# user_word = ""
# user_letter = input("Enter a letter or 'done' to stop: ")
# while user_letter != "done":
#     user_word += user_letter
#     user_letter = input("Enter a letter or 'done' to stop: ")
# print(f"Your word is {user_word}")

# # Using a loop, write code to calculate the sum of all odd numbers between 50 and 517. Print the result.

# odd_sum = 0 

# for number in range(51,518,2):
#     odd_sum += number
# print(odd_sum)

# Write a program that repeatedly asks the user for integers until a negative integer is given.
# The program should keep track of the sum of the numbers and print the sum at the end
# (not including the negative number)

# sum = 0
# user_num = int(input("Enter a positive integer or negative integer to stop: "))

# while user_num > -1:
#     sum = sum + user_num
#     user_num = int(input("Enter a positive integer or negative integer to stop: "))
# print(sum)

# Given a positive integer n, the following rules will always create a sequence that ends with 1, called
#Hailstone Sequence:
#(a) If n is even, divide by 2
#(b) If n is odd, multiply by 3 and add 1 (i.e. 3n + 1)
#(c) Continue until n is 1
#Write a program that prints the hailstone sequence starting at n = 25

# n = 25
# while n > 1:
#     if n % 2 == 0:
#         n = n // 2
#         print(n)
#     else:
#         n = (3*n)+1
#         print(n)

# Write code that asks the user for an integer and then prints each number that is a factor of the input.

# user_num = int(input("Enter an integer: "))
# for candidate in range(1,user_num+1):
#     if user_num % candidate == 0:
#         print(candidate)

# You are the newest rug fashion designer on the scene, but you’re running out of ideas. Write a program
# that will help you design rugs. The program should ask for a width, a length, and pattern, and then
# create a rug consisting of that pattern and dimensions.

# width = int(input("Enter rug width (integer): "))
# length = int(input("Enter rug length (integer): "))
# pattern = input("Enter a single character to serve as the rug pattern: ")
# pwidth = ""
# width_num = 1
# length_num = 1

# while length_num <= length:
#     while width_num <= width:
#         pwidth += pattern
#         width_num += 1
#     print(pwidth)
#     length_num += 1

# Write a program that asks the user for an integer. Calculate (and then print) the sum of all square
# numbers up to and including the user’s number

# user_number = int(input("Enter an integer: "))
# sum = 0
# for number in range(1,user_number+1):
#     number **= 2
#     sum += number
# print(sum)


