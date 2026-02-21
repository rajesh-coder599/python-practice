#WAP to ask the user to enter names of their 3 favorite movies & store them in list
print("write your three favorite movies")
movies = [input("1st: "), input("2nd: "), input("& 3rd: ")]
print(movies)

#WAP to check if a list contains a palindrome of elements.
list1 = [1,2,3,2,1,1]
list2 = list1.copy() #copy function copy the list
list2.reverse()
if(list1 == list2):
    print("given list contain palindrome of elements")
else:
    print("given list does not contain palindrome of elements")


#WAP to count the number of students with the "A" grade in the following tuple
tup1 = ("C", "D", "A", "A", "B", "B", "A")
print(tup1.count("A"))

#store the above values in a list & sort them from "A" to "D"
grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)