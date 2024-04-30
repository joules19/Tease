class Car:
    def __init__(self, color: str, make: str, type: str ):
        self.color = color
        self.make = make
        self.type = type

    def drive(self):
        print("Car is driving")

new_car = Car("red", "Toyata", "Sedan")
print(new_car.make, new_car.type, new_car.color)