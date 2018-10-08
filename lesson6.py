from pymonad import curry, State, unit

user = {'items': [], 'money': 1000}

items = {
    'apples': 70,
    'milk': 80,
    'wine': 300,
    'chips': 100
}


@curry
def buy_item(item, user):
    @State
    def state_computation(money):
        if items.get(item):
            user['items'].append(item)
            if money - items[item] >= 0:
                user['money'] = money - items[item]
                return [user, money - items[item]]
            else:
                print('Не хватает мани')
                return [user, money]
    return state_computation


buy = unit(State, user) >> buy_item('wine') >> buy_item('wine') >> buy_item('wine') >> buy_item('wine')
print(buy(user['money']))



# @curry
# def buy_item(item_in_store, items):
#     @State
#     def state_computation(money):
#         if items.get(item_in_store):
#             if money - items[item_in_store] >= 0:
#                 return [items, money - items[item_in_store]]
#             else:
#                 return 'не хватает'
#         return [items, money]
#
#     return state_computation
#
#
# buy = unit(State, items) >> buy_item('') >> buy_item('wine') >> buy_item('wine') >> buy_item('wine') >> buy_item('chips')
# print(buy(user['money']))



