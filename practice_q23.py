#create a function that add to number
def sum(a,b):
    return print(a+b)
sum(3,4)

#create a function that check if number prime or not
def find(a):
    if(a==2):
        print("prime number")
        return
    if(a>1):
        for i in range(2,a):
            if(a%i==0):
                print("not a prime number")
                return
                    
            else:
                print("prime number")
                return
    else:
        print("not a prime number")


    return

find(113)
