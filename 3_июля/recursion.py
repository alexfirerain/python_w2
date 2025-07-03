# РЕКУРСИЯ, самовызов
# стек = определённый участок памяти, в котором храняться инструкции о возврате
# результатов вызванных методов.
# Используется метод LIFO
#
def factorial_naive(count):
    result = 1
    for i in range(2, count + 1):
        result *= i
    return result

print(factorial_naive(10))

for n in range(10):
    print(n, factorial_naive(n))

def factorial(x):
    if x == 1 or x == 0:
        return 1
    return x * factorial(abs(x) - 1)

print(factorial(7))
print(factorial(0))
print(factorial(1))
print(factorial(-1))
print(factorial(-5))
print(factorial(-6))
print(factorial(-7))

# базовый вариант = это когда дальше рекурсии ходу нет,
# т.е. который стопит лавину самовызовов
# обычно в первой же строке надо прописать его - условие выхода


#  https://sky.pro/media/poisk-vseh-vhozhdenij-podstroki-v-stroke-v-python


# обход бинарного дела иначе никак, ну и фрактал, и XOR
# а так вообще лучше без рекурсии!

