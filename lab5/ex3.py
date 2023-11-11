#Create a base class Vehicle with attributes like make, model, and year,
# and then create subclasses for specific types of vehicles like Car, Motorcycle,
# and Truck. Add methods to calculate mileage or towing capacity based on the vehicle type.
class Vehicle:
    def __init__(self, make, model, year, fuel_capacity):
        if isinstance(make, str) and isinstance(model, str) and isinstance(year, (str, int)) and isinstance(fuel_capacity, (int, float)):
            self._make = make
            self._model = model
            self._year = year
            self._fuel_capacity = fuel_capacity


    def set_make(self, make):
        if isinstance(make, str):
            self._make = make
        else:
            return "Invalid type of parameter"

    def set_model(self, model):
        if isinstance(model, str):
            self._model = model
        else:
            return "Invalid type of parameter"

    def set_fuel_capacity(self, fuel_capacity):
        if isinstance(fuel_capacity, (int, float)):
            self._fuel_capacity = fuel_capacity
        else:
            return "Invalid type of parameter"

    def set_year(self, year):
        if isinstance(year, (int, str)):
            self._year = year
        else:
            return "Invalid type of parameter"

    def get_make(self):
        return self._make

    def get_model(self):
         return self._model

    def get_year(self):
        return self._fuel_capacity

    def get_make(self):
        return self._make

    def calculate_mileage(kilometers, consumed_liters):
        if consumed_liters > 0:
            mileage = kilometers / consumed_liters
            return mileage

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_capacity, doors,  number_seats, kilometers):
        super().__init__(make, model, year, fuel_capacity)
        if isinstance(doors, int) and isinstance(number_seats, int) and isinstance(kilometers, (int, float)):
            self._doors = doors
            self._number_seats = number_seats
            self._kilometers = kilometers

    def set_doors(self, doors):
        if isinstance(doors, int):
            self._doors = doors
        else:
            return "Invalid type of parameter"

    def set_number_seats(self, number_seats):
        if isinstance(number_seats, int):
            self._number_seats = number_seats
        else:
            return "Invalid type of parameter"

    def set_kilometers(self, kilometers):
        if isinstance(kilometers, (int, float)):
            self._kilometers = kilometers
        else:
            return "Invalid type of parameter"

    def get_doors(self):
        return self._doors

    def get_number_seats(self):
        return self._number_seats

    def get_kilometers(self):
        return self._kilometers

    def calculate_average_mileage(self):
        average_mileage = self._kilometers / self._fuel_capacity
        return average_mileage


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, fuel_capacity, engine, frame, agility_factor):
        super().__init__(make, model, year, fuel_capacity)
        if isinstance(engine, str) and isinstance(frame, str) and isinstance(agility_factor, (int, float)):
            self._engine = engine
            self._frame = frame
            self._agility_factor = agility_factor

    def set_engine(self, engine):
        if isinstance(engine, str):
            self._engine = engine
        else:
            return "Invalid type of parameter"

    def set_frame(self, frame):
        if isinstance(frame, str):
            self._frame = frame
        else:
            return "Invalid type of parameter"

    def set_agility_factor(self, agility_factor):
        if isinstance(agility_factor, (int, float)):
            self._agility_factor = agility_factor
        else:
            return "Invalid type of parameter"

    def get_engine(self):
        return self._engine

    def get_frame(self):
        return self._frame

    def get_agility_factor(self):
        return self._agility_factor

    def calculate_mileage(self, kilometers, consumed_liters, agility_factor):
        if consumed_liters > 0 and isinstance(consumed_liters, (int, float)):
            mileage = (kilometers / consumed_liters) * self._agility_factor
            return mileage


class Truck(Vehicle):
    def __init__(self, make, model, year, fuel_capacity, weight, horse_power, torque):
        super().__init__(make, model, year, fuel_capacity)
        if isinstance(weight, (int, float)) and isinstance(horse_power, int) and isinstance(torque, int):
            self._weight = weight
            self._horse_power = horse_power
            self._torque = torque

    def set_weight(self, weight):
        if isinstance(weight, (int, float)):
            self._weight = weight
        else:
            return "Invalid type of parameter"

    def set_horse_power(self, horse_power):
        if isinstance(horse_power, int):
            self._horse_power = horse_power
        else:
            return "Invalid type of parameter"

    def set_torque(self, torque):
        if isinstance(torque, int):
            self._torque = torque
        else:
            return "Invalid type of parameter"

    def get_weight(self):
        return self._weight

    def get_horse_power(self):
        return self._horse_power

    def get_torque(self):
        return self._torque

    def calculate_towing_capacity(self):
        towing_capacity = self._torque * self._horse_power - 2 * self._weight
        return towing_capacity


if __name__ == '__main__':
    vehicles = [Car("Toyota", "Camry", 2022, 60, 4, 5, 15000), Motorcycle("Honda", "CBR500R", 2022, 17, "500cc", "sport", 1.2), Truck("Volvo", "VNL 860", 2022, 800, 18000, 500, 1850)]
    for vehicle in vehicles:
        if isinstance(vehicle, Car):
            print(vehicle.calculate_average_mileage(), "km/l")
        if isinstance(vehicle, Truck):
            print(vehicle.calculate_towing_capacity())
        if isinstance(vehicle, Motorcycle):
            print(vehicle.get_frame())