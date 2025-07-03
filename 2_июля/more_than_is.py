def print_array(array: [], start: int = None):
    if start is None:
        start = 0
    print(array[start:])


def print_array_o(array: [], start: int = None):
    print(array[start if start is not None else 0:])


a = [1, 2, 3]

print_array(a)
print_array(a, 1)

print_array_o(a)
print_array_o(a, 1)


# мышление программиста - это понимать язык машины


def coordinates() -> tuple:
    return 5.4, 3.2  # здесь и такое бывает! "множественный возврат"


x, y = coordinates()  # такие функции умеют возвращать как бы сразу несколько :)
print(f'x = {x}, y = {y}')

# если мы не знаем точно, но их, скажем, больше двух
x, y, *z = coordinates()  # остатки сливаются под звёздочку
print(f'x = {x}, y = {y}, z = {z}')  # x = 5.4, y = 3.2, z = []


# поэтому называют "рест":
# x, y, *rest = coordinates()

def coordinates_more():
    return 5.4, 7.8, 3.14, 8, 73


x, y, *rest = coordinates_more()
print(f'x = {x}, y = {y}, z = {rest}')  # x = 5.4, y = 7.8, z = [3.14, 8, 73]
# звёздочка при распаковке только в одной переменной! и не обязательно в первой

x, *y, rest = coordinates_more()
print(f'x = {x}, y = {y}, z = {rest}')

*x, y, rest = coordinates_more()
print(f'x = {x}, y = {y}, z = {rest}')

# x, y, z = coordinates_more() # вылетает ошибка! ̶ ▌♪

bender = 'Остап Сулейман Бендер'
*names, surname = bender.split()
print(names, surname)
print(*bender)


# функция с переменным числом аргументов
def multy(*args):
    print(len(args))  # ноль
    print(args)  # пустой кортеж, можем обратиться по индексу, либо по итератору (в смысле в цикле)
    if args is None:
        return -1
    res = 1
    for arg in args:
        res *= arg
    return res if args else 0


multy()
print(multy(1, 2, 3, 4))
print(multy())


# метод утёнка - это рассказ резиновому утёнку

# проверку допустимых значений аргумента как правило делаем сами

def semimultiple(first, *args):  # первый позиционный
    # если поменять местами параметры (переменные аргументы на первом месте),
    # последний (остальные) должен быть именованным
    result = first
    # if not args:
    #     return first
    for arg in args:
        result *= arg
    return result


print(semimultiple(2, 3, 4))
print(semimultiple(2))
print(semimultiple(0))


def fio(name, surname):
    return f'{name} {surname}'


print(fio("Остап", "Бендер"))
print(fio(surname="Бендер", name="Остап"))  # именованые рулят


