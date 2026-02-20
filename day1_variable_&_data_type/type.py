a = "rajesh"
b = 55
c = 5.05
d = True
e = None
f = "66"

#type
#we can find type of variable by using type function
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))



#type conversion
#which conversion python do automaticaly we call it type conversion
print(c + b)#python converted int b into float


#type casting
#conversion that we do manualy is called type casting
i = str(d) + str(e)
print(type(i))
print(i)
j = int(f) + b
print(type(j))
print(j)
k = float(b) + float(f)
print(type(k))
print(k)