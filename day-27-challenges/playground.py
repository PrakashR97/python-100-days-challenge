def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5, 6))


def calculate(**kwargs):
    print(kwargs)


calculate(add=3, muliply=5)


class Cars:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")

car = Cars(model="BMW")
print(car.model)
