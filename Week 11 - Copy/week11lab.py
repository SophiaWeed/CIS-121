#12. (a) Write a class for a TVShow with the below instance variables and methods.
#The TVShow object should have the ability to be passed both initial values.
#You may pick anything you like for the string representation of the object.
#A TVShow has a genre and can be added to a dashboard.
#As part of your class, write a method called preview, that displays the show information.
#Hint: for this method, you should print the title and genre of the show.


import math
class TVShow:
    def __init__(self, show_title, show_genre):
        self.title = show_title
        self.genre = show_genre
    def get_title(self):
        return self.title
    def get_genre(self):
        return self.genre
    def set_title(self, new_title):
        self.title = new_title
    def set_genre(self,new_genre):
        self.genre = new_genre
    def preview(self):
        print(f"{self.get_title()}: A {self.get_genre()}.")
    def __str__(self):
        return f"Hello, you're watching a show called {self.get_title()}."
    
class NetflixDashboard:
    def __init__(self, profile_name = "Unknown"):
        self.profile = profile_name
        self.shows: TVShow = [] # This method is called explicit typing. It tells Python
        # that the list consists exclusively of type TVShow.
    def add_show(self, show_to_add : TVShow): # also defines the type: explicit typing
        self.shows.append(show_to_add)
    def display_recommendations(self):
        for show in self.shows:
            print(show) # Prints the __str__ of the TVShow class method

show1 = TVShow("Charlotte's Web","Fantasy")
show2 = TVShow("Good Omens", "Action")
dash1 = NetflixDashboard("Sophia")
dash1.add_show(show1)
dash1.display_recommendations()


# Write a class for a Point with the instance variables and methods listed below.
# A point in the coordinate plane has an x and y coordinate. Points can be compared, and the distance
# between two points can be calculated using the distance formu

class Point:
    def __init__(self,_x,_y):
        self.x = _x
        self.y = _y
    def __eq__(self, point2):
        return self.x == point2.x and self.y == point2.y
    def get_distance(self, other_point):
        return math.sqrt((self.x - other_point.x)**2+(self.y - other_point.y)**2)
    
p1 = Point(3,2)
p2 = Point(3,2)
print(p1.__eq__(p2))  #method overriding
print(p1.get_distance(p2))




