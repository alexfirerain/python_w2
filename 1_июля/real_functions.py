# функция это то, что берёт, обрабатывает и возвращает данные
# чистые функции -- похожи на математические:
#   ♥ детерминирована только аргументами
#   ♥ не оказывает стороннего эффекта
#   https://ru.hexlet.io/courses/python-functions/lessons/pure-functions/theory_unit
#
#
#

def square(num):
    temp = num ** 2
    return temp


t = square(5)


def even_odd(num):
    if num % 2 == 0:
        return "чёт"
    else:
        return "нечет"


# однако это не лучший варик
def even_odd(num):
    if num % 2 == 0:
        return "чёт"
    return "нечет"


def even_odd(num):
    return "чёт" if num % 2 == 0 else "нечет"


def print_string(s=None):
    if s is None:
        return  # пример выпрыга
    print(s)

"""
Д/З
выводить число словами, т.е. 356 → "триста пятьдесят шесть"
до максимум трёхзначного.
написать функцию.

"""