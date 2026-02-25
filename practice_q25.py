#write a recursive function to find a factorial of n
def factorial(n):
    if(n==1 or n==0):
        return 1
    elif(n>1 and type(n)==int):
        return n*factorial(n-1)
    else:
        return "factorial not possible"
    
print(factorial(5))