i = 1
while  i<= 10:
    print(i)
    if (i==4):
        break #here the loop will break
    i += 1
print("continue after break")

j = 0
while j<=10:
    if (j == 5):
        j+=2
        continue #this will skip the step and continue after it
    print(j)
    j+=1

#even & odd number
k = 0
while k<=10:
    if(k%2!=0):
        k+=1
        continue
    print(k)
    k+=1