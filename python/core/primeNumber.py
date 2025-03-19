"""
a Natural number that is greater than one and only divides by itself and 1 (e.g:2,3,5,7,11)
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
In simpler terms,it means a prime number can only be divided evenly (without leaving a remainder) by 1 and by the number
itself.
"""

# WAP to find the given number is Prime or not ?

num = int(input("Enter any Number:"))

if num > 1:
    for i in range(2,num):
        if num % i == 0 :
            print(f"{num} is a Composite Number or not Prime Number")
            break
    else:
        print(f"{num} is a Prime Number")
else:
    print(f"Number {num} wont consider as Prime/Composite Number",end=' ')
    print("because Prime/Composite number will only applicable on Natural Numbers that to from 2 onwards")

import math
import time
def is_prime_v1(n):
    if n == 1:
        return "Unit Number"
    for i in range(2,n):
        if n % i == 0:
            return "is not a Prime Number"
    return "is a Prime Number"

def is_prime_v2(n):
    if n == 1:
        return "Unit Number"
    max_divisor = math.floor(math.sqrt(n))
    for d in range(2,1+max_divisor):
        if n % d == 0:
            return "is not a Prime Number"
    return "is a Prime Number"

def is_prime_v3(n):
    if n == 1:
        return "Unit Number"
    # if it's an Even and not 2, then it's not prime
    if n == 2:
        return "is a Prime Number"
    if n > 2 and n % 2 == 0:
        return "is not a Prime Number"
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3,1+max_divisor,2):
        if n % d == 0:
            return "is not a Prime Number"
    return "is a Prime Number"

# start_time = time.time()
# for i in range(1,21):
#     print(i,is_prime_v3(i))
# end_time = time.time()
# print("Time Taken:",end_time-start_time)

