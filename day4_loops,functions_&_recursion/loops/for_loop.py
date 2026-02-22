#for loop
list1 = [1,2,3,4]
for element in list1: #syntax for "for loop"
    print(element)
else:
    print("end") #this else is optional

str1 = "rajeshrayla"
for ch in str1:
    if(ch == "l"):
        print("l found")
        break
    print(ch)
else:
    print("end") # this would't exicuted if loop breaks