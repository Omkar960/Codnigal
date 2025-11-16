class reverse:
    def __init__(self, word):
        self.word = word
    
    def func(self):
        newstring = ""
        for i in range(len(obj)-1, -1, -1):
            newstring += obj[i]
        for i in range(len(obj1)-1, -1, -1):
            newstring += obj1[i]
        return newstring

class rev(reverse):
    pass

obj = "Codingal"
obj1 = "is"
r = rev(obj)
print(r.func())
