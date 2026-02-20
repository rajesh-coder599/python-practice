marks = int(input("enter your marks: "))

if(marks>=90):
    print("grade = A")
elif(marks>=80):
    print("grade = B")
elif(marks>=70):
    print("grade = C")
elif(marks>=50):
    print("grade = D")
else :
    print("fail")


#nesting
temp = float(input("enter the temperature: "))

if(temp>=25):
    if(temp>=40):
        print("too hot to live")
        
    else :
        
        print("normal tempareture to live")


else :
    print("too cold to live")  