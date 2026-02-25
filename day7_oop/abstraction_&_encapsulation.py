#abstraction
#Hiding the implementation details of a class and only showing the essential features to the user.
#example
class student:
    college = "abcd college"
    subject = "python"
    def __init__(self,name,marks,age):
        self.name = name
        self.marks = marks
        self.age = age
    
    def hello(self): #creating methods 
        print("hello",self.name)
    def get_marks(self):
        print(self.marks)
    @staticmethod #creating methods without self
    def nothing():
        print("nothing")

s1 = student("rajesh",75,19)
s1.hello()
s1.get_marks()
s1.nothing()

#Encapsulation
#wrapping data and functions into a single unit(all the things we do in class)