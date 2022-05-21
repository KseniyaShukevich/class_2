count = int(input('Введите количество товаров: '))

data_tuples = []

for i in range(count):
    name = input('Введите название товара: ')
    price = input('Введите цену товара: ')
    count = input('Введите количетсво товара: ')
    unit = input('Введите единицу измерения: ')
    print('-' * 30)

    data_tuples.append(
        (i + 1, {'name': name, 'price': price, 'count': count, 'unit': unit})
    )

analytics = {
    'name': [],
    'price': [],
    'count': [],
    'unit': [],
}

for item in data_tuples:
    for key in analytics.keys():
        analytics[key].append(item[1][key])
        if key == 'unit':
            analytics[key] = list(set(analytics[key]))

print('Analytics:', analytics)
