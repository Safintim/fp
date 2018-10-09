from pymonad import curry, State, unit, Nothing

user = {'items': [], 'money': 1000}


@curry
def buy_item(item, user):
    items = {
        'apples': 70,
        'milk': 80,
        'wine': 300,
        'chips': 100
    }

    @State
    def state_computation(money):
        if items.get(item):
            if money - items[item] >= 0:
                user['items'].append(item)
                # user['money'] = money - items[item]
                return [user, money - items[item]]
            else:
                return [user, money]
    return state_computation


buy = unit(State, user) >> buy_item('wine') >> buy_item('wine') >> buy_item('wine') >> buy_item('wine') >> buy_item('chips')
print(buy(user['money']))
