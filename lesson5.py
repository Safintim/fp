from pymonad import Just, List, Nothing, curry


begin = lambda: Just([0, 0])


to_left = lambda num: lambda left_or_right: (
    Nothing
    if abs((left_or_right[0] + num) - left_or_right[1]) > 4
    else Just([left_or_right[0] + num, left_or_right[1]])
)


to_right = lambda num: lambda left_or_right: (
    Nothing
    if abs((left_or_right[1] + num) - left_or_right[0]) > 4
    else Just([left_or_right[0], left_or_right[1] + num])
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
