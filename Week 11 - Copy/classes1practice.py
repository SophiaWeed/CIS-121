# Create a product class with a name, a price, and a quantity. Initialize all these arguments and 
# create getter and setter methods for each. Create an instance variable

class Product:
    def __init__(self,_name,_price,_quantity=0):
        self.name = _name
        self.price = _price
        self.quantity = _quantity

    def get_name(self):
        return self.name
    def set_name(self,new_name):
        self.name = new_name
    def get_price(self):
        return self.price
    def set_price(self,new_price):
        self.price = new_price
    def get_quantity(self):
        return self.quantity
    def __str__(self):
        return f"You have {self.quantity} {self.name}(s) at a price of ${self.price} each."
    
#apple = Product("Honeycrisp Apple",0.5,83)
#print(apple)

# Create a Book class with a title, an author, and a page count. Initialize these with getters and setters and create an instance.

class Book:
    def __init__(self,_title,_author,_page_count):
        self.title = _title
        self.author = _author
        self.page_count = _page_count
    def get_title(self):
        return self.title
    def set_title(self,new_title):
        self.title = new_title
    def get_author(self):
        return self.author
    def set_author(self, new_author):
        self.author = new_author
    def get_page_count(self):
        return self.page_count
    def set_page_count(self,new_count):
        self.page_count = new_count
    def __str__(self):
        return f"Your book is {self.title} by {self.author} and has {self.page_count} pages total."
    
#book1 = Book("Charlotte's Web","E.B. White", 598)
#print(book1)

# Create an employee class with a name,a title, and a salary. Write getters and setters and 
# give them the ability to make a greeting and request a 6% raise.

class Employee:
    def __init__(self,_name,_title,_salary):
        self.name = _name
        self.title = _title
        self.salary = _salary
    def get_name(self):
        return self.name
    def get_title(self):
        return self.title
    def get_salary(self):
        return self.salary
    def set_name(self,new_name):
        self.name = new_name
    def set_title(self,new_title):
        self.title = new_title
    def set_salary(self,new_salary):
        self.salary = new_salary
    def give_greeting(self):
        return f"Hello. My name is {self.get_name()} and I'm the {self.get_title()}."
    def request_raise(self):
        return f"I'm currently making ${self.get_salary()}. I'd like a new salary of ${self.get_salary() + (self.get_salary() * 0.06)}"
    
employee1 = Employee("Sheryl","CEO",5)
print(employee1.give_greeting())
print(employee1.request_raise())




