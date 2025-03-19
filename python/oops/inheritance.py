class Father():
    def __init__(self):
        print("Father")
    def show(self):
        print("Show Method")
class Mother():
    def __init__(self):
        print("Motehr")
    def show(self):
        print("Show Method1")
class Child(Father,Mother):
    def __init__(self):
        print("Child")


c = Child()
c.show()