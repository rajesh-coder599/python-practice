#dictionary
dictionary1 = {
    "name" : "Rajesh",  #key : value
    "age" : 19,
    "marks" : 76.5,
    "adult" : True,
    "subjects" : ["physics", "chemistry", "maths", "hindi"],
    "friends" : ("anuj", "aman", "himanshu", "gautam"),
    6 : "rajesh",
    6.45 : 3,
    4 : 7,
    (5,) : 5,
    True : "Rajesh"
}
#we can print any data type in dictionary 
print(dictionary1)
print(type(dictionary1))
print(dictionary1[True])#we can access value by using key
print(dictionary1["subjects"])
#dictonare are mutable(changeable)
dictionary1["subjects"] = ["python", "java", "c++"]
print(dictionary1["subjects"])
#we can add new values to the dictionary
dictionary1["surname"] = "Rayal"
print(dictionary1["name"] ,dictionary1["surname"])
#null ditionary
null_dictionary = {}
print(null_dictionary)
null_dictionary["name"] = "stephen"
print(null_dictionary["name"])

#nesting in dictionary
t = 70+77+81+90+75
student1 = {
    "name" : "Rajesh",
    "Roll number" : 1234,
    "subjects" : ["Python", "Java", "C++", "HTML", "C"],
    "marks in subjects" : {"Python" : 70,
                           "Java" : 77,
                           "C++" : 81,
                           "HTML" : 90,
                           "C" : 75},
    "Total number" : (t),
    "percentage" : t/5 

}
print(student1["marks in subjects"]["Java"])#access data in nested dictionary
