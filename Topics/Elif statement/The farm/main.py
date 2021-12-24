# https://hyperskill.org/learn/step/6534

stock = {'Sheep': 6769, 'Cow': 3848, 'Pig': 1296, 'Goat': 678, 'Chicken': 23}

money = int(input())
amount, message, pluralization = None, 'None', 's'

animals = stock.keys()

for animal in animals:
    price = stock[animal]
    if price <= money:
        amount = money // price
        message = f'{amount} {animal.lower()}'
        if animal != 'Sheep' and amount > 1:
            message += pluralization
        break

print(message)

# animals = {"Chicken": 23, "Goat": 678, "Pig": 1296, "Cow": 3848, "Sheep": 6769}
# money = int(input())
# buy = 'None'
# for animal, price in animals.items():
#     if price <= money:
#         try:
#             current = animals[buy]
#         except KeyError:
#             buy = animal
#         else:
#             if current < price:
#                 buy = animal
# try:
#     number = money // animals[buy]
# except KeyError:
#     print(buy)
# else:
#     text = f"{number} {buy.lower()}"
#     if number > 1 and buy != 'Sheep':
#         text += 's'
#     print(text)
