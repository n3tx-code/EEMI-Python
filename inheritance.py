class Vehicle:
    """
    Base class for motorized vehicles.
    All vehicles have a name, max speed, and passenger capacity.
    """

    def __init__(self, name, max_speed, capacity):
        self.name = name
        self.max_speed = max_speed
        self.capacity = capacity

    def move(self):
        print(f"{self.name} is moving at {self.max_speed} km/h.")

    def info(self):
        return f"{self.name} | max speed: {self.max_speed} km/h | capacity: {self.capacity}"

class Train(Vehicle):
    """
    Base class for trains.
    All trains have a name, max speed, capacity, number of wagons, and line name.
    """
    def __init__(self, name, max_speed, capacity, number_of_wagons, line_name):
        super().__init__(name, max_speed, capacity)
        self.number_of_wagons = number_of_wagons
        self.line_name = line_name

    def move(self):
        print(f"🚂 {self.name} runs on rails at up to {self.max_speed} km/h with {self.number_of_wagons} wagons (capacity: {self.capacity}) on line {self.line_name}.")


class Tram(Vehicle):
    """
    Base class for trams.
    All trams have a name, max speed, capacity, number of wagons, and line number.
    """
    def __init__(self, name, max_speed, capacity, number_of_wagons, line_number):
        super().__init__(name, max_speed, capacity)
        self.number_of_wagons = number_of_wagons
        self.line_number = line_number

    def move(self):
        print(f"🚊 {self.name} runs on urban rails at up to {self.max_speed} km/h with {self.number_of_wagons} wagons (capacity: {self.capacity}) on line {self.line_number}.")


class Plane(Vehicle):
    """
    Base class for planes.
    All planes have a name, max speed, capacity, and altitude max.
    """
    def __init__(self, name, max_speed, capacity, altitude_max):
        super().__init__(name, max_speed, capacity)
        self.altitude_max = altitude_max

    def move(self):
        print(f"✈️ {self.name} flies at up to {self.max_speed} km/h (altitude: {self.altitude_max} m).")



class Bicycle:
    """
    Base class for bicycles.
    All bicycles have a name, max speed, and capacity.
    """

    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
        self.capacity = 1

    def move(self):
        print(f"🚴 {self.name} is pedalling at up to {self.max_speed} km/h (human-powered).")

    def info(self):
        return f"{self.name} | speed: {self.max_speed} km/h | capacity: {self.capacity} (not a vehicle)"




tgv = Train("TGV", 320, 400, 8, "Paris–Lyon")
tram = Tram("Tram A", 70, 200, 5, "T2")
plane = Plane("Airbus A320", 850, 180, 12500)
ter = Train("TER", 160, 163, 3, "Lyon-Grenoble")

for vehicle in [tgv, ter, tram, plane]:
    print(vehicle.info())
    vehicle.move()
    print()

bike = Bicycle("Mountain Bike", 45)
print(bike.info())
bike.move()
print()
print("Bicycle is a Vehicle ?", isinstance(bike, Vehicle))
print("TGV is a Vehicle ?", isinstance(tgv, Vehicle))
