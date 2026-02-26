class student:
    name = "unknown"

    def changename(self,name):#this would not change class 
        self.name=name

    def changename1(self,name):
        student.name=name #this will change class name variable
        self.__class__.name=name #this will also change

    @classmethod #class decoretor
    def changename2(cls,name):#this repersents the class and this will change the name variable
        cls.name=name

s1 = student()
s1.changename("rajesh")
print(s1.name)
print(student.name)
s1.changename1("rajesh")
print(student.name)
s1.changename2("rajesh")
print(student.name)
