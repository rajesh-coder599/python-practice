#private attribute & methods are meant to be used only within the class and are not accessible from outside the class.
class student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks = marks #private attributes

    def __body_count(self): #private methods
        if(self.__marks<45):
            return 1
        
    def find_body_count(self):
        return self.__body_count()
        
s1 = student("loky",40)
print(s1.name)
print(s1.find_body_count())
print(s1.__body_count) #this will get error