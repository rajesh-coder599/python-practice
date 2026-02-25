#guess the number game
i = 7
j = int(input("guess the right number: "))
if(i==j):
    print("you guessed the right number")
    i +=1
    if(int(input("guess again: "))==i):
        print("your guess is again corect")
    else:
        print("try again")
else:
    print("try again")