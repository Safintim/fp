from pymonad import Just, List, Nothing, curry


begin = lambda: Just([0, 0])

to_left = lambda num: lambda functor: (
    Nothing
    if abs((functor[0] + num) - functor[1]) > 4
    else Just([functor[0] + num, functor[1]])
)

to_right = lambda num: lambda functor: (
    Nothing
    if abs((functor[1] + num) - functor[0]) > 4
    else Just([functor[0], functor[1] + num])
)

get_value = lambda maybe: (
    print('упал')
    if maybe == Nothing
    else print('Еще стоит')
)

banana = Nothing

get_value(begin() >> to_left(2) >> to_right(5) >> to_left(-2))
get_value(begin() >> to_left(2) >> to_right(5) >> to_left(-1))
get_value(begin() >> to_left(2) >> banana >> to_right(5) >> to_left(-1))