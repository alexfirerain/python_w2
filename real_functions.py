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
