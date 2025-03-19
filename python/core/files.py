"""
Operations -->  open, close, read(r), write(w), append(a)
Modes --> read & write r+,
"""

# open a file

f = open ('sample')

print(f.name) # it will prints the file name
print(f.mode) # ir will print the mode of the file like read, write and append
# print(f.read())