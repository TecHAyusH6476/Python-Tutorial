class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Speaksss!!!!!"

    def breed(self):
        return "This is animal"

    # (Animal) -> Inheritance


class Cat(Animal):
    def speak(self):
        return self.name + " says meow!!"


class Dog(Animal):
    def a():
        return ""


my_dog = Dog(name="Bug")
my_cat = Cat(name="Bin")


print(my_dog.breed())
print(my_dog.speak())
