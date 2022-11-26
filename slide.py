from moviepy.editor import *
import os
from PIL import Image, ImageDraw,ImageFont



def creator(_text,_color_bg,_color_text,n):
    im = Image.new('RGB',(300,300), color=(_color_text))
    font = ImageFont.truetype('C:/Windows/Fonts/comic.ttf', size=18)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (50,150),
        _text,
        font = font,
        fill = (_color_bg)
        )
    im.save('C:/Мотивация кушать/new_pic'+str(n) +'.jpg')

text = ['Ты голоден?? \n Хочешь кушать?',
        'А с собой ничего нет?'
        'Ты считаешь себя тюбиком?',
        'Есть решение',
        'СДАЙ ЕГЭ',
        'тогда у тебя появятся деньги',
        'тачки',
        'а значит и еда',
        'либо просто сходи в ошку',
        'Хватит искать отмазки',
        'Возьми и сдай ЕГЭ']
color_bg = ['#0B5FA5','#FF4900','#67E300','#0099CC','#1142AA','#CC0000','#FE7300','#057C9E','#3813AF','#9EED00']
color_text = ['#000000']

for i in range(0,10):
    creator(text[i],color_text[0],color_bg[i],i)

directory = 'C:/Мотивация кушать'
files = os.listdir(directory)
images = list(filter(lambda x: x.endswith('.jpg'), files))
clips = [ImageClip(m).set_duration(2) for m in images]

final_clip = concatenate_videoclips(clips, method= 'compose')
final_clip.write_videofile('test2.mp4', fps=24)