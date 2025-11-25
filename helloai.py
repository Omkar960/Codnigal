print("Hello I am an AI bot what's your name")
name = input()
print(" Hello",name,"how are you feeling today good or bad: ")

mood = input().lower()

if mood == "good":
    print("it's good to hear that")
elif mood == "bad":
    print("That's not nice to hear")
else:
    print("It's diffciult to put feelings in words")
    
print("It was good talking to you!")