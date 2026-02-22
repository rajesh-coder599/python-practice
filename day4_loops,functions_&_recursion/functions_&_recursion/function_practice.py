#WAF to print the lenght of a list
e = [4,5,6]
f = [" ",6,6,""]
def length(list):
    print(len(list))
    return
length(e)
length(f)

#WAF to print the elements of a list in a single line
def elements(list1):
    g = 0
    while g<len(list1):
        print(list1[g],end=" ")
        g+=1
    print("")
    return
h = ["oggy", "bob", "oly", "jack"]
elements(h)

#WAFto find the factorial of n
def fact(n):
    i = 1
    j=1
    while i<=n:
        j=j*i
        i+=1
    print("number",n,"factorial is:",j)
    return
fact(5)

#WAF to convert USD to INR
def converter(b):
    print("INR:",b*90.73)
    return b+90.73
converter(5)

#WAF to to find odd & even in given number
def find(z):
    if (z%2==0):
        print("even")
    else:
        print("odd")
    return
find(90)
