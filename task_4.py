string = input('Введите слова, разделенные одним пробелом: ').strip()

words = string.split()

for counter, word in enumerate(words):
    print(counter + 1, word[:10])
