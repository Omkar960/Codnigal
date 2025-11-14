class myclass:
    __prive = 27

    def __func(self):
        print("Im inside class myClass")
    def hello(self):
        print("private variable value:",myclass.__prive)

foo = myclass()
foo.hello()
foo.__func()