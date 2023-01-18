# ЗАДАНИЕ 1
with open('cookbook.txt', 'rt') as f:
    cook_book = {}
    for line in f:
        recipe_name = line.strip()
        ingredients_count = int(f.readline())
        ingredients = []
        for i in range(ingredients_count):
            ing = f.readline().strip()
            ingredient_name, quantity, measure = ing.split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        f.readline()
        cook_book[recipe_name] = ingredients

print(cook_book)

# ЗАДАНИЕ НОМЕР 2

dinner = ['Омлет', 'Фахитос']


def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    for x in dishes:
        dish = cook_book.get(x)
        for el in dish:
            measure_quantity = {}
            ingredient = el.get('ingredient_name')
            if ingredient in res.keys():
                new_quantity = int(el.get('quantity')) * person_count
                old_quantity = res.get(ingredient).get('quantity')
                total_quantity = new_quantity + old_quantity
                measure_quantity['measure'] = el.get('measure')
                measure_quantity['quantity'] = total_quantity
            else:
                measure_quantity['measure'] = el.get('measure')
                measure_quantity['quantity'] = int(el.get('quantity')) * person_count
            res[ingredient] = measure_quantity
    return res


print(get_shop_list_by_dishes(dinner, 2))

# ЗАДАНИЕ НОМЕР 3

files = {}
counter = 1
for i in range(3):
    with open(f'{counter}.txt') as f:
        files[f'{counter}.txt'] = len(f.readlines())
    counter += 1

sorted_values = sorted(files.values())
print(sorted_values)
new_files = {}
for i in sorted_values:
    for x in files.keys():
        if files[x] == i:
            new_files[x] = i

print(new_files)
with open('result.txt', 'w') as f:
    for file in new_files:
        f.write(str(file))
        f.write('\n')
        f.write(str(new_files[file]))
        f.write('\n')
        with open(file, 'r') as fil:
            f.write(fil.read())
            f.write('\n')



















