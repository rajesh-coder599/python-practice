#check if string is palindrome or not
i = input("enter a string: ")
j = list(i)
k = j.copy()
k.reverse()
if(j==k):
    print("given string is palindrome")
else:
    print("given string is not a palindrome")