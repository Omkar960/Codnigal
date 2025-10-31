class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
ob = car("BMW",123)
ob1 = car("AUDI",678)
print("{} model {}".format(ob.brand,ob.model))
print("{} model {}".format(ob1.brand,ob1.model))