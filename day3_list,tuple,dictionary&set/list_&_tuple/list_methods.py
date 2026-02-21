#this function only use in list
list = [1, 2, 5, 3, 4, 3, 4, 5]
list.append(4) #this will add 4 in list
print(list)
list.sort()#this will make list in increasing order
print(list)
list.sort(reverse=True)#this will  make list in dicreasing order
print(list)
list.reverse()#reverse the list
print(list)
print(list.sort(reverse=True))
print(list)
list1 = ["Rajesh", "Aman", "Anuj", "Rahul", "Himanshu", "Gautam", "Ayush"]
list1.sort() #we can use sort function on string also
print(list1)
list1.reverse()
print(list1)
list.insert(2,100) #we can insert an element in any index
print(list)
list.remove(100) #this will remove element fom list
print(list)
list1.remove("Aman")
print(list1)