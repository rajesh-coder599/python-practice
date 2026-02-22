#Recursion
def i(n):
    if(n==0):
        return
    print(n)
    i(n-1) #here the function will call itself
i(9)

def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
print(fact(5))