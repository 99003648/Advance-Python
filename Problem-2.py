class Temperature:
    def __init__(self, temp):
        self.temp_celsius = temp

    def temp(self):
        return self.temp_celsius

    def convert_to_celsius(self):

        self.temp_far = (9 / 5 * self.temp_celsius) + 32
        return round(self.temp_far, 3)

    def display(self):
        print(self.temp_celsius)

    def __add__(self, other):
        value = self.temp_celsius + other.temp_celsius
        return Temperature(value)

    def __eq__(self, other):
        if self.temp_celsius == other.temp_celsius:
            return True
        return False

    def __lt__(self, other):
        if self.temp_celsius < other.temp_celsius:
            return True
        return False


C1 = Temperature(45)
print(C1.convert_to_celsius())