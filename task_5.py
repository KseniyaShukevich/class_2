rating = [5, 4, 3, 3, 2]

new_value = int(input('Введите натуральное число: '))

for counter, value in enumerate(rating):
    if counter == len(rating) - 1:
        rating.append(new_value)
        break

    if rating[counter] < new_value:
        rating.insert(counter, new_value)
        break

print('Результат:', rating)
