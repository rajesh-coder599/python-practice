#WAF that replace all occurrences of "java" with "python" in the file that created
def r(a):
    with open("practice.txt","r") as f:
        data = f.read()
    new_data = data.replace("java",a)
    print(new_data)
    with open("practice.txt","w") as g:
        g.write(new_data)

    return

r("python")
