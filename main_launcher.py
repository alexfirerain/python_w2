def print_goodbye(arg):
    print('Goodbye', end=' ')


def print_cruel(arg):
    print('cruel', end=' ')


def print_world(arg):
    print('world', end=' ')


def main():
    print_goodbye('')
    print_cruel('')
    print_world('')
    print()


main()

# оператор is -- когда два объекта это один и тот же

a = 1  # строки, кортежи, числа
print(id(a))
a += 1  # a is not a
print(id(a))

a = [0]  # списки, множества, словари - мутабельны
print(id(a))
a[0] += 1  # a is a
print(id(a))

my_refrigerator = ['колбаса', 'сыр', 'масло']
her_refrigerator = ['колбаса', 'сыр', 'масло']
print(my_refrigerator == her_refrigerator)  # true
print(id(my_refrigerator) == id(her_refrigerator))  # false

her_refrigerator = my_refrigerator

print(my_refrigerator == her_refrigerator)  # true
print(id(my_refrigerator) == id(her_refrigerator))  # true

my_refrigerator += ['мясо']
print(my_refrigerator)
print(her_refrigerator) # теперь это один и тот же
print(my_refrigerator is her_refrigerator)
print(my_refrigerator is her_refrigerator[:])

their_refrigerator = my_refrigerator[:] # эквивалентно my_refrigerator.copy()
temp = None
print(type(temp))
# if temp is None:    # так можно
# if temp == None:    # так нельзя
print(temp is None)
print(temp == None)   # хотя и работает, но так не надо
