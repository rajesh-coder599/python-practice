#print sum of digit
num1 = str(23)
sum = 0
for i in num1:
    sum +=int(i)

print(sum)

#find if elements of two list are same or not
list1 = [1,2,3,4]
list2 = [2,3,4,5,6]
print("common elements are",list(set(list1)&set(list2)))

#find a first non reapiting element in a string
str1 = "rajesh rayal"
for i in str1:
    if str1.count(i)==1:
        print(i)
        break

#return second largest number in list
list3 = [6,2,3,4,5]
list3.sort()
print(list3[-2])

#cpitalize first charechter of every word in sentence
sentence="hey am thanos i want my all power stones"
split = sentence.split()
new_sentence = " ".join(i.capitalize() for i in split)
print(new_sentence)

#check if given number is palindrome or not
num2=767767
num3 = list(str(num2))
num3.reverse()
num4 = int("".join(num3))
if(num2==num4):
    print("palindrome")
else:
    print("not a palindrome")

#reverse a list without using reverse() method
list4=[1,2,3,4,5]
start = 0
end = len(list4)-1
while start<end:
    list4[start],list4[end]=list4[end],list4[start]
    start+=1
    end-=1
print(list4)