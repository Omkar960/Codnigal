class bird:
    def __init__(self):
        print("Bird is ready")

    def whoisthis(self):
       print("Bird is ready")
    def swim(self):
        print("Swim faster")

class penguin(bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def whoisthis(self):
        print("penguin")
    def run(self):
        print("penguin")
peggy = penguin()
peggy.whoisthis()
peggy.swim()
peggy.run()