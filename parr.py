class parrot:
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
blue = parrot("Blue",10)
woo = parrot("Woo",15)

print("Blue is",blue.species)
print("Woo is",woo.species)

print("{} is {} years old".format(blue.name,blue.age))
print("{} is {} years old".format(woo.name,woo.age))
