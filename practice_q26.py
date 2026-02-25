#WAF that count words in string
print("enter text to count word in it ")
def count_word(a):
    print(len(a)-a.count(" "))
    return
count_word(input())

