Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from turtle import *
lt(90)
for i in range(7):
    forward(300)
    right(120)
pu()
for x in range (11):
    for y in range(11):
        goto(x*30, y*30)
        dot(5)
done()
