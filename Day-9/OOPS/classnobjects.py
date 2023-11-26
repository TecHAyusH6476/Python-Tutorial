# Class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(self.name, " says woof!")


# Create a object/instance  -> calls __init__
obj1 = Dog(name="Atom1", age=3)
obj2 = Dog(name="Atom2", age=2)

# obj props -> name and age
#     behaviour -> bark function

print(obj1.name, " is ", obj1.age, "yrs old")
obj1.bark()

obj2.bark()

# Constructor
# instance vars
# self
