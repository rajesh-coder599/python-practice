#print numbers from 1 to 100
i = 1
while i<=100:
    print(i)
    i += 1

#print numbers from 100 to 1
j = 100
while j>=1:
    print(j)
    j -= 1

#print the multiplication tadle of a number n
k = int(input("enter number: "))
x = 1
while x<=10:
    print(x*k)
    x += 1

#print the elements of the following list using a loop
y = 1
list1 = []
while y<11:
    list1.append(y*y)
    y += 1
print(list1)

#search for a number x in this tuple using loop
tup = (1,4,9,16,25,36,49,64,81,100)
z = int(input("enter number: "))
num = 0 
while num<len(tup):
    num += 1

    if z == tup[num]:
        print("number is in the tuple")
        break