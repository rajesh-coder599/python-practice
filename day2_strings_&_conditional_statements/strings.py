str1 = "hello github\nthis is my second day in python"
#by using \n sentence will continue printing by next line
print(str1)
len1 = len(str1) #we can find length of string by using len() function
print(len1)

str2 = "Rajesh"
str3 = " Rayal"
str4 = str2 + str3
#we can add two strings together by using +
print(str4)
print(len(str4))

#string functions
str5 = "i am a coder"
a = str5.endswith("apo")
#it will exicute if its true or not
print(a)

str6 = "cat"
print(str6.capitalize())
#this will capitalize first charechter of string but it only use one time
print(str6)

str7 = "i am learning new skill"
print(str7.replace("i","o"))
#this will replace all i from the string with the o
print(str7.replace("am learning","learned"))
#we can also replace sub string

str8 = "i am 19 year old"
print(str8.find("a"))
#find() function can find index of the charechter
print(str8.find("am"))

str9 = "i want small break after this"
print(str9.count("a"))
#this will find word or a charechter how many times reapeted in a string
print(str9.count("i"))