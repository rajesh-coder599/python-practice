#remove duplicate elements from given list
list1 = [1,2,3,2,4,7,3]
list2 = []
for i in list1:
    if(i not in list2):
        list2.append(i)

print(list2)

#rotate list from left by 1 in given list
def rotate(a,n):
    n=n%len(a)
    for _ in range(n):
        first = a.pop(0)
        a.append(first)
    print(a)

list3 = [1,2,3,4,5]
rotate(list3,3)

#find maximum value key in dictonary
dic1 = {
    1 : "aman",
    2:"anuj",
    3:"rajesh"

}

key = max(dic1,key=dic1.get)
print(dic1[key])