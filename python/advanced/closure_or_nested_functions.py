"""
Nested Functions is also called as closure
--> we never call inner functions outside which means python scripts
 A closure, unlike a function, allows the function to access those captured variables through the closure's reference
 to them, even when the function is invoked outside their scope
"""

def outer_fun():
    msg = "Hi"
    def inner_fun():
        print(msg)
    return inner_fun

res = outer_fun()
print(res)


def outer(num):
    x = num
    def inner():
        y = 10
        res = x+y
        return res
    return inner() # calling and return inner function

result = outer(100)
print(result)