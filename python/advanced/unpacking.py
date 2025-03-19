"""
Unpacking is a mechanism to extract the individual elements from the list
*_ is an exclude operator.

We can unpack any iterate variable.
"""

# x = 10
# y = 'ant'
#
# a,b = str(x)
# print(a)
# print(b)

lst = [1,2,3,4,5,6,7,8]
# We can unpack desired position elements from the list
a = lst[0]
b = lst[1]
c = lst[3]

# print(a)
# print(b)
# print(c)

# If we want to unpack elements in sequence
# x,y,z,xy = lst

# print(x)
# print(y)
# print(z)
# print(xy)
# Note: variables and list elements length doesn't match then will get bellow error
# --> "ValueError: too many values to unpack (expected 3)"

# If we want to unpack desired sequence of elements, which means only unpack first two or last two elements
# ab,cd,*_ = lst  # First two elements from the list
# *_, ab, cd = lst  # last two elements.
# ab,cd,*exc = lst # it will keep excluded records into the list form.
# *st,ab,cd,*end = lst # This syntax will throw an error, it doesn't allow the multiple starred (*) expressions.

# print(st)
# print(ab)
# print(cd)
# print(end)
# print(exc)
# print(type(*exc))

# unpack the nested lists
list_2 = [1,2,3,[5,6,7]]
*ab,cd,*exclude,(xy,*_) = list_2

print(ab)
print(cd)
print(exclude)
print(xy)
print(*_)







