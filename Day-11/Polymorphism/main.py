class Bird:
    def fly(self):
        pass


class Sparrow(Bird):
    def fly(self):
        return "Sparrow can fly..."


class Penguin(Bird):
    def fly(self):
        return "Penguin cannot fly..."


def describe_flight(a):
    return a.fly()


sparrow = Sparrow()
pen = Penguin()
# object - pen and sparrow

print(describe_flight(sparrow))
print(describe_flight(pen))
