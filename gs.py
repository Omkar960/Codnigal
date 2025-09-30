import random
playing = True
number = random.randint(10,20)
print("A number from 10-20 will be generated: ")

while playing:
    guess = int(input("Guess a number from 10-20: "))
    if guess == number:
        print("You got it right")
        break
    else:
        print("Guess again")
    
