# `a` потому что array
# ВЛОЖЕННЫЕ СПИСКИ
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# такой список двумерный, это таблица
print(matrix)

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row][col], end='\t')
    print()

N = 3
# можно создать заготовку списка, инициализированного значением-заглушкой
matrix = [[1] * N for _ in range(N)]
print(matrix)

i = 1
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        matrix[row][col] = i
        i += 1
print(matrix)

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row][col], end='\t')
    print()

matrix = []
start = 1
N = 4
for i in range(N):
    table = []
    for j in range(start, start + N):
        table.append(j)
    matrix.append(list(table))
    start += N
print(matrix)

matrix = [[i + j for j in range(N)] for i in range(1, 10, N)]
print(matrix)
