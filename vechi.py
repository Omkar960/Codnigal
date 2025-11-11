class vechile:
    def __init__(self, name, maxspeed, mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage

class Bus(vechile):
    pass
schoolbus = Bus("Volvo",180,12)
print(schoolbus.name,schoolbus.maxspeed,schoolbus.mileage)