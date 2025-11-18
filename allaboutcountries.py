class india:
    def cap(self):
        print("New Dehli is the capital of India")
    def lang(self):
        print("Hindi is the most speaken language in India")
    def type(self):
        print("India is a developing country")
    
class usa:
    def cap(self):
        print("Wahington Dc is the capital of the USA")
    def lang(self):
        print('English is the most spoken language in the USA')
    def type(self):
        print("USA is a developed country")

obj1 = india()
obj2 = usa()

for country in(obj1,obj2):
    country.cap()
    country.lang()
    country.type()