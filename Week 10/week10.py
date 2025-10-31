# import math
# class Planet:
#     def __init__(self,_name,_radius, _mass, _distance): # the constructor always needs to reference itself! 
#         # We want it to be able to pass in a name and also assign itself a name
#         self.name = _name
#         self.radius = _radius
#         self.mass = _mass
#         self.distance = _distance
#     def get_name(self):
#         return self.name
#     def get_radius(self):
#         return self.radius
#     def get_mass(self):
#         return self.mass
#     def get_distance(self):
#         return self.distance
#     def get_volume(self):
#         volume = 4/3 * math.pi * self.radius ** 3
#         return volume
#     def get_density(self):
#         density = self.mass / self.get_volume() # What is the difference between a function and a method?
#         return density
#     def set_name(self,new_name): # We need to assign the new name. Frequently we do not return information, we just change it.
#         self.name = new_name
#     def __str__(self):
#         msg = ""
#         msg += f"hello {self.get_name()}, how are you?"
#         return msg

# planet1 = Planet("x25",4,5,6)
# planet2 = Planet("z37",7,8,9)

# # print(planet1.get_name())

# # Build a Star class that takes a  name as an argument 
# # and has a getter, setter, and a string representation of the object. 
# # Then, instantiate a star objectl

# class Star:
#     def __init__(self, _name,_mass):
#         self.name = _name
#         self.masss = _mass
#     def get_name(self):
#         return self.name
#     def get_mass(self):
#         return self.mass
#     def set_name(self,new_name):
#         self.name = new_name
#     def set_mass(self,new_mass):
#         self.mass = new_mass
#     def __str__(self):
#         msg = ""
#         msg += f"{self.get_name()} will explode in a few billion years."
#         return msg
    
# # star1= Star("Sol")
# # print(star1.get_name())
# # print(star1.__str__())
# # print(star1)

# # Let's make a planetary system class with 
# # a central star as an argument, the ability to add planets, and the ability to display the planets.


# class PlanetarySystem:
#     def __init__(self, _star):    # Here is our planetary system's constructor.
#         self.star = _star
#         self.planets = [] # Now we need a data structure that can hold these objects. A list does the job.

#     def add_planet(self,_planet):
#         self.planets.append(_planet)
#     def show_planets(self):
#         for planet in self.planets:
#             print(planet.get_name())

# sun = Star("Sun")
# ss = PlanetarySystem(sun)

# # Let's add a planet or two to the solar system "ss".
# p = Planet("Mercury", 1,2,3)
# ss.add_planet(p)
# p = Planet("Venus",4,5,6)
# ss.add_planet(p)
# p = Planet("Earth",7,8,9)
# ss.add_planet(p)
# ss.show_planets()


# Let's cause the planets to Orbit. I also want to draw them so I'll use Turtle Graphics
# I need to gove the planets a color and a Velocity in the X and Y direction.


class Plant:
    def __init__(self,_name,_height_in_inches):
        self.name = _name
        self.height = _height_in_inches
    def get_name(self):
        return self.name
    def set_height(self,new_height):
        self.height = new_height
    def get_height(self):
        return f"{self.height} inches"
    def __str__(self):
        msg = ""
        msg = f"{self.get_name()} grows in the sunshine."
        return msg

plant1 = Plant("Jose",3)

print(plant1.__str__())
print(plant1.get_height())
plant1.set_height(2)
print(plant1.get_height())


