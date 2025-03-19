"""
List comprehension
List comprehension is a concise and elegant way to create lists in Python.
It allows you to generate lists by iterating over an existing iterable (like a list, tuple, or range) and applying an expression to each element.
Syntax: [expression for item in iterable if condition]
expression: The value to be included in the new list.
item: The variable that takes the value of the element from the iterable.
iterable: The collection of elements to iterate over.
if condition (optional): A conditional statement that filters elements based on a given condition.
"""

# write a program to add value 5 on each element without list comprehension
lst = [1,2,3,4,5]
new_lst = []
for i in lst:
    new_lst.append(i+10)
print(new_lst)

# write a program to add value 5 on each element with list comprehension

lst = [1,2,3,4,5]

new_lst = [i+100 for i in lst]
print(new_lst)

"""
This file contains List comprehension
Declaration; code not copied or refered from elsewhere
"""
# #List comprehensions
# #modifying a homogeneous numeric list elements
# list1 = [1, 2, 3, 4, 5, 6]
# list1 = [a*2 for a in list1]
# print(list1)

# #  list comprehension with a conditional
# #  list of all the factors for a given number
# num1 = int(input("Enter any number: "))
# factors1 = [x for x in range(1, num1) if num1 % x == 0]
# print(factors1)

#  list all the prime numbers within a given range
"""
a number divisible by 1 and only itself is called a prime number
"""
# r = int(input("Enter the range: "))
# #  this program used nested list comprehension
# primes = [x for x in range(2, r+1) if sum([x % a == 0 for a in range(2, x)]) == 0]
# print("There are ", len(primes), "prime number(s) between 0 to", r)
# print(primes)

"""
list all co primes within a given range of numbers
co-primes are number with only '1' as common factor
"""
# r = int(input("Enter the range : "))
# all_coprime_tuples = [(x, y) for x in range(2, r+1) for y in range(2, r+1) if len(set([a for a in range(2, x+1) if x % a == 0]).intersection(set([b for b in range(2, y+1) if y % b == 0]))) == 0]
#print(all_coprime_tuples)
#The above list contains duplicates, tried removing duplicates by set method (is there any other way?)
#Sets can not contain sets because, set elements must be immutable. Unhashable objects (TypeError)
# coprimes = []
# temp_list = [coprimes.append((i, j)) for (i, j) in all_coprime_tuples if (j, i) not in coprimes]
# i dont want to take any temporary list ..
# print("There are {} coprimes set(s) between 0 and {}, they are:-\n{}".format(len(coprimes), r, coprimes))


lst = []
print(lst)

for i in range(10):
    if i%2==0:
        print(i*i)

res = [i*i for i in range(10) if i%2==0]
print(res)

lst = [1,2,3,4,5]

