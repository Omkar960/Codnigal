class dog:
    colour = "blue"
    def __init__(self,age,breed):
        self.age = age
        self.breed = breed
ob = dog(5,"LAB")
ob1 = dog(7,"PUP")

print("{} is {} and {}".format(ob.breed, ob.age,ob.colour))
print("{} is {} and {}".format(ob1.breed, ob1.age,ob1.colour))


