import random
import threading
import sys
import time

# Global variable to control the game loop
game_running = True
score =0
def play():
    global game_running,score
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    choice = ["Rock", "Paper", "Scissors"]
    computer = random.choice(choice)
    values = {'1': "Rock", '2': "Paper", '3': "Scissors"}

    while game_running:
        user = input("Enter\n1 - Rock\n2 - Paper\n3 - Scissors\nEnter here ( 0 to stop): ")
        game_running=False if user=="0" else True
        if user=='0':
            print("Your Score is ",score)
            break
        user = values.get(user)
        if user is None:
            print("Enter the right value")
        else:
            break

    if not game_running:
        return
    print("------------")
    print("User: " + user)
    print("------------")
    print("Computer: " + computer)
    print("------------")
    if computer == user:
        print("Draw !!")
    elif ((computer == "Rock" and user == "Scissors") or
          (computer == "Scissors" and user == "Paper") or
          (computer == "Paper" and user == "Rock")):
        print("Computer Wins!")
    else:
        print("You win!")
        score+=1
while(game_running):
          play()
