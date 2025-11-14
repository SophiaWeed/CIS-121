

import math

class Planet:
    def __init__(self,_name,_radius, _mass, _distance): # the constructor always needs to reference itself! 
        # We want it to be able to pass in a name and also assign itself a name
        self.name = _name
        self.radius = _radius
        self.mass = _mass
        self.distance = _distance
    def get_name(self):
        return self.name
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_distance(self):
        return self.distance
    def get_volume(self):
        volume = 4/3 * math.pi * self.radius ** 3
        return volume
    def get_density(self):
        density = self.mass / self.get_volume() # What is the difference between a function and a method?
        return density
    def set_name(self,new_name): # We need to assign the new name. Frequently we do not return information, we just change it.
        self.name = new_name
    def __str__(self):
        msg = ""
        msg += f"hello {self.get_name()}, how are you?"
        return msg



planet1 = Planet("x25",4,5,6)
planet2 = Planet("z37",7,8,9)

#print(planet1.get_name(),planet1.get_mass(),planet1.get_volume())
#print(planet2.get_name(),planet2.get_distance(),planet2.get_density())
#print(f"Planet name: {planet1.get_name()}, Planet mass: {planet1.get_mass()} kg")
#print(planet1.get_name())
#planet1.set_name("Gornar")
#print(planet1.get_name())
print(planet1)
print(planet2)
class Dog:
    def _init__(self,_name,_breed,_age,_weight,_fur_color,_leg_count,_hunger_level):
        self.name = _name
        self.breed = _breed
        self.age = _age
        self.weight = _weight
        self.fur_color = _fur_color
        self.leg_count = _leg_count
        self.hunger_level = _hunger_level
    def can_dog_walk(leg_count):
        if leg_count >= 2:
            return True
    def will_bark(hunger_level):
        if hunger_level > 5:
            return True

