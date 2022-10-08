Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from turtle import *
lt(90)
def fr(w):
    if w >= 1:
        pensize(w)
        fd(w * 10)
        rt(30)
        fr(w * 0.75)
        lt(60)
        fr(w * 0.75)
        rt(30)
        bk(w * 10)
        pensize(w)
speed(10)
hideturtle()
penup()
goto(0, -200)
pendown()
fr(10)
