from PIL import Image, ImageDraw

image = Image.new('RGB', (600, 400), (0, 0, 255))
#  Рисуем примитивами: линия, прямоугольник (в т.ч. квадрат), овал (в т.ч. круг)

image.save('../images/blue_image.jpg')

RED = (255, 0, 0)
BLUE = (0, 0, 255)

draw = ImageDraw.Draw(image)
draw.line((0, 0, 600, 400), fill=(255, 0, 0), width=5)
image.save('../images/red_diagonal.jpg')
draw.line((600, 0, 0, 400), fill=RED, width=5)
draw.rectangle((30, 30, 590, 300), outline=RED, width=5)
draw.ellipse((50, 50, 370, 280), outline=RED, width=3)
draw.text((120, 120), 'вид из неразвитого окна', fill=BLUE, stroke_fill=RED, font_size=18)
# ДЗ найти для текста шрифт и его размер
# голубое небо, залитое синим, в углу солнце выглядывает жёлтое
# и текст "солнечный день"


# ПОЛИГОН - все точки кортежа соединённые линиями
POLY = (35, 75, 48)
draw.polygon(POLY, fill=RED, outline=BLUE, width=4)

image.save('../images/художество.jpg')