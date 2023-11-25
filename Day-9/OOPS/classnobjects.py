# Class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(self.name, " says woof!")


# Create a object/instance
obj = Dog(name="Atom", age=3)

print(obj.name, " is ", obj.age, "yrs old")
obj.bark()


# Constructor
# instance vars
# self
