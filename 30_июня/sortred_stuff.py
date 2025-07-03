# sorted - системный сортировщик, возвращает список
names_set = {'John', 'Paul', 'George'}
names_list = list(names_set)
names_list.sort()
print(*names_list, sep=', ')

# второй путь
names_set = {'John', 'Paul', 'George'}
names_list = sorted(names_set)
print(*names_list, sep=', ')

r = True
my_list = sorted(names_set, reverse=r)
print(my_list)
print(*my_list) # напечатать как множество элементов, без скобок

# enumerate() создаёт сопоставление индекса съ значением
dudes = ['John', 'Paul', 'George']
for i, v in enumerate(dudes): # блеск, автонумерация
    print(f'{i + 1}. {v}')
