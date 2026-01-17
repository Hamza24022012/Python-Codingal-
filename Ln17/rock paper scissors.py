import random
while True:
    user=input("enter your choice[rock,paper,scissors]")
    options=  ["rock","paper","scissors"] 
    computer=random.choice(options)
    print("you chose",user)
    print("computer chose",computer)

    if user==computer:
        print("both players selected",user,"it's a tie")
    elif user=="rock":
        if computer=="scissors":
            print("rock smashes scissors,you win")
        else :
            print("paper covers rock,you lose")
    elif user=="paper":
        if computer=="rock":
            print("paper covers rock,you win")
        else :
            print("scissor cuts paper,you lose")
    elif user=="scissors":
        if computer=="paper":
            print("scissor cuts paper,you win")
        else :
            print("rock smashes scissors,you lose")
    play_again=input("play again[write y or n]")
    if play_again!="y":
        break

