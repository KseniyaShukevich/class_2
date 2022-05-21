user_string = input('Введите значения, разделяя одним пробелом: ')

new_list = user_string.split()

for i in range(0, len(new_list), 2):
    if i + 1 < len(new_list):
        new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]

print('Результат:', new_list)
