class person ( object):
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.idnumber)
        print(self.name)

class employee ( person):
    def __init__(self,name,idnumber,salary,post):
        self.salary = salary
        self.post = post

        person.__init__(self,name,idnumber)
a = employee('rahul',8685858,292082389,"Intern")
a.display()