# Write 100 integers created randomly into a file named QuizInts.txt. The numbers should be between
# 50 and 200 (inclusively). Each number should be on a new line.
# Hint: Your code will likely use the following two lines of code somewhere in your program.
# import random.
# random.randint(50,200)


import random

with open("QuizInts.txt","w") as quiz_ints:
    for numbers in range(0,100):
        quiz_ints.write(f"{random.randint(50,200)}\n")


# Write a Python program that will open a file named thisFile.txt and write every other line into the file
#thatFile.txt

with open("thisfile.txt","w") as this_file:
    this_file.write(f"Sophia\n")
    this_file.write(f"Ssphia\n")
    this_file.write(f"Soshia\n")
    this_file.write(f"Sopsia\n")
    this_file.write(f"Sophsa\n")
    this_file.write(f"Sophis\n")

with open("thisfile.txt","r") as this_file:
    data = this_file.readlines()

with open("thatfile.txt","w") as that_file:
    line_index = 0
    for line in data:
        if line_index % 2 == 0:
            that_file.write(f"{line}\n")
        line_index += 1

# A book club tracks how many pages each member read, stored in a file named PagesRead.csv. The file
# includes a header row and contains the member’s name and the number of pages they read for each
# book. Write a program that reads the file, stores the data in a dictionary where the key is the member
# name and the value is the total pages read by that member (across both books), and then prints each
# member’s name and their total pages read.


with open("PagesRead.csv","r") as page_file:
    dataline = page_file.readlines()
    reading_dict = {}

    for line in dataline[1:]:
        data = line.split(",")
        name = data[0]
        book1 = int(data[1])
        book2 = int(data[2])
        pages_read = book1 + book2
        if name in reading_dict:
            reading_dict[name] += pages_read
        else:
            reading_dict[name] = pages_read

print(reading_dict)


# 11. A music streaming app tracks how many times each user listens to different songs. The data is stored
# in a file called SongPlays.txt, which includes a header row. Each line contains the user’s name and
# the number of times they played a song on a given day. Write a program that reads the file, uses a
# dictionary to store the total plays per user, and then prints out each user and their total number of
# song plays.


with open("SongPlays.txt","r") as song_file:
    line_data = song_file.readlines()
    user_dict = {}
for line in line_data[1:]:
    data = line.split(" ")
    name = data[0]
    repeats = int(data[1])
    if name in user_dict:
        user_dict[name] += repeats
    else:
        user_dict[name] = repeats

print(user_dict)


# A weather station logs the temperature each day and stores the data in a file called DailyTempera-
# tures.csv. The file includes a header row and each line contains the date and the temperature recorded
# on that day. Write a program that reads the file, stores all the temperatures in a list, and then prints
# the highest, lowest, and average temperature recorded.

with open("DailyTemperatures.csv","r") as daily_temps:
    daily_data = daily_temps.readlines()
    temp_list = []

for line in daily_data[1:]:
    data = line.split(",")
    date = data[0]
    temp = int(data[1])
    temp_list.append(temp)

highest_temp = 0
lowest_temp = temp_list[0]
total_temp = 0
number_temps = 0
for temperature in temp_list:
    if temperature > highest_temp:
        highest_temp = temperature
for temperature in temp_list:
    if temperature < lowest_temp:
        lowest_temp = temperature
for temperature in temp_list:
    total_temp += temperature
    number_temps += 1
average_temp = total_temp/number_temps

print(f"Highest temperature is: {highest_temp}")
print(f"Lowest temperature is {lowest_temp}")
print(f"Average temp is {average_temp}")



# Create a python program that writes the name and age of everyone in your family to .csv file. There
# should be a column for the name with a header titled Name, and there should be a column for the age
# with a header titled Age. Do not use the csv module. You may make up fake family members if you
# choose. The result should look similar to the following.

with open("familyages.csv","w") as ages_file:
    ages_file.write("Name,age\n")
    ages_file.write("Sophia,20\n")
    ages_file.write("Amy,53\n")
    ages_file.write("Apollo,2\n")


#  Create a file named MyName.txt, and write your name to it (your actual name). Then read the file
# and print the letters of your name one at a time where each letter is on a new line

with open("MyName.txt","w") as name_file:
    name_file.write("Sophia Weed\n")

with open("MyName.txt","r") as name_file:
    data = name_file.readline()
    for letter in data:
        print(f"{letter}")

# ssume you are working on a file named MyCode.py and there is a file MyWords.txt in the same working
# directory (same folder). The MyWords.txt file contains exactly 20 words all written on separate lines.
# Read the file, and then write the words to a new file in four lines of five words

with open("MyWords.txt","w") as twenty_words:
    twenty_words.write("One\n")
    twenty_words.write("Two\n")
    twenty_words.write("Three\n")
    twenty_words.write("Four\n")
    twenty_words.write("Five\n")
    twenty_words.write("Six\n")
    twenty_words.write("Seven\n")
    twenty_words.write("Eight\n")
    twenty_words.write("Nine\n")
    twenty_words.write("Ten\n")
    twenty_words.write("Eleven\n")
    twenty_words.write("Twelve\n")
    twenty_words.write("Thirteen\n")
    twenty_words.write("Fourteen\n")
    twenty_words.write("Fifteen\n")
    twenty_words.write("Sixteen\n")
    twenty_words.write("Seventeen\n")
    twenty_words.write("Eighteen\n")
    twenty_words.write("Nineteen\n")
    twenty_words.write("Twenty\n")

with open("MyWords.txt","r") as twenty_words:
    word_data = twenty_words.readlines()
    twenty_words.strip()
    built_line = ""
    index = 0
    for word in word_data:
        if 4 >= index >= 0:
            index += 1
            built_line += f"{word} "
            if index == 5:
                print(f"{built_line}\n")
                index = 0
            


