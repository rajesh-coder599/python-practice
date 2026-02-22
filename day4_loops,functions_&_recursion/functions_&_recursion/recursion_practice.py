#Write a recursive function to calculate the sum of first n natural number
def num(n):
    if(n==0):
        return 0
    return num(n-1) + n
print(num(5))

#Write a recursive function to print all elements in a list
def el(a,b=0):
    if(b==len(a)):
        return
    print(a[b])
    el(a,b+1)
f = [1,2,3,4,5]
el(f,3)