class Vector:
    def __init__(self,x,y):
        self.a = x
        self.b = y
        # Operator overloading methods:
        # __add__(self,other)
        #__sub__(self,other)
        #__mul__(self,other)
        #__eq__(self,other)
        # We need to overload the equality operator.

    def __eq__(self,other_vector):
        return (self.a == other_vector.a and self.b == other_vector.b)
    def __str__(self):
        return f"v = {self.a}x + {self.b}y."
    
vector1 = Vector(10,5)
vector2 = Vector(10,5)
print(vector1 == vector2)
print(vector1.__eq__(vector2))
print(vector1)






