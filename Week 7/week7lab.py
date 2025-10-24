# dictionaries work!

# Question 4
# Write a function that takes a dictionary called names of tech ids and student names as key-value
# pairs, and returns a list containing just the student names.


# in a dictionary, keys are always unique, but ts value can be uniwue or not unique.
dict = {"01475":"Steve","12345": "Steve", "8765":"Sophia"}
print(dict)
for key in dict:
    print(key)
    print(dict[key])

def get_names(student_dictionary):
    names_list = []
    for key in student_dictionary:
        name = student_dictionary[key]
        names_list.append(name)
    return names_list
# same as
def get_names(student_dictionary):
    names_list = []
    for key in student_dictionary:
        names_list.append(student_dictionary[key])
    return names_list
print(get_names(dict))

# Write a function that takes a dictionary, called people, containing the names and ages of a group of
# people, and returns the name of the oldest person.

def find_oldest(people):
    oldest_age = -1
    oldest_name = ""
    for name in people:
        if people[name] > oldest_age:
            oldest_age = people[name]
            oldest_name = name
        return oldest_name


# Question 6
# Write a function that takes a string word and returns a dictionary containing the count of each letter
# in the word.

def letter_count(word):
    built_dictionary = {} # {letter:number of times the letter appears}
    for letter in word:
        if letter not in built_dictionary:
            built_dictionary[letter] = 1
        elif letter in built_dictionary:
            built_dictionary[letter] += 1
    return built_dictionary 


# To add a new entry to the dictionary:
dict0 = {}
dict0["Test"] = 1
print(dict0)

# Question 9 
# Initialize an empty dictionary named receipt, and then add the contents of the receipt as key-value
# pairs.
# (b) Using the dictionary you created in part a, write code that prints the total cost of all the items
# on the receipt. The code should work regardless of the contents of the receipt. (meaning don’t
# write print(6+12+3))


# for this problem, the key:value is item:cost
receipt = {}
receipt["Side Salad"] = 6
receipt["Chicken Parm"] = 12
receipt["Cookie"] = 3

def get_cost(receipt):
    total_cost = 0
    for item in receipt:
        total_cost += receipt(item)
    return total_cost

print(get_cost(receipt))













