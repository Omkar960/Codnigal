import random

list = ["Rock" ,"Paper" ," Scissors"]
computergo = random.choice(list)
usergo = input("Choose from,Rock,Paper and Scissors:")
print("The computer chose",computergo)
print("You selected",usergo)

if usergo == computergo:
    print("it's a tie")
elif usergo == "Rock" and computergo == "Scissors":
    print("You won")
elif usergo == "Paper" and computergo == "Rock":
    print("You won")
elif usergo == "Scissors" and computergo == "Paper":
    print("You won")
else:
    print("You lost")