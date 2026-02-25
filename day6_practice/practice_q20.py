#take two list & write common elements of it
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
list3 = list(set(list1).intersection(set(list2)))
print(list3)

common = []
#for loop
for el in list1:
    if(el in list2):
        common.append(el)
print(common)