'''def add(a, b, c):
    print(a)
    print(b)
    print(c)
    d = a * b * c
    print(d)
add(5, 8, 5)
add(2, 3, 4)'''

# function parameter:
'''def add(y,z):
    c = y+z
    print(c)

add(20,30)
add(5,10)
add(50, 100)
add(200, 400)'''

#argument is same as parameter

#positional arguments
'''def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Ruturaj", "gaikwad")
my_function("MS", "Dhoni")'''

#variable length positional argument





# keyword argument





# variable length keyword argument





# default parameter
'''def my_function(country = "India"):
    print("I am from" + country)
my_function("Sweden")
my_function("india2")'''

# passing a list to function :





# return keyword : will return a value to function
'''def my_function(x):
    return 5 * x
print("15:-", my_function(3))
print(my_function(5))
print(my_function(9))'''

# lambda function : lambda function is a small anonymous/independent
# eg:
'''hey = lambda z: z + 10
print(type(hey))
print(hey(7))'''          #17
# eg:2
'''x = lambda a, b : a*b
print(x(5,6))'''

# eg3:
'''x = "python"
rev = lambda x: x.upper()
print(rev(x))'''


# methods in lambda
'''filter()
    map()
    reduce()'''




# today's assessment
'''1. input : 
Matrix A[0] [0] : 1
Matrix A[0] [1] : 2
Matrix A[1] [0] : 3
Matrix A[1] [1] : 4

Matrix A[0] [0] : 7
Matrix A[0] [1] : 6
Matrix A[1] [0] : 5
Matrix A[1] [1] : 4

print both the matrix 
Matrix A:
[1,2]
[3,4]

Matrix B :
[7,6]
[5,4]

2. Recursive lambda to generate permutation :-
a, b, c

a, b, c
a, c, b
b, c, a
c, b, a
c, a, b'''

# eg: 1
'''matrix_a = []
matrix_b = []

print("Enter elements for Matrix A:")
for i in range(2):
    row = []
    for j in range(2):
        value = int(input(f"Matrix A[{i}][{j}] : "))
        row.append(value)
    matrix_a.append(row)

print("\nEnter elements for Matrix B:")
for i in range(2):
    row = []
    for j in range(2):
        value = int(input(f"Matrix B[{i}][{j}] : "))
        row.append(value)
    matrix_b.append(row)

print("\nMatrix A:")
for row in matrix_a:
    print(row)


print("\nMatrix B:")
for row in matrix_b:
    print(row)'''

# eg: 2
'''permutations = lambda lst: (
    [lst] if len(lst) == 1 else
    [x + [y] for i, y in enumerate(lst) for x in permutations(lst[:i] + lst[i+1:])]
)

elements = ['a', 'b', 'c']

result = permutations(elements)

for perm in result:
    print(", ".join(perm))'''


