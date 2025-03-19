"""
lambda function : [one line function, in line functions, anonymous function, temporary function]
difference between regular function and lambda function.
for developing lambda functions we need to use lambda keyword.
lambda function will not have names
we will use lambda functions for single usage purpose.
lambda functions can't stored on memory.
adhoc
"""

def sum(a,b):
    c = a+b
    print(c)
# sum(5,10)
# sum(50,100)
# sum(500,10000)
# sum(5000,10000)

ans = 10+20 # expression
# print(ans)

add = lambda x,y: x+y
print(add(10,20))

res = lambda x,y:"X is Big" if x > y else "Y is Big"  # lambda function
# print(res(100,100))