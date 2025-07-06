from PIL import Image, ImageDraw, ImageFont

sky = Image.new("RGB", (600, 400), color="aqua")
picture = ImageDraw.Draw(sky)

picture.ellipse((550, -50, 650, 50), fill="yellow")

font = ImageFont.truetype('../res/Times.TTF', 45)

picture.text((115, 170), "СОЛНЕЧНЫЙ ДЕНЬ", fill="yellow", font=font)
sky.save("../images/sunny_day.jpg")
