# # Write code to determine how many letters are in a word.

# word = input("Enter a word or phrase: ")
# count = 0
# for letter in word:
#      if letter != " ":
#          count += 1
# print(f"Number of letters in your word: {count}")

# # Write code to determine how many vowels are in a given word.

# vowel = ["a","e","i","o","u"]
# word = input("Enter a word: ")
# count = 0
# for letter in word:
#     if letter in vowel:
#         count += 1
# print(f"Number of vowels in your word: {count}")

# Another solution:

# word1 = input("Enter a word: ")
# word2 = input("Enter a word: ")
# word3 = input("Enter a word: ")
# word_list = [word1,word2,word3]
# count = 0 

# for word in word_list:
#     for letter in word:
#         if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "y":
#             count += 1
#     print(f"The vowel count in '{word}' is {count}")
#     count = 0
 
# print("---------")
# def vowel_counter(passed_word):
#     count = 0
#     for letter in passed_word: 
#         if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u": 
#             count += 1 
#         print(count)
#         count = 0

# I only want the function to do something when we invoke it or intend it to do something. 
# word1 = "hello world" 
# word2 = "apples and bananas"
# word3 = "happy times"
# vowel_counter(word1)

# word = 0
# count = 0
# def vowel_counter(passed_word):
#     passed_word = "banana"
#     count = 0
#     for letter in passed_word:
#         if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u": 
#             count += 1
# print(f"the vowel count in {word} is {count}")

# Write a function that takes an int, adds 2 then multiplies by 4 and prints the result

# def practice_function(passed_variable):
#     passed_variable = (passed_variable+2)*4
#     print(passed_variable)


# def my_fct(number):
#     number += 2
#     number *= 4
#     return number

# # If we want to do this function again and again with the numbers it outputs, we use the keyword "return".

# result1 = my_fct(10)
# result2 = my_fct(result1)
# print(result2)

# You can nest function calls
# def add_ten(number):
#     number += 10
#     return number

# result1 = add_ten(my_fct(10))


# Say we want to call my_fct 10 times. Then 100 times.

# result = 10
# for iteration in range(0,10):
#     result = my_fct(result)
# print(result)

# for iteration in range(0,100):
#     result = my_fct(result)
# print(result)

# # Write a function that returns the product of two arguments.

# def product(num1,num2):
#     product = num1 * num2
#     return product
# print(product(4,3))

# x = [] # This is a list with nothing inside it. We can store things in it!

# basket = ["apple", "banana", 3, False, 4.5, "grapes"]

# # print the element of the list basket in index position 1.
# print(basket[1]) # it's in index 0, so this prints "banana"

# # print everything that is not a string.

# print(basket[2], basket[3], basket[4])
# print(basket[2:5])

# x = "appl"
# print(x) # reveals we forgot an e. Let's tack on the e.

# x += "e"
# print(x)

# basket.append(element) will add th element to the end of the list basket

# basket = ["apple", "banana", 3, False, 4.5, "grapes"]
# basket.insert(3,12)
# print(basket)

# where (index position, value to add)

basket = ["apple", "banana", 3, False, 4.5, "grapes"]
basket.remove(3)
print(basket)
