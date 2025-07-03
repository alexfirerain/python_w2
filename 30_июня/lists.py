# Списки

s = ['3', '4', '5']
lst = list(range(1, 2, 3))  # range генерирует итерируемую последовательность
lst = []  # один способ
lst = list()  # второй способ
lst = list('слово')
print(lst)
lst = [1, 2, 3] * 3  # повторяет!
print(lst)
print(type(lst))
lst = [1] * 10
lst = [1, 2, 3]
print(lst[1:])
# список мутабелен!
"""
['append', 'clear', 'copy', 'count', 'extend', 'index',
 'insert', 'pop', 'remove', 'reverse', 'sort']
"""
sob = 'сабака'
lst = list(sob)
lst[1] = 'о'
print(lst)

# координаты индекса должны быть в рамках массива
s.clear()
for i in range(11):
    s.append(i)
print(s)

s1 = [1, 2, 3]
s2 = [4, 5, 6]
s = s1.extend(s2) # второй добавился в первый
print(s) # None! ибо .extend() пустой метод
s = s1 + s2
s += [4] # конкатенируем только однородное!
s[0] = 'числа'
print(s)

order = list(range(10))
print(order)
for item in range(0, len(order), 2):
    print(order[item], "-", order[item] ** 2)

slicer = order[:len(lst):2]
print(slicer)
sli2 = order[2::2]
print(slicer)

del lst[2]
print[lst]

del lst[::2] # удалится каждый второй

lst.sort(reverse=True)