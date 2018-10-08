from pymonad import Just, List, Nothing, curry


@curry
def add(x, y):
    return x + y


def add10(x):
    return add * Just(10) & x


print(add10(List(1, 2, 3, 4, 5, 6)))
print(add10(Just(33)))
