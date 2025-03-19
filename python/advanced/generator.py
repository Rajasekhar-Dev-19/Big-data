"""
We don't have tuple Comprehension in Python,
if a Comprehension concept wrapped with the Parenthesis then it will become the Generator.
Generator must be a function we need to yield keyword in generator,
which function contains yield keyword then that function will become the generator.
overcome the memory issues as well performance issues
"""

# list comprehension
res = [x*x for x in range(1,2000)]
# res = [x*x for x in range(1,200000000000000000000000000)] # will get performance issue and memory issues
# print(res)

input_list = ['a', 1, 'y', 5, 'z', 99]
output_list = [int(item) for item in input_list if str(item).isdigit()]
# print(output_list)

"""



"""

# List comprehension
l = [x*x for x in range(10)]
# print(type(l))

# Generator
g = (x*x for x in range(10))
# print(type(g))

def gen(num):
    for i in range(1,num):
        yield i*i

x = gen(5)
for i in x:
    print(i)