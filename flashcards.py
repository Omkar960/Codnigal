class flashcard:
    def __init__(self,word,meaning):
            self.word = word
            self.meaning = meaning
    def __str__(self):
          
          return self.word+ "("+ self.meaning +")"
flash = []
print("welcome to flashcard game: ")

while True:
      word = input("Write the object of card: ")
      meaning = input("Write the meaning of card: ")
      
      flash.append(flashcard(word,meaning))
      option = int(input("to continue press 0 to continue or 1 to quit:  "))
      if (option):
            break

print("Your flashcards")
for i in flash:
      print(i)
