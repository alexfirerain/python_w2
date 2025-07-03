# Питон для детей и родителей
# черепашья графика
# подбиблиотека какой-то нормальной библиотеки
# она бежит по песку и оставляет след,
# чтоб не следила, нужно её перенести
import turtle as t

# смотри чтоб не заимпортировать самого себя)) Питон не вкурит

t.speed(20)
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange', 'teal']
# t.bgcolor('black')
angle = 360 / len(colors) - 1

# turtle.forward(50) # сколько пикселей вперёд пройти
# turtle.right(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(50)
# turtle.right(90)

def plot_square(edge_length):
    for i in range(4):
        t.forward(edge_length)
        t.left(90)


def plot_polygon(edges, edge_length):
    for i in range(edges):
        t.forward(edge_length)
        t.left(360 / edges)


plot_square(50)
plot_polygon(5, 50)
plot_polygon(36, 5)

t.penup()
t.goto(100, 200)
t.pendown()


# N = 8
# for _ in range(N):
#     t.circle(50)
#     t.right(360 // N)
#
# for _ in range(N):
#     plot_square(100)
#     t.right(360 // N)
#


def plot_squared_polygon(edge, angles):
    for _ in range(angles):
        plot_square(edge)
        t.right(360 / angles)


def plot_circle_petal_flower(radius, petals):
    for _ in range(petals):
        t.circle(radius)
        t.left(360 / petals)


plot_squared_polygon(30, 7)

t.penup()
t.goto(-100, - 50)
t.pendown()

# plot_circle_petal_flower(40, 7)
# plot_circle_petal_flower(80, 9)

for x in range(200):
    t.pencolor(colors[x % len(colors)])
    t.width(x // 100 + 1)
    t.forward(x)
    t.right(angle)

def tree(length):
    if length <10:
        return
    t.forward(length)
    t.left(30)
    tree(length * 0.618)
    t.right(60)
    tree(length * 0.618)
    t.left(30)
    t.backward(length)


t.left(90)
tree(20)

t.mainloop()

# Д/З завтра будет модуль Ран-Дом
# задание картинкой в группе