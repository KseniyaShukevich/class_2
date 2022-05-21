number_of_month = int(input(''))

seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {0: 'Зима', 1: 'Весна', 2: 'Лето', 3: 'Осень'}

season_by_list = None
season_by_dict = None

if number_of_month == 12:
    season_by_list = seasons_list[0]
    season_by_dict = seasons_dict.get[0]
    print('Пора года(list):', season_by_list)
    print('Пора года(dict):', season_by_dict)
elif number_of_month > 0 and number_of_month // 3 < len(seasons_list):
    season_by_list = seasons_list[number_of_month // 3]
    season_by_dict = seasons_dict.get(number_of_month // 3)
    print('Пора года(list):', season_by_list)
    print('Пора года(dict):', season_by_dict)
else:
    print('Нет такого месяца')
