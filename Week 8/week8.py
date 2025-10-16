# Hi

# total = 0
# user_number = input("Enter a number or type q")

# while user_number != "q":
#     total += int(user_number)
#     user_number = input("Enter a number or type q")

# print(f"total = {total}") 


# dict[key] produces the value
# pass the key through the dictionary to obtain the value

test_dict = {}
#test_dict["apple"]
# results in keyerror. apple is not in the dictionary.

# def letter_counter(word):
#     letter_dict = {}
#     for letter in word:
#         if letter in letter_dict:
#             letter_dict[letter] = letter_dict[letter] + 1
#         else:
#             letter_dict[letter] = 1
#     return letter_dict

my_word = "peter piper picked a peck of pickled peppers"
# print(letter_counter(my_word))


# store a list of words consisting of all words with 2 or more vowels
# take "peter piper picked a peck of pickled peppers" and return
#  ["peter", "piper", "picked", "pickled", "peppers"]
def string_to_list_with_vowels(word):
    words = []
    # collect a word
    built_word = ""
    vowel_count = 0
    for letter in word:
        if letter == "":
            if vowel_count >= 2:
                words.append(built_word)
        else: 
            built_word += letter
            if letter in "aeiou":
                vowel_count += 1

        
    return words

print(string_to_list_with_vowels(my_word))
