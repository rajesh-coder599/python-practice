#inheritance (single inheritance)
class car:
    color = "black"
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stoped")

class toyotacar(car): #inheritance syntax
    def __init__(self,name):
        self.name = name

car1 = toyotacar("fortuner")
print(car1.name)
print(car1.start())
print(car1.color)

#multi level inheritance
class car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stoped")

class toyotacar(car): #inheritance syntax
    def __init__(self,brand_name):
        self.brand_name = brand_name

class fortuner(toyotacar):
    def __init__(self,color,speed):
        self.color = color
        self.speed = speed

car2 = fortuner("black","200km/h")
print(car2.start())

#multiple inheritance
class A:
    i = "this is a class A"

class B:
    j = "this is a class B"

class C(A,B):
    k = "this is a class C"

c1 = C ()
print(c1.i)
print(c1.j)
print(c1.k)
