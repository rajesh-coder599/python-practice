class car:
    def __init__(self,color):
        self.color = color

class toyota(car):
    def __init__(self,name,color):
        super().__init__(color)
        self.name = name

car1 = toyota("fortuner","white")
print(car1.color)