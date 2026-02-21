#dictionary methods
dictionary1 = {
    "name": "Rajesh",
    "age" : 19,

    "subjects" : {"math" : 55,
                  "physics" : 66,
                  "chemistry" : 67},
    "percentage" : (55+66+67)/3,
    "total number" : (55+66+67)

    }
print(dictionary1.keys())
#access all the keys in dictionary (but can't nested dictionary's key)
print(list(dictionary1.keys())) # type casting list

print(dictionary1.values()) #returns all values
print(list(dictionary1.values()))


print(dictionary1.items()) #returns all key value pair as tuple
i = list(dictionary1.items())
print(i[1])

print(dictionary1.get("name")) #return value acording to key
print(dictionary1["name"]) #it will get error if the key is wrong
print(dictionary1.get("name2")) # it would'nt give error even if key is wrong

print(dictionary1.update({"city" : "dehradun"})) #we can add new key value and even new dictionary
print(dictionary1)
new_dictionary = {"weight" : 65.87,
                  "hobie" : "sleeping",
                  "fav food" : "nothing",
                  "name" : "unknown"} #it will update the value of key if you pass same key
dictionary1.update(new_dictionary)
print(dictionary1)