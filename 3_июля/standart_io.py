# механизм, позволяющий просто вводить-вводить-вводить строки,
# а на ввод их отправить только всё вместе в нужный момент
# sys.stdin
# такой же итератор range(), но он движется только вперёд и выдаёт
# только строки ввода юзера
import sys

# for line in sys.stdin:
#     print(line)
# есть метод строки readline

# data = sys.stdin.readlines()
#
# print(data)
# spltd = (''.join(data)).split('\n')
# print(spltd)
# data = '-'.join(sorted(
#     spltd
# ))
# print(data)

datas = [d.strip('\n') for d in sys.stdin.readlines()]
# string = '-'.join(
#     sorted(list(
#         filter(lambda w: len(w) > 3, datas))
#     )
# )
# print(string)

# ТЗ: "гори-ёлочка"

temp = []  # как список кортежей: индекс строки в ДАТАС и число слов в строке
for i, s in enumerate(datas):
    temp.append((i, len(s.split()),))   #

print(temp)
temp.sort(key=lambda x: x[1])
print(temp)

index = temp[0][0]


res = sorted(datas[index].split())
print(*res, sep='-')


