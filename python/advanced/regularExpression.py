import re

# literal characters
# \d --> Digit (0-9)
# \D --> except Digits (0-9)
# \w --> word character (a-z) (A-Z),(0-9)
# \W --> not a word character
# \s --> white spaces (space, new line, tab)
# \S --> except white spaces (space, new line, tab)

# Meta characters
# .(dot) --> any character except new line
# ^ beginning a string
# $ end of a string
# \ 	Signals a special sequence (can also be used to escape special characters)
# | 	Either or
# [] 	Matches characters in braces
# () 	Capture and group
# {} 	Exactly the specified number of occurrence

# anchors
# \b --> word boundary ()
# \B --> not word boundary ()

# Quantifiers
# ? 0 or one
# * 0 or more
# + 1 or more

# a --> exact match
# a+ --> at least one a
# a* --> any number of a's including 0 a's
# a? --> atmost one a
# a{n} --> exactly number of a's
# a{m,n} --> minimum number of a's to maximum number of a's

x = """123-456-789
456.123.789
789-456.123
123.456-123"""
# res = re.findall(r"\d",x) it returns all arbitrary digits elements into the list except symbols
# res = re.findall(r"\d\d\d.\d\d\d.\d\d\d",x) #it returns ['123-456-789', '456.123.789', '789-456.123', '123.456-123']
# because we specified .(Dot) only dot will include anything except new line character.
# res = re.findall(r"\d\d\d\.\d\d\d\.\d\d\d",x) it returns [456.123.789] because we specified
# \.(Backward slash with Dot) significantly.


# res = re.findall(r"\d\d\d[-.]\d\d\d[.-]\d\d\d",x)
# square braces take n number of literal characters meta characters and digits
# if we want search for a explicitly character like a then we need to define [a].
# if we want to give multiple characters like [-*] now it can be true whether character may be a (-) or (*).
# if we want to give multiple characters like [abc] now it can be true whether the character may be a,b,c.
# now if we want search except a,b or c [^abc]. now caret will exclude a or b or c from input string or file.
# now if we want search any lower case character from a to z then [a-z] now python regular expression
# will treat it as a to z which means it will cover 26 lower case alphabet. but not either a or -(hyphen) or b.
# now if we want search any lower case or upper case character from a to z then [a-zA-Z] now python regular expression
# will treat it as lower case (a to z) or upper case (A-Z) which means it will cover 26 lower case and upper case alphabet
# but not either a or -(hyphen) or b as well as upper case.
# if we want search any digit from 0 to 9 then we will define [0-9].
# if we want special character(symbols) then we will define [^a-zA-Z0-9].

# print(res)

# methods
# -------
# Compile()
#  -->  we need to give searching pattern in compile method like pattern = re.compile ("python")
# finditer()
# --> we will get how many matches are there in input string with their positions.
# re.finditer(pattern,x)
#start()
# start index of the match pattern
# end()
# end+1 index of the match pattern
# group()
# return matched strings
# search()
# match()
# fullmatch()
# findall()
# sub() method will work as replace
# subn() it returns int which means how many replacements were happen.
# split() will split based on the given delimiter

# Quantifiers
# ? 0 or one
# * 0 or more
# + 1 or more

s = """I have two dogs
one dog name is puppy
another dog name is tomy
dogs
"""
# now we have to found dog or dogs from the input string ?
res = re.findall(r"dogs?",s)
print(res)

# anchors
# \b --> word boundary ()
# \B --> not word boundary ()

"""
The small letter "\b" word boundary indicates that a pattern is bounded by a non-word character. 
Non-word characters are all characters apart from numbers, letters, and underscore (_).
"""
# s = "apple apples pineapple"
# res = re.findall(r"\wapple\w",s)

# mobile_numbers = """
# +91 9876543210
# +91 8976543210
# +91 7894563210
# +91 9876543219
# +91 8976543218
# +91 7896543217
# """

mobile_numbers = """
9876543210
8976543210
7894563210
9876543219
8976543218
7896543217
"""
# res = re.findall(r"\d\d\d\d\d\d\d\d\d0",mobile_numbers)
# print(res)
