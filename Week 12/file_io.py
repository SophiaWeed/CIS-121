# Let's learn how to write from a file

# var_name = open("whatever your file name is.ext","w")
# that "w" is for writing, "r" for reading, "a" for append, "wr" for reading and writing


# Let's write 100 random integers.

from random import randint
my_file = open("numbers.txt","w")

for index in range(0,100):
    number = str(randint(50,250))
    my_file.write(f"{number}\n")
# also effective:
    # my_file.write(str(number)+"\n")


# How do we create a reference to this file?
# Also we need to finalize the file for security reasons and also so everything saves nicely
my_file.close()



'''

# Now we want to get iinformaton from the file. First we need a reference to the file:
my_file = open("numbers.txt","r")

data = my_file.readlines()
# Takes every character in the file and returns them all in one giant string.
# print(data)

# data = my_file.readlines() will return a list of lines.
for element in data:
    print(element)


total = 0
count = 0
for line in data:
    number = float(line)
    total += number
    count += 1
print(f"total = {total}")
print(f"avg = {total / count}")
# everything the file pulls is a string. So we type cast the lines

# find the average. We need the total and total number of numbers.

# monty carlos simulation can be used to predict behavior 
'''

# now i want to list all the people.

new_file = open("family.txt","w")

new_file.write("Name,Age,Occupation,Hobby\n")
new_file.write("Matt,39,Teacher,Running\n")
new_file.write("Dexter,8,Student,Reading\n")
new_file.write("Ashley,38,Important Teacher,Learning\n")

new_file.close()

my_file = open("family.txt","r")
data = my_file.readlines()
line_count = 0
age_total = 0
for line in data[1:]:
    line_data = line.split(",")
    occupation = line_data[2]
    age = line_data[1]
    age_total += float(age)
    name = line_data[0]
    line_count += 1
print(f"avg age = {age_total/line_count}")

# for line in my_file.readlines()[1:]: