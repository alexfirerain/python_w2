from PIL import Image

image = Image.open('../images/harry_python.jpg')
print(image.size)
x, y = image.size
mode = image.mode

print(f'Ширина = {x}, высота = {y}, схема = {mode}')
image.save('../images/HP_2.jpg')

pix_matrix = image.load()  # загружает собственно таблицу пикселей, само изображение
for i in range(x):
    for j in range(y):
        r, g, b = pix_matrix[i, j]
        pix_matrix[i, j] = g, r, b
image.save('../images/HP_perv.jpg')

# негатив
image = Image.open('../images/harry_python.jpg')
pix_matrix = image.load()
for i in range(x):
    for j in range(y):
        r, g, b = pix_matrix[i, j]
        pix_matrix[i, j] = 256 - r, 256 - g, 256 - b
image.save('../images/HP_neg.jpg')

# Greyscale
image = Image.open('../images/harry_python.jpg')
pix_matrix = image.load()
for i in range(x):
    for j in range(y):
        r, g, b = pix_matrix[i, j]
        average = (r +g + b) // 3
        pix_matrix[i, j] = average, average, average
image.save('../images/HP_grey.jpg')

image = Image.open('../images/harry_python.jpg')
pix_matrix = image.load()
image_rotated = image.rotate(180)
image_rotated.save('../images/HP_rotated.jpg')
image_flipped = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
image_flipped.save('../images/HP_mirrored.jpg')
cropped = image.crop((100, 200, 500, 450))
cropped.save('../images/HP_cropped.jpg')

# пропорции ресайза отслеживаем сами
resized = image.resize((400, 300))
resized.save('../images/HP_enlittled.jpg')

ratio = x // y # либо целочисленно, либо приводя к int, ибо библиотека растровая
