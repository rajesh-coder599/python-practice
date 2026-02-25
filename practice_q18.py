#remove duplicate element from list
list1 = [1,1,2,2,3,4,5,5,5,1,69]
set1 = set(list1)
print(list(set1))

#for loop
unique = []
for el in list1:
    if (el not in unique):
        unique.append(el)
print(unique)