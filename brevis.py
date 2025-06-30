# СОЗДАНИЕ АББРЕВИАТУР

word = input('Введите словосочетание для сокращения: ').strip()
abbr = ''
for i in range(len(word)):
    if i == 0 or (word[i - 1] == ' ' and word[i] != ' '):
        abbr += word[i].capitalize()
print(abbr)

# lst = []
# while (word := input('input word: ').strip()) != '':
#     lst.append(word[0].upper())
#
# print('we got: ', end=': ')
# print(*lst[:10], sep='')

# КОРТЕЖ такой же список, но немутабельный
# если что-то константно, то лучше кортежем
# выигрыш и памяти, и времени
BLACK = (0, 0, 0)
empty = ()
empty = tuple
str = "наш ковёр зелёная поляна"
carpet = tuple(str) + ('.',)  # "мутирует" по типу строки
# следовательно бывают цепочки вызовов
print(carpet)
one = (1,)  # без запятой не кортеж!

"""
['count', 'index']
вот и все методы, зато позволяет менять местами переменные и сравнивать,
можем сложные структуры создавать (вложенный список больше памяти взял бы) 
"""
cards = [(7, '♦'), (8, '♥')]
print((1, 2) >= (2, 1))  # сравнивает элементы по очереди
print((5, 2) >= (1, 2, 3))

channels = ['red', 'green', 'blue']
r, g, b = channels  # это РАСПАКОВКА кортежа
print(r, g, b)  # главное чтоб количество совпадало слева и справа
# если не равняется, то ошибка
print(channels)
r, *g = channels  # неполная распаковка! остаток идёт в *последний
h, *channels = channels  # и даже так
print(channels)

a, b = input(), input()
print(a, b)

a, b, c = 1, 2, 3
a, b = [1, 2], 3

# students = [('Petrov', 3.6), ('Ivanov', 3.9), ('Sidorov', 4.0)]
# print(students)
N = 5
students = []
for _ in range(N):
    student, average = input('ФИО: '), float(input('бал: '))
    students.append((student, average))

print(students)

for st in students:
    student, average = st
    print('Студент: ', student)
    print("Средний бал: ", average)

