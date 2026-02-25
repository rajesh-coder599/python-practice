#reverse the string
str1 = input("enter text & reverse it: ")
str2 = ""
for char in str1:
    str2 = char + str2

print(str2)

# with slicing
print(str1[-1::-1]) #syntax: [start:end:step size]