#Name: Riva Crystal
#Email: riva.crystal@gmail.com
#Date: November 10, 2021
#This program makes a rock-paper-scissors game

import random

game = True
winner = ""
         
while game:
        playerMove = int(input("enter 1 for rock, 2 for paper, or 3 for scissors: "))

        if playerMove < 1:
                break

        computerMove = random.randint(1,3)
        print(f"computerMove: {computerMove}")

        if playerMove > 3:
                winner = "invalid"

        elif playerMove == computerMove:
                winner = "draw"

        elif playerMove == 1:
                if computerMove == 2:
                        winner = "computer"
                else:
                        winner = "human"

        elif playerMove == 2:
                if computerMove == 3:
                        winner = "computer"
                else:
                        winner = "human"

        elif playerMove == 3:
                if computerMove == 1:
                        winner = "computer"
                else:
                        winner = "human"
        print (f"round finished and winner is: {winner}")

print(f"game finished and winner is: {winner}")
