#functions
def num(n):
    sum = n*(n+1)/2
    return sum
print(num(7))

def s(a,b):
    return a+b
print(s(1,2))

def sun(str): #fun with functions
    print(str)
    return str
sun("main dd hu")

#average of 3 number
def av(a,b,c):
    i = (a+b+c)/3
    print(i)
    return i
av(2,5,7)

def product(a=1,b=1): #default value for function
    print(a*b)
    return a*b
product() #calling without argument