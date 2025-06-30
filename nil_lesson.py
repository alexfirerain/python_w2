#
# # неправильно!
# s = set()
# res = s.add('x')
# print(res) # 'None'
#
# s = 'смотреть'
# if s.startswith('смо'):
#     print('это смо')
#
# if s.endswith('еть'):
#     print('это еть')
#
# ss = 'Смотреть, вертеть, видеть'
#
# index = s.find('еть') # даёт индекс первого вхождения
# print(index)
#
# index = s.find('w') # если нет, вернёт -1
# print(index)
#
# """
# 1. find('подстрока') -> индекс первого вхождения
# 2. find('подстрока', start) -> индекс первого вхождения после старта
# 3. find('подстрока', start, end) -> индекс первого вхождения после старта,
#                                     но не далее финиша
# """
# print(ss.find('еть', 6))

word = 'синхрофазотрон'
# сколько букв "о" и на каких позициях
positions = set()
start = 0
while start < len(word):
    index = word.find('о', start)
    if index != -1:
        positions.add(index)
        start = index + 1
    else:
        break
print(f'В слове {word} буква "о" встречается {len(positions)} раз на индексах: {positions}')





