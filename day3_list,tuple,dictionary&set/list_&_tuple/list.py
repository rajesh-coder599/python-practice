#list
age = [19, 20, 23, 16, 25]
print(age)
print(type(age))

#list also uses indexing
print(age[2])
print(age[-3])

#list can store any type of data
student1 = ["Rajesh",19,65.7,]
print(student1)
#list are mutable but strings are immutable
student1[1] = 20
print(student1)

#slicing in list
name = ["Rajesh", "Anuj", "Aman", "Rahul", "Himanshu", "Gautam"]
print(name[3:6])
name1 = name[2:5]
print(name1)
print(name1[0])
