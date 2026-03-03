a = 10
d=a # deep copy
b = "ra"
c=[a,b]
print(id(a)) # addres of a
print(id(d)) # both addres are same
print(id(b))
print(id(c))

#split & join
str1="hello i am obsesd with this line"
print(str1.split())
print(str1.split("i"))
list1=['hello', 'i', 'am', 'obsesd', 'with', 'this', 'line']
print(" ".join(list1))
print("*".join(list1))

#ascii value
print(ord("#"))
print(ord("a"))
print(ord("5"))
print(ord("M"))