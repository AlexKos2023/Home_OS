
import os
import pprint


if not os.path.isdir(r".\OS_1"):
    os.mkdir(r".\OS_1")
    new_file = open (r".\OS_1\test_folder.txt", "w", encoding="utf-8")
    new_file.write(input("Введите список рецептов: "))
else:
    with open(r".\OS_1\test_folder.txt", "w", encoding="utf-8") as f:
        f.write(input("Введите список рецептов: "))

cook_book = {}
with open (r".\OS_1\test_folder.txt", "r", encoding="utf-8") as f:
    data = f.read()
    sp_list = data.split("\n\n")
    for i in sp_list:
        sp_dish = i.split("\n")
        for i in range(2, len(sp_dish)):
            value_out = sp_dish[i].split(" | ")
            value = {}
            value['ingredient_name'] = value_out[0]
            value['quantity'] = value_out[1]
            value['measure'] = value_out[2]
            if sp_dish[0] in cook_book:
                cook_book[sp_dish[0]].append(value)
            else:
                cook_book[sp_dish[0]] = [value]
print("Книга рецептов:")             
pprint.pprint(cook_book)
              


def get_shop_list_by_dishes(dishes : list, person_count : int):
    answer = {}
    #all_dict = []
    for i in range (0, len(dishes)):
        c_b = cook_book[dishes[i]]
        #all_dict.append(c_b)
        for i in range (0, len(c_b)):
            value = {}
            new_key = c_b[i]['ingredient_name']
            new_weight = int(c_b[i]['quantity']) * person_count
            new_union = c_b[i]['measure']
            value['measure'] = new_union
            value['quantity'] = new_weight
            if new_key in answer:
                answer[new_key].append(value)
            else:
                answer[new_key] = value
    print("Результат:")            
    pprint.pprint(answer)
           

pprint.pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

order = {}
os.chdir(r".\OS_1")
#print("Все папки и файлы:", os.listdir())
for x in os.listdir():
    if (x == "1.txt" or x == "2.txt" or x == "3.txt") and x.endswith(".txt"):
        #print(x)
        with open(x, "r", encoding="utf-8") as f:
            text = f.read()
        with open(x, "r", encoding="utf-8") as f:
            key = len(f.readlines())
            if key in order:
                order[key].append(text)
            else:
                order[key] = text    
        with open(r".\new_text.txt", "w", encoding="utf-8") as f:
            for key, value in sorted(order.items()):
                f.write(f'{x}\n{key}\n {value}\n')     



     

        















