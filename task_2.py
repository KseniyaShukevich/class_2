userString = input('Введите значения, разделяя одним пробелом: ')

newList = userString.split()

for i in range(0, len(newList), 2):
    if i + 1 < len(newList):
        newList[i], newList[i + 1] = newList[i + 1], newList[i]

print('Результат:', newList)
