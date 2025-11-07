class IOString():
    def __init__(self):
        self.str1 = ""
    def getstring(self):
        self.str1 = input("Enter string: ")
    def printstring(self):
        print("Result is",self.str1.upper())
str1 = IOString()

str1.getstring()
str1.printstring()

