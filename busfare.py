class vehicle:
    def __init__(self, seating_capacity, fare):
        self.seating = seating_capacity
        self.fare = fare
    def func(self):
        print(self.fare*110)

class bus(vehicle):
    def __init__(self, seating_capacity, fare):
        super().__init__(seating_capacity, fare)

obj = bus(50,50)
obj.func()





