my_dict = {}
my_dict["my_key"] = "my_value"

print(my_dict)

def find_oldest(people):
    oldest_age = -1
    oldest_name = ""
    for name in people:
        if people[name] > oldest_age:
            oldest_age = people[name]
            oldest_name = name
    return oldest_name
    
# Events fnctions!

def skip_letter(word):
    built_list = []
    position = 0

    word = word.replace(" ", "")

    for letter in word:
        if position % 2 == 0:
            built_list.append(letter)           
        position += 1  
    return built_list

print(skip_letter("Banana sunday"))

def find_relation(name=" "):
    if name == "Darth Vader":
        return "Father"
    elif name == "Leia":
        return "Sister"
    elif name == "Han":
        return "Brother In Law"
    elif name == "R2D2":
        return "Droid"
    else:
        return "Unknown"
print(find_relation("Darth Vader"))

# 15

def is_negative(user_integer):
    return user_integer < 0

def is_odd(user_integer):
    return user_integer % 2 != 0

def report_negative_odd(user_list):
    # Check if each number is negative and odd
    built_list = []
    for number in user_list:
        if is_negative(number) and is_odd(number):
            built_list.append(number)
    return built_list

# 7 
def ascending_order(a,b=5,c=25):
    if a>b:
        a,b = b,a
    if a>c:
        a,c = c,a
    if b>c:
        b,c = c,b
    return [a,b,c]

print(ascending_order(100,40))
# 8
def descending_order(a,b=5,c=25):
    if a<b:
        a,b = b,a
    if a<c:
        a,c = c,a
    if b<c:
        b,c = c,b
    return [a,b,c]
print(descending_order(4))

# 1

def heads_or_tails(guess=0):
    from random import randint
    value = randint(0,1) #picks a random integer. Either 0 or 1
    return value == guess
print(heads_or_tails(1))

#3
def count_duplicates(num1=0,num2=0,num3=0):
    if num1 != num2 and num1 != num3 and num2 != num3:
        print("Each number is unique!")
    elif (num1 == num2 and num1 != num3 and num2 != num3) or (num1 != num2 and num1 == num3 and num2 != num3) or (num1 != num2 and num1 != num3 and num2 == num3):
        print("There are 2 of the same number.")
    elif (num1 == num2 and num2 == num3):
        print("There are 3 of the same number.")

count_duplicates(1,2,2)


def hailstone_seq(n=40):
    n = 25
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            print(n)
        else:
            n = (3*n)+1
            print(n)



