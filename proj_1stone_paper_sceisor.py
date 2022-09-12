import random

Total_games=0
Your_score=0
computer_score=0
Tied=0

a=1

while(a!=0):
    print("0:for exit")
    print("1: for stone")
    print("2: for paper")
    print("3: for sciesor")

    a=int(input("enter your choice\n"))


    l1 = ["stone", "paper", "sciesor"]
    x = random.choice(l1)
    if(a==1):
        y="stone"
        print("your choice is stone")
    elif(a==2):
        y="paper"
        print("your choice is paper")
    elif(a==3):
        y= "sciesor"
        print("your choice is sciesor")
    else:
        print("Enter proper choice")
        break
    if(x=="stone"):
        if(y=="stone"):
            print("selected same")
            print("Match Tied")
            Total_games+=1
            Tied+=1
        elif(y=="paper"):
            print("you selected paper and computer selected stone ")
            print("You Won")
            Your_score+=1
            Total_games+=1
        else:
            print("You selected scisor and computer stone")
            print("You Lose")
            computer_score+=1
            Total_games+=1
    elif(x=="paper"):
        if(y=="stone"):
            print("You selected stone and computer selected paper")
            print("You Lose")
            Total_games+=1
            computer_score+=1
        elif(y=="paper"):
            print("Match Tied")
            Tied+=1
            Total_games+=1
        else:
            print("You selected sciesor and computer selected paper")
            print("You Won")
            Your_score+=1
            Total_games+=1
    else:
        if (y == "stone"):
            print("You selected stone and computer selected scisor")
            print("You won")
            Total_games += 1
            Your_score += 1
        elif (y == "paper"):
            print("You selected paper and computer selected scisor")
            print("You Lose")
            computer_score+=1
            Total_games += 1
        else:
            print("Match Tied")
            Tied+=1
            Total_games += 1

    z=f"Total_games={Total_games},computer_score={computer_score},Tied={Tied},Your_score={Your_score}"
    print(z)
