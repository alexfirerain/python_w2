# можно -> any, тогда может и не только число вернуть, а и строку тоже :)
def universal_action(*args, action: str = '+') -> float:
    match action:
        case '+':
            res = 0
            for arg in args:
                res += arg
        case '-':
            res = 0
            for arg in args:
                res -= arg
        case '*':
            res = 1
            for arg in args:
                res *= arg
        case '/':
            res = 1
            for arg in args:
                res /= arg
        case _:
            return 0
    return res


print(universal_action(3, 5, 7, action='+'))
print(universal_action(3, 5, 7, action='-'))
print(universal_action(3, 5, 7, action='*'))
print(universal_action(3, 5, 7, action='/'))
print(universal_action(3, action='+'))
print(universal_action(3, action='-'))
print(universal_action(3, action='*'))
print(universal_action(3, action='/'))
print(universal_action(8))
print(universal_action(8, 7))
print(universal_action(8, action='!'))


# print(universal_action(3, action='-'))
# print(universal_action(3, action='*'))
# print(universal_action(3, action='/'))

# САНДВИЧ
def sandwich(type_of_meat, with_onion=False, with_tomato=False):
    print("Булочка")
    if with_onion:
        print("Лучок")
    print(type_of_meat)
    if with_tomato:
        print("Помидорочка")
    print("Булочка")
    print()


sandwich("Свининка")
sandwich("Говядинка", True)
sandwich("Буженинка", with_tomato=True)
sandwich("Свининка", True, True)
