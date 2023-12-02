class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Speaksss!!!!!"

    def breed(self):
        return "This is animal"

    # (Animal) -> Inheritance


# Inheritance - parent class ( properties and functions)
class Cat(Animal):
    def speak(self):
        return self.name + " says meow!!"


class Dog(Animal):
    def a():
        return ""


my_dog = Dog(name="Bug")
my_cat = Cat(name="Bin")


print(my_cat.breed())
print(my_cat.speak())
