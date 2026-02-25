#count vowels in any string
i = input("enter text here to find the number of vowels in it: ")
j = i.count("a")
k = i.count("e")
a = i.count("i")
b = i.count("o")
c = i.count("u")

print(j+k+a+b+c)

#using for loop
vowels = "aeiouAEIOU"
count = 0
for el in i:
    if el in vowels:
        count += 1

print(count)