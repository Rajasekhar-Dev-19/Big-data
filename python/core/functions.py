# =================================  Functions ===============================================
# a function is a self-contained block of code that encapsulates a specific task or related group of tasks.
# Functions allows the re-usability of the code and avoid the code duplication.
# Functions are more readable and maintainable.
# Functions are easy to debug.
# We will achieve modularity.
# functions must have definition and function calling.
# functions are classified into two types.
# 1. built-in functions 2.user defined functions.
# functions will allow the arguments/parameters.
# functions will return the values.
# to define a user define functions we must use def keyword.
# methods are dependent on the objects.

""" We can define a function that doesn’t take any arguments, but the parentheses are still required.
Both a function definition and a function call must always include parentheses, even if they’re empty.
Occasionally, we may want to define an empty function that does nothing.
This is referred to as a stub, which is usually a temporary placeholder for a Python function that will be fully implemented at a later time.
Just as a block in a control structure can’t be empty, neither can the body of a function.
To define a stub function, use the pass statement.
"""

# concepts
# 1. Functions with no arguments
# 2. Positional Arguments
# def add(a,b):
#      c=a+b
#      print(c)
# add(1,2)

# 4.Default Values


# 5.Use the multiple Returns
# def check(num):
#     if num<0:
#         return num
#     if num >0:
#         return num
# print(check(10))

# 6.Keyword Arguments
""" we can specify arguments in the form <keyword>=<value>  
In that case, each <keyword> name must match with the parameter name in the Python function definition and function calling
Using keyword arguments lifts the restriction on argument order. 
Each keyword argument explicitly designates a specific parameter by name, 
so you can specify them in any order and Python will still know which argument goes with which parameter 
Like with positional arguments, though, the number of arguments and parameters must still match
"""
# def add(a, b):
#     c = a - b
#     print(c)
#
# add(a=1,b=2)

# 7. Arbitrary arguments
# def add(*j):
#     res = 0
#     for i in j:
#         res = res + i
#     return res
#
# print(add(10,20))
# print(add(1,2,3))
# print(add(1,2,3,4,5,6,7,8,9,10))

# 8. Arbitrary Key word arguments
def add(**j):
    res = 0
    for i,x in j.items():
        res = res + x
    return res

print(add(x=10,y=20))
print(add(x=1,y=2,z=3))
print(add(x=1,y=2,z=3,a=4,b=5,c=6,d=7,e=8,f=9,g=10))


"""
Functions --> ()
  --> Will get the modularity with functions.
  --> Builtin functions Eg:  input(), print(), type(), range()
  --> User define functions :
    --> functions names must be in lowercase.
    --> functions names must not be keywords, builtin functions names.
    --> if a function name contains two words then we can use camel case or snake case.
    --> We need to define the functions with def keyword.
    --> we must call that function, otherwise it will not execute.
    --> in order functions definition must be at first, fallowed by function calling.
  --> Function variants.
    --> Positional Arguments.
    --> Keyword Arguments.
    --> Default Arguments.
    --> Arbitrary arguments/Variable length arguments.
    --> Variable Length keyword arguments.
    --> Combination of all types.
  --> Lambda(Anonymous) Functions
  --> Higher order function
A higher-order function is one that either takes one or more functions as arguments or returns a function as a result
"""
# Arbitrary arguments
def print_numbers(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)

print_numbers(1, 2, 3, 4, 5)

# Variable Length keyword arguments.
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the Function
# display_info(name="Alice", age=25, city="Wonderland")


# Higher Order Function passing function as argument
def add(x,y):
    return x+y

def highFun(fun,x,y):
    return fun(x,y)
res_add = highFun(add,10,20)
# print("Sum is:",res_add)






