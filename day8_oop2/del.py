#del key used to delete object properties or object itself
class student:
    def __init__(self,name):
        self.name = name

s1 = student("thor")
print(s1.name)
del s1
print(s1.name)

