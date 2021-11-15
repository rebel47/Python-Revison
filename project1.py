'''We all have played snake, water, gun game in out childhood. If you haven't, google the rules of this game and write a
python program capable of playing this game with the user'''


import random


def game():
    num =10
    compScore = 0
    playerScore = 0
    i=0
    while i<=num:
        randNo= random.randint(1,3)
        if randNo== 1:
            compChoice = "s"
        elif randNo==2:
            compChoice="w"
        elif randNo==3:
            compChoice="g"

        yourChoice = input("Player's turn: SNAKE(s) WATER(w) GUN(g): ")
        if yourChoice ==compChoice:
            print("It's a Draw")
        elif yourChoice == "s" and compChoice=="w":
            print("You Wins!!")
            playerScore=playerScore+ 1
        elif yourChoice == "w" and compChoice=="g":
            print("You Wins!!")
            playerScore=playerScore+ 1
        elif yourChoice == "g" and compChoice=="w":
            print("You Wins!!")
            playerScore=playerScore+ 1
        elif yourChoice == "s" and compChoice=="g":
            print("Computer Wins!!")
            compScore =compScore+1
        elif yourChoice == "w" and compChoice=="s":
            print("Computer Wins!!")
            compScore =compScore+1
        elif yourChoice == "g" and compChoice=="s":
            print("Computer Wins!!")
            compScore =compScore+1
        print(f"{num-i}times left!")
        i=i+1
        
    if playerScore>compScore:
        print(f"You Wins with a score of:{playerScore} out of 10 and computer score is {compScore}")
    elif playerScore<compScore:
        print(f"Sadly you lose the game with a score of {playerScore} and computer score is {compScore}")

    



game()

