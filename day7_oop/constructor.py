#All classes have a function called __init__ 
#which is always executed when the object is being initiated.
class student:
    def __init__(self,name,age): #constructor
        print("adding new student in database:")
        self.name = name #instance atributes
        self.age = age

s1 = student("Rajesh",19)
print(s1.name)
print(s1.age)

s2 = student("anuj",21)
print(s2.name)
print(s2.age)