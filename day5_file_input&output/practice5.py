#from a file(even&odd.txt) containing numbers separated by comma,print the count of even numbers.
i = 0
with open("even_&_odd.txt","r") as f:
    data = f.read()
    nums = data.split(",")
    for val in nums:
        if(int(val)%2==0):
            i+=1
print(i)