class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2):
        new_real = self.real + num2.real
        new_img = self.img + num2.img
        return complex(new_real,new_img)
    
    def __sub__(self,num3):
        new_real = self.real - num3.real
        new_img = self.img - num3.img
        return complex(new_real,new_img)
    
num1 = complex(2,5)
num1.shownumber()
num2 = complex(5,8)
num2.shownumber()
num3 = num1 + num2
num3.shownumber()
num4 = num2 - num3
num4.shownumber()