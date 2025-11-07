class Employee():
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Employeed destroyed")
obj = Employee()
del obj