def get_summ(one, two, delimeter='&'):
    one = str(one)
    two = str(two)

    return one+delimeter+two


print(get_summ("Vlad","Bryuchko").upper())


def format_price (price):
    price = int(price)
    return str("Цена: {price} руб.".format(price=price))


a = format_price(56.24)
print(a)



phone_cost = {
    'city': 'Moscow', 'phone': ['Iphone X', 'S10', 'Iphone SE'], 'cost': [60000, 50000, 20000]
}

def price_phone(phone_cost['city'], phone_cost['phone'][0], phone_cost['cost'][0], discount = 30):
    phone_cost['cost'][0] = phone_cost['cost'][0] - discount/100
    return phone_cost['cost'][0]


print(def price_phone(phone_cost['city'], phone_cost['phone'][0], phone_cost['cost'][0], discount = 30))









