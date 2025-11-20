# 9 and 10

class Playlist:
    def __init__(self,name = "New Playlist", songs = []):
        self.name = name
        self.songs = songs

    def add_song(self,song_to_add):
        self.songs.append(str(song_to_add))
    
    def __add__(self,other): # Overload the + operation such that
        # we can now add playlists together
        combined_name = self.name + "+" + other.name
        combined_song = self.songs + other.songs
        return Playlist(combined_name,combined_song)
    
    def __str__(self):
        return f"{self.songs}"
        

playlist1 = Playlist("X",["Song A","Song B"])
playlist1.add_song("Song D")
playlist2 = Playlist("Y", ["Song C"])
combined = playlist1 + playlist2
#playlist1.__add__(playlist2)
print(combined)




class ShoppingCart:
    def __init__(self,_items={}):
        self.items = _items
        
    def add_item(self,item_to_add):
        if item_to_add in self.items:
            self.items[item_to_add] += 1
        else:
            self.items[item_to_add] = 1


    def __add__(self,other):
        combined = ShoppingCart()
        # Also check if item preexisting in other cart
        for item,quantity in self.items.items(): # for key,value in {}.keys 
            combined.items[item] = quantity
        for item,quantity in other.items.items():
            if item in combined.items:
                combined.items[item] += quantity
            else:
                combined.items[item] = quantity
        return combined
            


    def __str__(self):
        return f"{self.items}"

p1 = ShoppingCart({"tea":1,"Energy Drink":2})
p2 = ShoppingCart({"Energy Drink":3,"hat":1})
p1.add_item("clock")
print(p1)
print(p2)
combined = p1+p2
print(combined)


