# попробуем сделать ключ сортировки
fruits = ["арбуз", "ананас", "банан", "авокадо", "киви"]

print(sorted(fruits, key=lambda s: s[-1]))
# лексиграфическая сортировка по умолчанию для текстов

# кортежем определим последовательность сортираторов:
print(sorted(fruits, key=lambda s: (len(s), s[-1])))

goods = [
    ["утюг", 1500],
    ["фен", 1000],
    ["праща", 800],
]

print(sorted(goods))
print(sorted(goods, key=lambda g: g[1]))

goods_store = [
    ["утюг", 1500, 5],
    ["фен", 1000, 12],
    ["праща", 800, 15],
]
print(sorted(goods_store, key=lambda g: (g[1], g[2], g[0])))

# Д/З сделать сортировку по одному критерию возрастающе, затем по другому убывающе
# stackoverflow.com/questions/70314727/how-can-i-sort-a-list-by-the-second-item-descending-and-first-one-ascending
# веб-приложение, группы товаров, сортировка, просмотром и т.д.
