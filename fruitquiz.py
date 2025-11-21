import random
class fruitquiz:
    def __init__(self):
        self.fruits = {"apple":"red",
                       "banana":"yellow",
                       "orange":"orange",
                       "watermelon":"green",
                       "pear":"green"}
        
    def quiz(self):
        while (True):
            fruit, color = random.choice(list(self.fruits.items()))
            print("What is the colour of {}".format(fruit))
            useranswer = input()
            if(useranswer.lower() == color):
                print("That's correct")
            else:
                print("That's wrong")
            option = int(input("Press 0 to keep playing or 1 to stop: "))
            if(option):
                break

print("Welcome to the games")
fq = fruitquiz()
fq.quiz()
                  

