class Dog:
    def __init__(self, _name, _age, _weight, _height, _color, _playfulness, _tricks, _species="unknown",):
        self.name =_name
        self.species = _species
        self.age = _age
        self.weight = _weight
        self.height = _height
        self.color = _color
        self.playfulness = _playfulness
        self.tricks = _tricks

    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name
    def get_species(self):
        return self.species
    def set_species(self,new_species):
        self.species = new_species
    def get_age(self):
        return self.age
    def set_age(self,new_age):
        self.age = new_age
    def get_weight(self):
        return self.weight
    def set_weight(self,new_weight):
        self.weight = new_weight
    def get_height(self):
        return self.height
    def set_height(self,new_height):
        self.height = new_height
    def get_color(self):
        return self.color
    def set_color(self, new_color):
        self.color = new_color
    def get_playfulness(self):
        return self.playfulness
    def set_playfulness(self, new_playfulness):
        self.playfulness = new_playfulness
    def get_tricks(self):
        return self.tricks
    def speak(self):
        # Small dogs yip, med dogs bark, large dogs woof
        if self.height == 1:
            print("Yip")
        elif self.height == 2:
            print("Bark")
        else:
            print("Woof")

    
class DogPark:
    def __init__(self, _name):
        self.name = _name
        self.dogs = []  # A list of dogs in the park. Currently empty.
    def add_dog(self,dog):
        self.dogs.append(dog)
    def show_dogs(self):
        for dog in self.dogs:
            print(dog.get_name())
    def change_dog_name(self,old_name,new_name):
        for dog in self.dogs:
            if dog.get_name() == old_name:
                dog.set_name(new_name)
    def find_dog(self,dog_name): # Which dog am I trying to make bark?
        for dog in self.dogs:
            if dog.get_name() == dog_name:
                dog.speak()
    def call_dog(self,dog_name):
        # Remove a dog from the park
        for dog in self.dogs:
            if dog.get_name() == dog_name:
                self.dogs.remove(dog)





dog1 = Dog("Spoot",2,4,1,"Blue",5,"Fetch","Yorkie")
dog2 = Dog("Rover", 6, 5,3,"Pink",18,"Cry","Mastiff")
park1 = DogPark("Barkzone")
park1.add_dog(dog1)
park1.add_dog(dog2)
park1.show_dogs()
park1.change_dog_name("Spoot","Spot")
park1.show_dogs()
park1.find_dog("Rover")
park1.find_dog("Spot")
park1.show_dogs()
park1.call_dog("Rover")
print("-")
park1.show_dogs()


