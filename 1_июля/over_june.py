# как вычистить например знаки из текста:

punctuations = (',',
                '.',
                '?',
                '!',
                ':',
                ';')
text = "длинный текст, наполненный: запятыми, точками, вопросами! и что?"
print(text)
for z in punctuations:
    text = text.replace(z, '')
print(text)

# списочные выражения, list comprehension
squares = []
for i in range(10):
    squares.append(i ** 2)
print(*squares, sep=', ')

squares_comprehension = [i ** 2 for i in range(10)]  # то же самое! ↑
print(*squares_comprehension, sep=', ')

# итак: список = [что как]

# список квадратов чётных:
quadrates_of_evens = [i ** 2 for i in range(10) if i % 2 == 0]

print(*quadrates_of_evens)

# произведение ай и джей
print([i * j for i in range(3) for j in range(3)])

for i in range(3):
    for j in range(3):
        print(i * j, end=' ')
print()

n = '500 600 700 800'
print([int(i) for i in n.split()])

N = '100 200 300 400 500 600 700 800 900'
approved = [500, 600]
a = [int(i) for i in n.split() if int(i) in approved]
print(a)

# список, берущий каждое третье слово
string = 'Списочные выражения применяются для эффективности кода и'
filtered = [w for w in string.split() if (string.split().index(w) + 1) % 3 == 0 ]
res = [a for a in string.split()[2::3]]
print(filtered)
print(res)

# если это без [], это получается просто выражение, 