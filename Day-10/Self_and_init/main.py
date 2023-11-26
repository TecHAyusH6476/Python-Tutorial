# Encapsulation -> Binding data and functions into a single unit (class)


class Car:
    def __init__(self, a, b):
        self.color = a
        self.model = b
        self.engine_modified = True
        self.is_car_started = True

    def print_car(self):
        print("Car is ", self.color, " color and model = ", self.model)
        print("Car is started", self.is_car_started)

    def start_car(self):
        self.is_car_started = True

    def stop_car(self):
        self.is_car_started = False


my_car = Car(a="Red", b="HS-345")


my_car.stop_car()  # False
print(my_car.is_car_started)
my_car.print_car()

my_car.start_car()  # True
my_car.print_car()
