#create a dictionary
student = {
    "name" : "Rajesh Rayal",
    "age" : 19,
    "course" : "BTech"

}
print(student.keys())
print(student.values())

#add marks in previous dictionary & calculate percentage
student["subject"] = {"python" : 77,"java" :78,"c++" :75}
student["percentage"] = (77+78+76)/3
#search value from its key
print(student["percentage"])
print(student["age"])

#find maximum marks
marks = student["subject"]
max_marks = list(marks.values())[0]
for el in marks.values():
    if (el>max_marks):
        max_marks = el

print(max_marks)

#reversed dictionary in nested(vallue : key)
reversed_nested_dictionary = {}
for key,value in student["subject"].items():
    reversed_nested_dictionary[value]=key

reversed_dictionary = {}
for key,value in student.items():
    if type(value) != dict:
        reversed_dictionary[value] = key

final_dictionary = {}
final_dictionary.update(reversed_dictionary)
final_dictionary.update(reversed_nested_dictionary)
print(final_dictionary)