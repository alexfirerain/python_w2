# обычное дело для словарей -- частотный анализ
text = """
Каникулы! Само слово, слово "каникулы", звучит как музыка, как обещание свободы и приключений. 
Каникулы – это время, когда можно забыть про будильник, забыть про уроки, забыть про всё, 
что связано со школой. Каникулы – это время для себя, для друзей, для семьи.

Эти каникулы, эти долгожданные каникулы, я планирую провести незабываемо. Я мечтаю о море, 
о тёплом море, о ласковом море, где можно плавать, плавать и плавать, пока пальцы не сморщатся. 
Я мечтаю о солнце, о ярком солнце, о жарком солнце, которое будет согревать меня своими лучами. 
Я мечтаю о песке, о мягком песке, о белом песке, на котором можно строить замки, замки, замки, 
которые смоет волна.

Но даже если море, море, море останется только в мечтах, каникулы всё равно будут прекрасны. 
Ведь каникулы – это время для новых открытий, для новых увлечений, для новых знакомств. 
Можно читать, читать, читать книги, которые давно пылились на полке. Можно рисовать, рисовать, 
рисовать картины, вдохновлённые летним солнцем. Можно гулять, гулять, гулять по парку, 
наслаждаясь свежим воздухом.

Главное, чтобы каникулы, каникулы, каникулы были наполнены радостью, смехом и позитивными 
эмоциями. Главное, чтобы после каникул, после этих замечательных каникул, остались только 
приятные воспоминания, воспоминания, воспоминания, которые будут согревать нас долгими 
зимними вечерами.

Так пусть же каникулы, каникулы, каникулы будут самыми лучшими! Пусть они принесут много 
счастья, много радости, много незабываемых моментов! Ура каникулам! Ура! Ура! Ура!
"""

punctuations = {',', '.', '!', '–', '"'}
for z in punctuations:
    text = text.replace(z, '')

words = sorted(text.lower().split())

dic = {}

for word in words:
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] = dic[word] + 1

for word, frequency in dic.items():
    print(word, '→', frequency)

qwerty = dic.items()
print(dir(qwerty))
