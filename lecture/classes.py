#turns out inheritence from class oject is implicit who knew?
class Employee:
    def __init(self):
        self.first_name = ""
        self.last_name = ""

#car class added a bunch of extra attributes and methods
class Car(object):
    def __init__(self, make, model, vin_number,seats,color,year,engine):
        self.make = make
        self.model = model
        self.vin_number = vin_number
        self.seats = seats
        self.color = color
        self.year = year
        self.engine = engine
    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stoppping")

    def openDoor(self):
        print(f"the {self.color} {self.make} {self.model} opens its door ")

    def changeColor(self,to_color):
        self.color = to_color

#lets try inheritence user user()
class ElectricCar(Car):
    def __init__(self, make, model, vin_number,seats,color,year,engine,range):
        super().__init__(make, model, vin_number,seats,color,year,engine)
        self.range = range

    def start(self):
        print("starting the electric car")

electric_car = ElectricCar(1,2,3,4,5,6,7,1000)
print(electric_car.range)
electric_car.start()

#my own stuff not lecture related
class InheritCar(Car):
    def __init__(self, make, model, vin_number,seats,color,year,engine,extra, bonus):
        Car.__init__(self, make, model, vin_number,seats,color,year,engine)
        self.extra = extra
        self.bonus = bonus
    def start(self):
        print("Vroom Vroom")

example_car = Car("ur mum", "toy model", 12345, 4,"red",2019,"fast as hell 3000")

print(example_car.make)
example_car.changeColor("green and purple")
print(example_car.color)

fancy_car = InheritCar("fancy", "cool model", 54321, 2,"black",2020,"fast as hell 9000","extra","bonus")

print(fancy_car.bonus)
fancy_car.start()
fancy_car.stop()
fancy_car.openDoor()
