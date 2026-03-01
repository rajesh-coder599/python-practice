#print fibonacci series n terms
fibonacci_series = [0,1]
n=10
for i in range(n-2):
    a = fibonacci_series[-1]+fibonacci_series[-2]
    fibonacci_series.append(a)
print(fibonacci_series)

#check if given list is sorted or not
list1=[1,2,3,4,5,3]
list2=list1.copy()
list2.sort()
if (list1==list2):
    print("given list is sorted")
else:
    print("given list is not sorted")

#sort the dictionary basis of value
student={
    1:"aman",
    2:"anuj",
    3:"himanshu",
    4:"gautam",
    5:"rajesh",
    6:"james",
    7:"emily",
    8:"tony",
    9:"odin",
    10:"bheem"
}
sorted_students = sorted(student.items(), key=lambda x:x[1])
print(sorted_students) 

#print factorial by using recursion
def factorial(n):
    if(n<0):
        return "not possible"
    elif(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

#print elemts that apears only one time in a list
list3 = [1,2,3,1,5,2,3,7,6,9]
list4=[]
for i in list3:
    if(list3.count(i)==1):
        list4.append(i)

print(list4)