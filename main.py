import os
from pprint import pprint

current = os.getcwd()
folder = '2.4.files'
file = 'recipes.txt'
full_path = os.path.join(current, folder, file)

with open(full_path) as file:
    cook_book = dict()
    ingridients = list()
    for line in file:
        dish_name = line.strip()
        dishes_count = int(file.readline())
        for _ in range(dishes_count):
            ing = file.readline().strip()
            name_of_ing, pices, measure = ing.split(' | ')
            ingridients.append(
                {'name_of_ing': name_of_ing,
                 'pices': pices,
                 'measure': measure})
        cook_book[dish_name] = ingridients
        file.readline()
pprint(cook_book,sort_dicts=False)

# def get_shop_list_by_dishes(dishes, person_count):
#     ingr_list = dict()
#
#     for dish_name in dishes:
#         if dish_name in cook_book:
#             for ings in cook_book[dish_name]:
#                 quantity_list = dict()
#                 if ings['name_of_ing'] not in ingr_list:
#                     quantity_list['measure'] = ings['measure']
#                     quantity_list['pices'] = ings['pices'] * person_count
#                     ingr_list[ings['ingredient_name']] = quantity_list
#                 else:
#                     ingr_list[ings['name_of_ing']]['quantity'] = ingr_list[ings['name_of_ing']]['pices'] + \
#                                                                  ings['pices'] * person_count
#
#         else:
#             print(f'\n"Такого блюда нет в списке!"\n')
#     return ingr_list
# # print(get_shop_list_by_dishes('Оливье',2))
#
# pprint(cook_book,sort_dicts=False)
