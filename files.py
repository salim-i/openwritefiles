from pprint import pprint
from collections import Counter

cook_book = {}
dish_name_lst = []
dish_number = -1

with open('recipes.txt', encoding='utf8') as f:
    for line in f:
        dish_name_lst.append(line.lower().strip())
        counter = int(f.readline().strip())
        dish_number += 1
        ingredient_lst = []
        for ingredients in range(counter):
            ingredient_dic = {}
            ingredients = f.readline().lower().strip().split(' | ')
            ingredient_dic['ingredient_name'] = ingredients[0]
            ingredient_dic['quantity'] = int(ingredients[1])
            ingredient_dic['measure'] = ingredients[2]
            ingredient_lst.append(ingredient_dic)
            cook_book[dish_name_lst[dish_number]] = ingredient_lst
        f.readline()
    print('Задача № 1 ----------->')
    pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    dish_name = []
    shop_dic = {}
    for element in dishes:
        dish_name.append(element.lower())

    for dish in dish_name:
        for inger in cook_book[dish]:
            c = Counter(dish_name)[dish]
            shop_dic[inger['ingredient_name']] = {'quantity': inger['quantity'] * c * person_count,
                                                  'measure': inger['measure']}

    print('Задача № 2 ----------->')
    pprint(shop_dic)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
