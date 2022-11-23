# 1

class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(self.name, end="")


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"{self.name}, Author {self.author}, {self.page_count} pages")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"The Magazine {self.name}, Chief Editor {self.chief_editor}")

b = Book("Compartment No. 6 ", " Rosa Liksom", 192)
b.print_information()

m = Magazine("Donald Duck", "Aki Hyyppä")
m.print_information()


# 2

from Ex9 import Car

class ElectricCar(Car):
    def __init__(self, regNum, maxSpeed, battery):
        super().__init__(regNum, maxSpeed)
        self.battery = battery

    def print_travDis(self):
        print(f"TRavelled distance is {self.travDis}")

class Gasoline(Car):
    def __init__(self, regNum, maxSpeed, tank):
        super().__init__(regNum, maxSpeed)
        self.tank = tank

    def print_travDis(self):
        print(f"TRavelled distance is {self.travDis}")

electric_car = ElectricCar("ABC-15", 180, 52.5)
gas_car = Gasoline("ACD-123",165, 32.3)
electric_car.accelerate()

