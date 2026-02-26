#define cicle class which calculate area & perimeter of circle
class circle:
    def __init__(self,r):
        self.r = r

    def area(self):
        return 3.14*(self.r**2)

    def perimeter(self):
        return 2*3.14*(self.r)

c1 = circle(5)
c1.area()
c1.perimeter()

#define a employee class & create a showdetails method
class employee:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary

    def show_details(self):
        print("role is:",self.role)
        print("department is:",self.department)
        print("salary is:",self.salary)

emp1 = employee("majdoor","labour","70,000")
emp1.show_details()

class engineer(employee):
    def __init__(self,name,age,role,department,salary):
        super().__init__(role,department,salary)
        self.name = name
        self.age = age

    def show_final_details(self):
        print("name is:",self.name)
        print("age is:",self.age)
        print("role is:",self.role)
        print("department is:",self.department)
        print("salary is:",self.salary)

eng1 = engineer("elon musk",89,"majdoor","labour","7,00")
eng1.show_final_details()
