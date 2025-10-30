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

# print(planet1.get_name())

# Build a Star class that takes a  name as an argument 
# and has a getter, setter, and a string representation of the object. 
# Then, instantiate a star objectl

class Star:
    def __init__(self, _name):
        self.name = _name
    def get_name(self):
        return self.name
    def set_name(self,new_name):
        self.name = new_name
    def __str__(self):
        msg = ""
        msg += f"{self.get_name()} will explode in a few billion years."
        return msg
    
star1= Star("Sol")
print(star1.get_name())
print(star1.__str__())
print(star1)


