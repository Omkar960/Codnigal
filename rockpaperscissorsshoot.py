from colorama import init, Fore, Style
import random

init(autoreset=True)
ailist = ["rock","paper","scissors"]

def game():
    aitool = " "
    win = 0
    playerinput = input("Select between rock, paper or scissors: ")
    aitool = aitool + playerinput
    aichoice = random.choice(ailist)

    print(aichoice)
    print(playerinput)
    if playerinput == aichoice:
        print("It's a tie !")
      
     
    elif playerinput.lower() == "rock" and aichoice == "scissors":
        print("You win!")
        win = win + 1
        
    elif playerinput.lower() == "rock" and aichoice == "paper":
        print("You lose")
        
    elif playerinput.lower() == "scissors" and aichoice == "paper":
        print("You win!")
        win = win+ 1
        
    elif playerinput.lower() == "scissors" and aichoice == "rock":
        print("You lose!")
        
    elif playerinput.lower() == "paper" and aichoice == "scissors":
        print("You lose!")
        
    elif playerinput.lower() == "paper" and aichoice == "rock":
        print("You win")
        win = win + 1
       
        
    else:
        playerinput = input("Could you rephrase")
    choice = input("Do you want to play again: ")
    if choice.lower() == "yes":
        for i in range(1):
            game()
    else:
        print("No problem")
    

game()






