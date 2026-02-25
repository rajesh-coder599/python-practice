#WAF that find a average of list
def average(a):
    n = 0
    for i in a:
        n = n + i
    print(n/len(a))
    return
average([1,2,3])