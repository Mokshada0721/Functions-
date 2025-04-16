# functions: reuseble block of code or block of organized reusable code
# uses : avoid redundancy (repetition) easy debug or to reduce complexity
# define a function: using (def) keyword
# syntax for def keywords : def func_name(parameter):
# body
# return (expression)

# eg1:
''' def greet(name):    # define func
    print(f"hello, {name}!")
greet("swapnil")    # call func '''

# parameters and argument:
'''args is used to make a tuple of all arguments sent in a function.
kwargs or the keyword arguments are used when the arguments are to be stored in the from of dictionary'''
# eg2:1.positional keyword
'''def add(a,b):
    return a + b
print(add(5,10))'''
# default keyword :
'''def greet(name = "Guest"):
    print(f"Hello, {name}!")
greet()'''

# ares() and kwargs() :
'''def show(*args,**kwargs):
    print("Arguments", args)
    print("Arguments second", kwargs)
show(1,2,3,a=4,b=5)'''
'''args is used as a tuple for storing the number of single arguments in a tuple
any keyword arguments are store in the form of key and value pair'''

'''def operations (a,b):
    return a+b, a-b, a*b, a/b
print((operations(10,2))'''

# today's assessment:
# prime number using func
# factorial calculator using recurrsion

# eg:1
'''def prime(number):
    if number <=1:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % 1 == 0:
            return False
        return True

n = int(input("Enter a number:"))
if prime(n):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")'''

# eg:2
'''def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

number = int(input("Enter a number to calculate its factorial: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(number)
    print(f"The factorial of {number} is: {result}")'''

