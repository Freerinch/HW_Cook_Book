import os
from pprint import pprint
#Задание 1
current = os.getcwd()
folder = '2.4.files'
file = 'recipes.txt'
full_path = os.path.join(current, folder, file)

with open(full_path) as file:
    cook_book = dict()

    for line in file:
        dish_name = line.strip()
        dishes_count = int(file.readline())
        ingridients = list()
        for _ in range(dishes_count):
            ing = file.readline().strip()
            name_of_ing, pices, measure = ing.split(' | ')
            ingridients.append(
                {'name_of_ing': name_of_ing,
                 'pices': pices,
                 'measure': measure})
        cook_book[dish_name] = ingridients
        file.readline()


# {get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }
# Задание 2

def get_shop_list_by_dishes(dishes, person):
    total = dict()
    for dish in dishes:
        if dish in cook_book:
            for ing in cook_book[dish_name]:
                quan_list = dict()
                if ing['name_of_ing'] not in total:
                    quan_list['measure'] = ing['measure']
                    quan_list['pices'] = ing['pices'] * person
                    total[ing['name_of_ing']] = quan_list
                else:
                    total[ing['name_of_ing']]['pices'] = total[ing['name_of_ing']]['pices'] + \
                                                         ing['pices'] * person
    return total

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


