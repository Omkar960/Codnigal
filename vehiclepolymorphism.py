class BMW():

    def price(self):
        print("The price is £200000 ")
    def colour(self):
        print("The colour is black")
    def model(self):
        ("The model is a MX6")

class Porsche():

    def price(self):
        print("The price is £500000 ")
    def colour(self):
        print("The colour is red")
    def model(self):
        print("The model is a 9/11")
        
obj1 = BMW()
obj2 = Porsche()

for vec in (obj1,obj2):
    vec.price()
    vec.colour()
    vec.model()
    vec.model
