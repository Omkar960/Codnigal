from colorama import init, Fore, Style
import random

init(autoreset=True)


def game():
    aitool = " "
    win = 0
    attempt = 0 
    playerinput = input(f"{Fore.GREEN}Select between rock 🪨, paper 📃 or scissors ✂️: ")
    aitool = aitool + playerinput
    aitool = ""
    aitool  = aitool + playerinput
    a = "You lose!"
    t = "It's a tie"
    w = "It's a win"

    if aitool == "rock":
        aiiq= ["rock","paper","paper","scissors"]
        aichoice = random.choice(aiiq)
    elif aitool == "paper":
        aiiq = ["rock","paper","scissors","scissors"]
        aichoice = random.choice(aiiq)
    else:
        aiiq = ["rock","rock","paper","scissors"]
        aichoice = random.choice(aiiq)

    print(f"{Fore.YELLOW}AI chose: ",aichoice)
    print(f"{Fore.YELLOW}You chose:",playerinput)
    if playerinput == aichoice:
        print("It's a tie !")
        result = t
        attempt = attempt + 1

      
     
    elif playerinput.lower() == "rock" and aichoice == "scissors":
        print(f"{Fore.GREEN}You win!")
        win = win + 1
        result = w
        
    elif playerinput.lower() == "rock" and aichoice == "paper":
        print(a)
        result = a 
        attempt = attempt + 1
        
    elif playerinput.lower() == "scissors" and aichoice == "paper":
        print(f"{Fore.GREEN}You win!")
        win = win+ 1
        result = w
        attempt = attempt + 1
        print("You won in",attempt,"attempts")
        
    elif playerinput.lower() == "scissors" and aichoice == "rock":
        print(a)
        result = a 
        attempt = attempt + 1
        
    elif playerinput.lower() == "paper" and aichoice == "scissors":
        print(a)
        result = a 
        attempt = attempt + 1
        
    elif playerinput.lower() == "paper" and aichoice == "rock":
        print(f"{Fore.GREEN}You win!")
        win = win + 1
        result = w
        attempt = attempt + 1
        print("You won in",attempt,"attempts")
       
        
    
    
    while result ==  a or result == t:
        playerinput = input(f"{Fore.GREEN}Select between rock 🪨, paper 📃 or scissors ✂️: ")
        aitool = aitool + playerinput
        aitool = ""
        aitool  = aitool + playerinput
        a = "You lose!"
        t = "It's a tie"
        w = "It's a win"

        if aitool == "rock":
            aiiq= ["rock","paper","paper","scissors"]
            aichoice = random.choice(aiiq)
        elif aitool == "paper":
            aiiq = ["rock","paper","scissors","scissors"]
            aichoice = random.choice(aiiq)
        else:
            aiiq = ["rock","rock","paper","scissors"]
            aichoice = random.choice(aiiq)

        print(f"{Fore.YELLOW}AI chose: ",aichoice)
        print(f"{Fore.YELLOW}You chose:",playerinput)
        if playerinput == aichoice:
            print("It's a tie !")
            result = t
            attempt = attempt + 1

        
        
        elif playerinput.lower() == "rock" and aichoice == "scissors":
            print(f"{Fore.GREEN}You win!")
            win = win + 1
            result = w
            
        elif playerinput.lower() == "rock" and aichoice == "paper":
            print(a)
            result = a 
            attempt = attempt + 1
            
        elif playerinput.lower() == "scissors" and aichoice == "paper":
            print(f"{Fore.GREEN}You win!")
            win = win+ 1
            result = w
            attempt = attempt + 1
            print("You won in",attempt,"attempts")
            
        elif playerinput.lower() == "scissors" and aichoice == "rock":
            print(a)
            result = a 
            attempt = attempt + 1
            
        elif playerinput.lower() == "paper" and aichoice == "scissors":
            print(a)
            result = a 
            attempt = attempt + 1
            
        elif playerinput.lower() == "paper" and aichoice == "rock":
            print(f"{Fore.GREEN}You win!")
            win = win + 1
            result = w
            attempt = attempt + 1
            print("You won in",attempt,"attempts")
        else:
            ans = input(f"{Fore.GREEN}Do you want to play again(yes/no): ")
            if ans.lower() == "yes":
                for i in range(1):
                    game()
            else:
                print(f"{Fore.YELLOW}No problem")

game()
    




