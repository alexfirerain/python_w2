# анонимные функции (однострочники, безымянные)
# лямбда-функции
# lambda <аргументы>: <выражение>
# проверка коллекции: any(), all()
# вернули ИСТИНА все или хотя бы какой-то элемент коллекции


# функция критерия отбора элементов
#
# def is_first_letter_a(word):
#     return word[0] == 'a'

is_first_letter_a = lambda word: word[0] == 'a'

string_contains_an = lambda string: "ан" in string

fruits = ["арбуз", "ананас", "банан", "авокадо", "киви"]

print(list(filter(is_first_letter_a, fruits)))

print(list(filter(string_contains_an, fruits)))

print(list(filter(lambda s: "ан" in s, fruits)))

# в одну строку напечатать список квадратов чисел от 3 до 15

print(list(map(lambda n: n ** 2, range(3, 16))))

# списочным выражением:
print([n ** 2 for n in range(3, 16)])

words = "В этом списке останутся только данные слова длиннее шести букв".split()

long_words = [word for word in words if len(word) > 6]
print(long_words)

ENG_ABC = set(chr(ch) for ch in range(ord('a'), ord('z') + 1))
print(ENG_ABC)
RUS_ABC = set([chr(ch) for ch in range(ord('а'), ord('е') + 1)] + ['ё'] +
              [chr(ch) for ch in range(ord('ж'), ord('я') + 1)])
print(RUS_ABC)

ENG_ABC_CAP = set(map(lambda l: l.upper(), list(ENG_ABC)))
RUS_ABC_CAP = set(map(lambda l: l.upper(), list(RUS_ABC)))

ABC_alt = (set(ENG_ABC) ^ set(RUS_ABC) ^
           set([x.upper() for x in ENG_ABC]) ^
           set([x.upper() for x in RUS_ABC]))

print(ENG_ABC_CAP)
print(RUS_ABC_CAP)
ABC = ENG_ABC ^ RUS_ABC ^ ENG_ABC_CAP ^ RUS_ABC_CAP  # и так мы получили полный набор двух азбук!
print(ABC)

# вот как например отфильтровать знаки из текста
text = ('Это такая долгая, капец долгая история: сначала вышел, потом купил, потом вкусил'
        '- и что? А вот! Смотри: что хотел, и что получилось...')
text = ''.join(filter(lambda x: x in ABC ^ {' '}, text.lower()))
print(text)


def remove_punctuation(txt):
    ENG_ABC = set(chr(ch) for ch in range(ord('a'), ord('z') + 1))
    RUS_ABC = set([chr(ch) for ch in range(ord('а'), ord('е') + 1)] + ['ё'] +
                  [chr(ch) for ch in range(ord('ж'), ord('я') + 1)])

    return ''.join(filter(lambda x: x in ABC ^ {' '}, txt.lower()))


print(remove_punctuation(text))


def purified_list(txt):
    return remove_punctuation(txt).split()


print(purified_list(text))


def long_words(text, length=4):
    return [word for word in text if len(word) >= length]


def long_words_lambda(text, length=4):
    return list(filter(lambda w: len(w) >= 4, text))


print(long_words(purified_list(text)))
print(long_words_lambda(purified_list(text)))

text = ('Я знаю, что я ничего не знаю, но другие не знают и этого,'
        ' а значит, я знаю больше, чем другие.')

words = purified_list(text)
print(words)

# считаем частоту слов
d = {}
for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

for k, v in d.items():
    print(f'{k} = {v}')

# ключ сортировки

print(fruits.sort())  # не работает
# надо так
fruits.sort()
print(fruits)
# или так:
print(sorted(fruits))

# внимание:
print(sorted(fruits, key=lambda ch: ch[1]))
print(sorted(fruits, key=lambda w: len(w), reverse=True))

res = {k: v for k, v in sorted(d.items(),
                               key=lambda item: item[1], reverse=True)}
for k, v in d.items():
    print(f'{k} = {v}')

print(all([1, 2, 3]))  # возвращает ИСТИНА, ибо все элементы != 0
print(any([1, 2, 3]))  # возвращает ИСТИНА, ибо не все элементы != 0
print(any([1, 2, 0]))  # возвращает ИСТИНА, ибо хотя бы один != 0
print(any([-1]))
print(any([0]))  #
print(any([]))

words = 'один два три'.split()
print('что-то из "один два три" длиннее трёх букв?')
print(any(list(map(lambda w: len(w) > 3, words))))
print('все из "один два три" длиннее трёх букв?')
print(all(list(map(lambda w: len(w) > 3, words))))
