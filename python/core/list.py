int_list = [1,2,3,4,5,6]
float_list = [5.6,6.3,8.2,7.9]
char_list = ['A','a','B','b']
str_list = ["ant","bat","cat","dog"]
hetro_list = [9,5.8,'A','Fox']
dup_list = [2,2,'A','A',"Cat","Cat",9.8,9.8]

"""--> length
--> type
--> access elements
--> positive index and negative index
--> int_list[],int_list[1],int_list[8],int_list[-1],int_list[-8],int_list[0:2],int_list[0:],int_list[:3]
--> add elements in the list [append] add element at the end of the list
	Eg:int_list.append(8)
--> add element at specific position [insert]
	Eg: int_list.insert(2,25) it will insert it will not overwrite.
--> add n elements into the list [extend]
	Eg: int_list1 = [7,8,9]
		int_list.extend(int_list1)
--> remove elements from the list [pop]
	Eg:int_list.pop()  --> remove last element in that list
--> remove specific element [remove]
	Eg:int_list.remove(2)
--> reverse a list [reverse]
--> sort the list [sort]
	Eg:int_list.sort() --> ascending by default
	--> Eg: int_list.sort(reverse=True)
	Other way we can use [sorted] global function
	Eg:sorted(int_list) --> ascending
	Eg:sorted(int_list,reverse=True)
--> aggregation operation like [min],[max],[sum]
	Eg:min(int_list)
	   max(int_list)
	   sum(int_list)
--> check element existed or not
	Eg:print(1 in int_list)
	   print(2 not in int_list)
--> fetch index [index]
	Eg:print(int_list.index(9))
	"""


