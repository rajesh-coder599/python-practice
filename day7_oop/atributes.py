class student:
    college = "gehu" #class attr
    def __init__(self,name,age):
        self.name = name #instance attr
        self.age = age

s1 = student("rajesh",19)
print(s1.name)
print(s1.age)
print(s1.college)