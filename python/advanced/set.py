"""

"""


s = {1,2,3}
s1 = {3,4,5}
# union
print("Union:",s.union(s1))
# intersection : Common element from the both sets A & B
print("Intersection:",s.intersection(s1))
# difference : he set containing all elements that are in set-A but not in set-B
print("Difference:",s.difference(s1))
# symmetric_difference : set containing all elements that are in either set-A or set-B
print("Symmetric Difference:",s.symmetric_difference(s1))
# difference_update : method is used to update a set by removing elements found in another set.
# This modifies the original set in place.
# s.difference_update(s1)
# print(s)
# intersection_update : is used to update a set by keeping only the elements that are also found in another set.
# This operation modifies the original set in place
# s.intersection_update(s1)
# print("intersection_update",s)
# symmetric_difference_update :
print(s.symmetric_difference_update(s1))
print("symmetric_difference_update",s)