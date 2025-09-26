# Write a program that outputs the amount of deficient numbers, perfect numbers, and abundant numbers
#between 1 and some upper bound specified by the user. That’s it! Get coding!
# For each number between 1 and the upper bound, you need to:
# Find the proper divisors
# Find the sum of the proper divisors
# Determine if that sum is less than, equal to, or greater than the number itself.

# PROPER DIVISOR:  a divisor that is strictly less than the number. Ex: P. divisors of 20 are 1, 2, 4, 5, 10
# PERFECT NUMBER: a positive integer that is equal to the sum of its proper divisors. Ex: 6 has prop divs 1, 2, and 3. 1 + 2 + 3 = 6
# ABUNDANT NUMBER: pos int less than the sum of its proper divisors. Ex: 18 has prop div 1,2,3,6,9 which are greater than 18 when added
# DEFICIENT NUMBER: pos int greater than the sum of its prop divs
upper_bound = int(input("Enter a positive integer upper bound for a check: "))
candidate = 1
divisor_sum = 0
while candidate <= upper_bound: 
    for number in range(1,candidate): #FINDING PROPER DIVISORS
        if candidate % number == 0: # If prop div
            divisor_sum += number # Sum of prop divs
    candidate += 1


