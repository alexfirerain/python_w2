nums = list(range(1, 10))
print(nums)


def square(num):
    return num ** 2


print(''.join(map(str, map(square, nums))))
