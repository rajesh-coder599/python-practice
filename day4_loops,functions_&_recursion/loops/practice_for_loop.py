#print the elements of the following list using a loop:
list1 = [1,4,9,16,25,36,49,64,81,100]
for el in list1:
    print(el)

#search for a number x in this tuple using loop:
tup1 = (1,4,9,16,25,36,49,64,81,100)
x = int(input("enter number: "))
for el in tup1:
    if(x==el):
        print("number found at the index of: ",tup1.index(x))
        break
else:
    print("number not found")