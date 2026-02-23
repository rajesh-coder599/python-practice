#WAF to find in which line of the file does the word "learnin" occur first
def line_finder():
    word = input()
    data = True
    line = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print("faound at line:",line)
                return
            line += 1
    return -1

line_finder()