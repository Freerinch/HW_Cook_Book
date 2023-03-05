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

# pprint(cook_book, sort_dicts=False)

# Задание 2

def get_shop_list_by_dishes(dishes, person):
    total = dict()
    for dish in dishes:
        if dish in cook_book:
            for ing in cook_book[dish]:
                quan_list = dict()
                quan_list['pices'] = int(ing['pices']) * person
                if ing['name_of_ing'] not in total:
                    quan_list['measure'] = ing['measure']
                    total[ing['name_of_ing']] = quan_list
                else:
                    total[ing['name_of_ing']]['pices'] = total[ing['name_of_ing']]['pices'] + \
                                                         int(ing['pices']) * person
    return total


# pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))

# Задание 3

files = ['1.txt', '2.txt', '3.txt']
os.chdir('2.4.files/sorted')
massive = []

for file_name in files:
    with open(file_name) as f:
        file_data = f.readlines()
        file_data.insert(0, f'Количество строк {str(len(file_data))}\n')
        file_data.insert(0, f'\n Название файла: {file_name}\n')
        massive.append(file_data)

massive.sort(key=len)
with open('total_file.txt', 'a') as document:
    for text in massive:
        with open('total_file.txt', 'a') as document:
            document.writelines(text)