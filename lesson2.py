from pymonad import curry


# 2.3.1
@curry
def concatenation(x, y):
    return x + y


hello_arg = concatenation('Hello, ')

print(hello_arg('Sergey'))


# 2.3.1
@curry
def greeting_func(greeting, mark1, mark2, name):
    return greeting + mark1 + name + mark2


greeting = greeting_func('Hello', ', ', '!')
print(greeting('Petya'))
