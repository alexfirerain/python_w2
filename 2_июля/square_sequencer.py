nums = list(range(1, 10))
print(nums)


def square(num):
    return num ** 2


print(''.join(map(str, map(square, nums))))


### вхождение подстроки
# в частности "ан"

def contains_an(string, exp):
    return exp in string

string_contains_an = lambda string : "ан" in string


print(contains_an("банан", "ан"))
fruits = ["арбуз", "ананас", "банан", "авокадо", "киви"]
a_fruits = list(filter(string_contains_an, fruits))
print(a_fruits)