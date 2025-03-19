"""
collection of heterogeneous items
{}
heterogeneous : <meaning and usage>
key-value
keys are unique
values may be duplicated
key-values must be separated by colons
items must be separated by comma
name:Xyz
age:25
[1,2,3,4,5]
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
"""

# d = {}  # empty dictionary
dd = dict() # empty dictionary
# print(type(d))
# print(type(dd))

d1 = {'name':'Python','age':25,'branch':'CSE','marks':{'maths':75,'physics':85,'chemistry':96}}
# print(d1.items())
# print(d1.keys())
# print(d1.values())
# print(d1.get('name','Key is not there'))
# d1.update({'id':123,'habbits':'reading books'})
# print(d1)
# d1.pop('gender')
# print(d1)
# d1.popitem()
# print(d1)
# d1.popitem()
# print(d1)
# d1.clear()
# print(d1)

d2 = d1.copy()

# print(d1)
# print(id(d1))
# print(d2)
# print(id(d2))



edict = {"name":"Python","age":50,"mobile":1234567890}
# print(type(edict))
# print(len(edict))
# print(edict.get("name"))
# print(type(edict.keys()))
# print(edict.values())
# print(edict.items())
# print(edict['mobile'])
# edict["subjects"]=["Maths","Computers","Science"]
# print(edict['subjects'][0])
# edict.update({'X':123,'Y':456})
# print(edict)
# edict['name'] = 'Scala'
# sdict = sorted(edict,reverse=True)
# print(sdict)
# edict.pop("age")
# del(edict['name'])
# edict.clear()
# cdict = edict.copy()
# print(edict)
# print(cdict)
# a = 25
# print(a)
# b = a
# print(b)
# print(hex(id(a)))
# print(id(b))

# Comprehension
d = {1:'ant',2:'bat',3:'cat',4:'dog',5:'tiger'}
# print(d)
res = {k:v for k,v in d.items() if len(v) == 3 }
print(res)

nd = {1:0,2:0,3:0,4:0,5:0}
result = {k:k*k for k,v in nd.items() if v%2 == 0}

print(result)