#WAP to store following word meanings in a python dictionary :
dictionary1 = {
    "table" : ("a piece of furniture" , "list of facts & figures"),
    "cat" : "a small animal"
}
print(dictionary1.get(input()))

#you are given list of subjects for students. Assume one classroom is required for 1 subject.
#How many classrooms are needed by all students.
subjects = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}
print("classroom required for subjects is: ", len(subjects))

#WAP to enter marks of 3 subjects from the user and store them in a dictionary.
#start with an empty dictioonary & add one by one. Use subjects name as key & marks as value.
dictionary2 = {}
dictionary2["physics"] = float(input("enter your physics marks: "))
dictionary2["chemistry"] = float(input("enter your chemistry marks: "))
dictionary2["maths"] = float(input("enter your maths marks: "))
print(dictionary2)
print("your total persentage is: ",(dictionary2["physics"]+dictionary2["chemistry"]+dictionary2["maths"])/3,"%")

#Figure out a way to store 9 &9.0 as separate values in the set.
set1 = {("float",9.0) , ("int",9)}
print(set1)
