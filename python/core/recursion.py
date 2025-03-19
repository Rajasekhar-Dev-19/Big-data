"""Write a program for a Factorial?
--> O Factorial is 1
--> 1 Factorial is 1
--> 2 Factorial is:1*2 = 2
--> 5 Factorial is:1*2*3*4*5 = 120.
"""
def recursive_factorial(n):
    if n < 0:
        return "invalid number to calculate Factorial."
    elif n<2:
        return 1
    else :
        return n * recursive_factorial(n-1)

print(recursive_factorial(10))

def iterative_factorial(n):
    if n < 0:
        return "invalid number to calculate Factorial."
    elif n < 2 :
        return 1
    else:
        fact = 1
        for i in range(1,n+1):
            fact *= i
        return fact
print(iterative_factorial(10))

"""Write a program for a Factorial?
--> O Factorial is 1
--> 1 Factorial is 1
--> 2 Factorial is:1*2 = 2
--> 5 Factorial is:1*2*3*4*5 = 120.
Natural Numbers 1,2,3,4,5 -----
Whole Numbers 0,1,2,3,4,5----
Integers -+1,0,1
"""
print("Welcome To Python")
def recursive_factorial(n):
    if n < 0:
        return "invalid number to calculate Factorial."
    elif n<2:
        return 1
    else :
        return n * recursive_factorial(n-1)

x = recursive_factorial(5)
print(x)

# def iterative_factorial(n):
#     if n < 0:
#         return "invalid number to calculate Factorial."
#     elif n < 2 :
#         return 1
#     else:
#         fact = 1
#         for i in range(1,n+1):
#             fact *= i
#         return fact
# print(iterative_factorial(10))

