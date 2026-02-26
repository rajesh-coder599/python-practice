class order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,odr2):
        return self.price>odr2.price
    
o1 = order("condom",50)
o2 = order("baby oil",100)
print(o1>o2)
