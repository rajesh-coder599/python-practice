#search if the word "learning" exist in the file or not
def finder(a):
    with open("practice.txt","r") as f:
        data = f.read()
        i = data.find(a)
        if(i==-1):
            print("your word does not exist")
        else:
            print("your word is exist at the index of:",i)
    return


finder(input())