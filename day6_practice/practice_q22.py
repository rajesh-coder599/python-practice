#reversed dictionary
student = {
    "name" : "Rajesh Rayal",
    "age" : 19,
    "course" : "BTech"

}

reversed_student = {}
for key,value in student.items():
    reversed_student[value] = key

print(reversed_student)