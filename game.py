import random
import threading
import sys
import time

# Global variable to control the game loop
game_running = True

def stop_game():
    global game_running
    input("Press Enter to stop the game...")
    game_running = False

def play():
    global game_running
    choice = ["Rock", "Paper", "Scissors"]
    computer = random.choice(choice)
    values = {'1': "Rock", '2': "Paper", '3': "Scissors"}

    while game_running:
        user = input("Enter\n1 - Rock\n2 - Paper\n3 - Scissors\nEnter here (or press Enter to stop): ")
        if not user:
            game_running = False
            break

        user = values.get(user)
        if user is None:
            print("Enter the right value")
        else:
            break

    if not game_running:
        return

    print("User: " + user)
    print("Computer: " + computer)

    if computer == user:
        print("Draw !!")
    elif ((computer == "Rock" and user == "Scissors") or
          (computer == "Scissors" and user == "Paper") or
          (computer == "Paper" and user == "Rock")):
        print("Computer Wins!")
    else:
        print("You win!")

    time.sleep(2)
    timeout_thread = threading.Thread(target=play)
    timeout_thread.start()

if __name__ == "__main__":
    stop_thread = threading.Thread(target=stop_game)
    stop_thread.start()
    play()
