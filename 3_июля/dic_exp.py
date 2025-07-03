# словарные выражения!

numbers = list(range(1, 6))
squares_dummy = {
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}

squares_smart = {n: n ** 2 for n in numbers}

print(squares_smart)
print(squares_smart == squares_dummy)

# квадраты чётных чисел от 0 до 10
new_dic = {n: n ** 2 for n in range(1, 11) if n % 2 == 0}
print(new_dic)

source_dict = {
    'x': 1,
    'y': 2,
    'z': 3,     # можно оставлять тут запятую
}

dest_dic = {k : v * 2 for k, v in source_dict.items()}
print(dest_dic)

