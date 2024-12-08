class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def call(self, number):
        print(f"Calling {number} from {self.model}...")
    
    def display_details(self):
        print(f"Smartphone Details:\nBrand: {self.brand}\nModel: {self.model}\nPrice: ${self.price}")

class Smartwatch(Smartphone):
    def __init__(self, brand, model, price, battery_life):
        super().__init__(brand, model, price)  # Reuse attributes from the parent class
        self.battery_life = battery_life  # Unique attribute for Smartwatch
    
    def track_activity(self):
        print(f"Tracking activity on the {self.model} smartwatch...")
    
    def display_details(self):
        super().display_details()  # Extend functionality from the parent class
        print(f"Battery Life: {self.battery_life} hours")


# Creating instances
phone = Smartphone("Apple", "iPhone 15", 999)
watch = Smartwatch("Apple", "Apple Watch Series 9", 499, 18)

# Test methods
phone.display_details()
phone.call("123-456-7890")

watch.display_details()
watch.track_activity()



# polymorphism
class Animal:
    def move(self):
        pass  # This method will be overridden by subclasses

class Dog(Animal):
    def move(self):
        print("The dog is running 🐕.")

class Fish(Animal):
    def move(self):
        print("The fish is swimming 🐟.")

class Bird(Animal):
    def move(self):
        print("The bird is flying 🦅.")

# Polymorphism in action
animals = [Dog(), Fish(), Bird()]

for animal in animals:
    animal.move()
