x = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

#If I wanted to extract the middle day, I can do indexing:
#print(x[2])
#print(x[1:4])

# for day in x:
#     print(day, end=' ')

# word = "Appl"
# word += "e"

# print(word)

# To add to a list in a similar way: use keyword append

# x.append("Saturday")
# x.append("Sunday")

# print(x[2][3:6])

# x[4] = "Funday"
# print(x)

# word = "apfel"
# print(word[2]) # Isolates "f"

# word[2] = "p" # fails
# print(word)

# x ="apple"
# y = x
# print(x)
# print(y)

# x = "banana"

# print(x)
# print(y)


# x = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# y = x
# print(x)
# print(y)
# # Prints the same list

# x[4] = "Funday"
# print(x)
# print(y)

# Say I don't want someone to be able to modify my list. I want it to be immutable.
# x = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# # I don't want friday to be funday. It's a WORKDAY! >:((((((((
# x = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
# print(x)

# x[4] = "Funday"

# write a function that takes a string as an argument 
# and returns a list containing all of the words in that string.

user_string = "Peter Piper picked a peck of pickled peppers."

def string_to_list(word):
    words = []
    built_word = ''
    for letter in word:
        if letter == ' ':
            words.append(built_word)
            built_word = ''
        else:
            built_word += letter
    words.append(built_word)
    return words

# print(string_to_list("Peter Piper picked a peck of pickled peppers."))

# def string_to_list_other(word):
#     words = []
#     built_word = ''
#     for index in range(len(word)):
#         if word[index] == " ":
#             words.append(built_word)
#             built_word = " "
#         elif index == len(word)-1:
#             built_word += word[index]
#             words.append(built_word)
#         else:
#             built_word += word[index]
#     return words


# print(string_to_list_other("When does a man become a monster?"))


# print(user_string.split())
# # Also works

# Write a fct that takes a string as an argument, and returns a list containing all the words 
# that have at least two vowels.
# user_string = "Peter Piper picked a peck of pickled peppers."

# def two_vowel_string(my_word):
#     words = []
#     built_word = ""
#     vowel_count = 0
#     for letter in my_word:
#         if letter == " ":
#             if vowel_count >= 2:
#                 words.append(built_word)
#             built_word = " "
#             vowel_count = 0
#         else: 
#             built_word += letter
#             if letter in 'aeiou':
#                 vowel_count += 1
#     if vowel_count >= 2:
#         words.append(built_word)
#     return words

# print(two_vowel_string(user_string))



# phonebook = {}  # This initialilzes the dictionary(with no values).
# phonebook = {"matt":5073891438,"ashley":12345}
# print(phonebook)

# # To add to a dicitonary, we use name_of_dict[ key ] = value

# phonebook["waters"] = 7890

# print(phonebook)

# # To look up a value in a dicitonary, use name_of_dct[ key ]
# print(phonebook["matt"])

# # If we enter a key that is not known to the dictionary, it crashes with a KeyError

# # Recall that dicitonaries are non-sequential, so you can't iterate over it normally
# #  since the components of the list have no order. But you can use the built-in function:


# for person in phonebook.keys():
#     print(person)

# # But also python will automatically assume you're talking about the keys.

# for person in phonebook:
#     print(person)

# for person in phonebook:
#     print(person,phonebook[person])



# Write a function that takes a string as an argument and returns a dictionary containing
# all of the unique words in that string.

def string_to_dictionary(word):
    string_to_list = word.split()
    word_dictionary = {}
    for word in string_to_list:
        word_dictionary[word] = "in word"
    return word_dictionary

my_words = "ef;ahsi;asfh sjfhadhfa oasdfsdf dfhasjdfh aohdf;"
print(string_to_dictionary(my_words))

# Write a function that takes a string as an argument and
#  returns a dictionary that counts the number of times each word was used.

def string_to_dictionary(word):
    string_to_list = word.split()
    word_dictionary = {}
    for word in string_to_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    return word_dictionary

my_words = "ef;ahsi;asfh sjfhadhfa oasdfsdf dfhasjdfh aohdf;"
print(string_to_dictionary(my_words))


