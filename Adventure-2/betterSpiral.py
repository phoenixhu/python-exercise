# coding=utf-8
# 螺旋形状
import turtle
import time
length = 0
angle = 90
while length < 200:
    turtle.forward(length)
    turtle.left(angle)
    length = length + 1
time.sleep(3)    