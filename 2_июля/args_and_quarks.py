# kwargs = фактически "словарь кейвордов"
def print_some(*args, **kwargs):
    for i in args:
        print(i)
    for k, v in kwargs.items():
        print(k, '=', v)


print_some(1, 2, name='Mariska')
print_some("John", "Lennon", city='Liverpool', age=27)


def profile(name, surname, city, *children, **miscellaneous):
    print(f'Имя: {name}')
    print(f'Фамилия: {surname}')
    print(f'Из города: {city}')
    if children:
        print(f'Дети: {', '.join(children)}')
    if "Хобби" in miscellaneous:
        print("Увлечения: ", miscellaneous["Хобби"])
    print('Хобби', end=': ')
    print(miscellaneous)


profile("Дима", "Колесов", "Сталинград",
        "Мария", "Ксения", "Артур", Хобби="грэпплинг")
