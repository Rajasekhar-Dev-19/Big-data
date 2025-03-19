


# slicing
str1 = "Pyothon"
# substr1 = slice() #It throws TypeError: slice expected at least one argument
sbstr2 = slice(0) #It doesn't return anything meanwhile it doesn't throw any exception too.
substr3 = slice(0,len(str1))
# print(str1[substr3])
# It returns entire string
substr4 = slice(0,3);
# print("First three characters:",str1[substr4])
substr5 = slice(len(str1)-5,len(str1))
# print("Last Five characters:",str1[substr5]) # It returns last five characters.
substr6 = slice(0,len(str1),2)
# print("Increment by 2:",str1[substr6])
substr7 = slice(-7,-1)
print("Negative index:",str1[substr7]) # It returns string.
substr0 = slice(-1,-7)
# print(str1[substr0])
# reverse the string.
substr9 = slice(-1,-7,-1)
print(str1[substr9]) # reverse the string.
print(str1.index('o')) # if substring not found will throw an error
print(str1.rindex('o')) # it will start searching from left to right
print(str1.find('z')) # if sub-string returns -1 instead of an error
print(str1.rfind('o')) #it will start searching from right to left
print(str1[-1:-len(str1):-1])
print(str1[-7])

str1 = "Python"
join_str1 = ''.join(str1)
print(join_str1)
str2 = "Welcome 123 ###"
join_str2 = '->'.join(str2)
print(join_str2)