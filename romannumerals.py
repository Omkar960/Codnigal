class number:
    def __init__(self):
        self.values = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

    def convert_to_roman(self, num):
        roman = ""
        for value, numeral in self.values:
            count = num // value
            roman += numeral * count
            num -= value * count
        return roman

    def method(self):
        try:
            obj = int(input("enter a number: "))
        except ValueError:
            print("Please enter a valid integer.")
            return

        if obj > 0:
            result = self.convert_to_roman(obj)
            print(f"{obj} in Roman numerals is: {result}")
        else:
            print("Number must be positive.")

num = number()
num.method()

    