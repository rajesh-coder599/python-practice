#set methods
set1 = set()
set1.add("Rajesh") #adds an element
set1.add(2)
set1.add(2)
set1.add((3,4,4))
print(set1)

set1.remove(2) #removes an element
print(set1)
print(len(set1))

set1.clear()
print(set1)
print(len(set1))

set2 = {2,5,"python", "Rajesh",20,5.6}
print(set2.pop()) #pops a random value of sets
print(set2.pop())
print(set2.pop())

set3 = {4,5,"python", "cool",20,3}
set4 = {4,"python" , 7, 19, "cool"}
print(set3.union(set4)) #union of both sets
print(set3.intersection(set4)) #intersection of both set
print(len(set3.union(set4)))
print(len(set3.intersection(set4)))