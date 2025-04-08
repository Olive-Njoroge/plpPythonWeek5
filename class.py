#Assignment 1
class Phone:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def phone_info(self):
        print(f"My phone is a {self.brand} {self.model} from {self.year}, and it does not overheat.")

# Create an instance of the class
my_phone = Phone("Tecno", "Spark 10C", 2023)

# Access attributes
print(my_phone.brand) 

# Call the method
my_phone.phone_info()

#inheritance
class Phone2(Phone):
    pass

new_phone = Phone2("Samsung", "Galaxy A14", 2024)
new_phone.phone_info()

#polymorphism

class Phone3:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def phone_info(self):
        print("Yaaay I have a phone🥳🥳🥳")

meAndMyPhone = Phone3("iphone", "13 pro", 2013)
meAndMyPhone.phone_info()

#Activity 2
# Parent class Animals
class Animals:
    def __init__(self, name, sound_type, move):
        self.name = name
        self.sound_type = sound_type  # Renamed attribute
        self.move = move

    def sound(self):
        return "yikes😬"  # Default sound

# Subclass Pig inheriting Animals
class Pig(Animals):
    def __init__(self, name, sound_type, move):
        super().__init__(name, sound_type, move)

    def sound(self):
        return "oink"

# Subclass Cow inheriting Animals
class Cow(Animals):
    def __init__(self, name, sound_type, move):
        super().__init__(name, sound_type, move)

    def sound(self):
        return "mooo"

# Create instances of Pig and Cow
pig1 = Pig("Mama", "oink", "run")
cow1 = Cow("Ibiza", "mooo", "walk")

# Loop through the animals and call sound() method
for animal in (pig1, cow1):
    print(f"{animal.name} says: {animal.sound()}") 



