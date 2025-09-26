# def pool_time(grade , time):
#     time_output = ""
#     if grade == "k":
#         grade = 0
#     if 0 <= grade <= 3:
#         if time == "Morning":
#             time_output = "9 AM"
#         elif time == "Afternoon":
#             time_output = "1 PM"
#         else: 
#             print("Invalid time entered")
#     elif 4 <= grade <= 8:
#         if time == "Morning":
#             time_output = "10 AM"
#         elif time == "Afternoon":
#             time_output = "2 PM"
#         else: 
#             print("Invalid time entered")
#     elif 9 <= grade <= 12:
#         if time == "Morning":
#             time_output = "11 AM"
#         elif time == "Afternoon":
#             time_output = "3 PM"
#         else: 
#             print("Invalid time entered")
#     else:
#         print("Invalid grade entered")
#     return time_output

# grade = input("Enter grade k-12: ")
# time = input("Enter preferred time, Morning or Afternoon: ")
# print(f"The pool time is {pool_time(grade,time)}")



def money(user_knuts):
    output = ""
    
    num_galleons = user_knuts // (493)
    num_sickles = (user_knuts % (29*17))//17
    num_knuts = ((user_knuts % (29*17))%17)

    if num_galleons > 0:
        output += f"{str(num_galleons)} galleon(s) " 
    if num_sickles > 0:
        output += f"{str(num_sickles)} sickle(s) "
    if num_knuts > 0:
        output += f"{str(num_knuts)} knut(s)"
    return output


user_knuts = int(input("Enter # of knuts: "))
print(f"You have: {money(user_knuts)}")

#def leg_counter(num_pigs, num_chickens, num_cows):




# Q2 Strings
# Write a function is_fever
# Check the last character if it's F or C
# if F > 98.6 fever true
# if C > 37 fever true
# word = "98F"
# word[-1] = "F"              ([-1] always gives last character)
# word[:-1] = "98"            ([:-1] gives everything before the last character)

def is_fever(user_temp):
    if user_temp[-1] == "F":
        if int(user_temp[:-1]) > 98.6:
            return True
        else:
            return False
    elif user_temp[-1] == "C":
        if int(user_temp[:-1]) > 37:
            return True
        else:
            return False
    else:
        return False
    
user_temp = input("Enter your temperature as '32F' or '0C'")
print(is_fever(user_temp))


