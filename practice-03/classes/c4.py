class Car:
    wheels = 4  # class variable

    def __init__(self, brand):
        self.brand = brand  # instance variable

c1 = Car("Toyota")
print(c1.brand)
print(c1.wheels)
