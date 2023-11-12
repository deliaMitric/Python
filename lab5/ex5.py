#Create a class hierarchy for animals, starting with a base class Animal.
# Then, create subclasses like Mammal, Bird, and Fish.
# Add properties and methods to represent characteristics unique to each animal group.

class Animal:
    def __init__(self, name, habitat, gender, weight):
        if isinstance(name, str) and isinstance(habitat, str) and isinstance(gender, str) and isinstance(weight, (int,float)):
            self._name = name
            self._habitat = habitat
            self._gender = gender
            self._weight = weight

class Mammal(Animal):
    def __init__(self, name, habitat, gender, energy, weight, can_swim=False, num_births=0, hungry=False):
        super().__init__(name, habitat, gender, weight)
        if isinstance(energy, (int, float)) and isinstance(num_births, (int, float)):
            self._energy = energy
            self._can_swim = can_swim
            self._num_births = num_births
            self._hungry = hungry
    def feed(self):
        if self._hungry:
            self._hungry = False
    def sleep(self, num_hours):
        if num_hours > 0:
            self._energy += num_hours * 2.5

    def give_birth(self, num_baby):
        if self._gender == "female":
            if num_baby > 0:
                self._num_births += 1
                self._energy -= num_baby * 3
                return True
        else:
            return False

class Bird(Animal):
    def __init__(self, name, habitat, gender, weight, beak_length, wingspan, num_eggs=0 , num_fish=0,  feather_colours=None, can_fly = False ):
        super().__init__(name, habitat, gender, weight)
        if isinstance(beak_length, (int, float)) and isinstance(num_eggs, int) and isinstance(num_eggs, int) and isinstance(can_fly, bool) and isinstance(wingspan, (int, float)):
            self._beak_length = beak_length
            self._num_eggs = num_eggs
            self._feather_colours = feather_colours if feather_colours else []
            self._can_fly = can_fly
            self._num_fish = num_fish
            self._wingspan = wingspan


    def lay_eggs(self, number_eggs):
        if self._gender == "female":
            if number_eggs > 0 :
                self._num_eggs += number_eggs
                return True
        return False

    def catch_fish(self, fish):
        if isinstance(fish, Fish):
            if (self._beak_length * self._weigth) > (fish.get_legth * fish.get_weight):
                self._num_fish += 1
                return True
        return False

    def flight_performance(self):
        if self._can_fly:
            return self._wingspan / self._weight
        return None

class Fish(Animal):
    def __init__(self, name, habitat, gender, weight, length, max_depth, swim=True, num_eggs=0):
        super().__init__(name, habitat, gender, weight)
        if isinstance(length, (int, float)) and isinstance(max_depth, (int, float)) and isinstance(num_eggs, int) and isinstance(swim, bool):
            self._length = length
            self._max_depth = max_depth
            self._num_eggs = num_eggs
            self.swim = swim

    def lay_eggs(self, num_eggs):
        if self.gender == "female":
            if num_eggs > 0:
                self._num_eggs += num_eggs
                return True
        return False

    def calculate_swimming_speed(self):
        if self._max_depth > 0 and self. swim:
            return (self._length * self._weight) / 2

if __name__ == '__main__':
    print("main")