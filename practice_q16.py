# create a list of 5 number then find(max,min,sum)
print("enter five numbers to find max min & sum")
x = [int(input("1st: ")),int(input("2nd: ")),int(input("3rd: ")),int(input("4th: ")),int(input("5th: ")),]
max = x[0]
min = x[0]
sum = 0
for el in x:
    sum = sum + el
    if(max<el):
        max = el
    if(min>el):
        min = el

print("maximum is:",max)
print("minimum is:",min)
print("sum is:",sum)