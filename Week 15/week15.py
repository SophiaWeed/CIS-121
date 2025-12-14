def is_odd(num):
    return num%2==1

def is_pos(num):
    return num>0

def is_odd_and_positive(num):
    return is_odd(num) and is_pos(num)
    '''if is_odd(num):
        if is_pos(num):
            return True'''

print(is_odd_and_positive(9))


def wacky_fct(num):
    print(num)
    if num > 25:
        return num
    return wacky_fct(num+1)


print(wacky_fct(10))
wacky_fct(10)
print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")


def factorial(num):
    if num == 0:
        return 1
    else:
        return num*factorial(num-1)
    
print(factorial(4))

def fibonacci(num):
    if num == 0 or num == 1:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)

print(fibonacci(5))