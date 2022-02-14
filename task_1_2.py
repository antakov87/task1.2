from pprint import pprint


def create_cook_book():
    with open('recipes.txt', encoding='UTF-8') as f:
        cook_book = {}
        for line in f:
            line_ = line.strip()
            cook_book[line_] = []
            count = int(f.readline().strip())
            for ingredient in range(count):
                ing_name = f.readline().strip().split(' | ')
                dict_ = {'ингредиент': ing_name[0], 'колличество': ing_name[1], 'мера': ing_name[2]}
                cook_book[line_].append(dict_)
            f.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    list_ ={}
    for dish in dishes:
        for ing in create_cook_book()[dish]:
            name_ing = ing["ингредиент"]
            if name_ing not in list_:
                list_[name_ing] = {"колличество": int(ing["колличество"]) * person_count, "мера": ing["мера"]}
            else:
                list_[name_ing]["количество"] += int(ing["количество"]) * person_count
    return list_


pprint(create_cook_book())
print()
pprint(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 5))
