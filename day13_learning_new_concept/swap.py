#swapin to variable without using thirde variable
a=4
b=5
a,b=b,a
print(a)
print(b)

list1=[1,2,3,4]
x=list1.pop()
print(x)