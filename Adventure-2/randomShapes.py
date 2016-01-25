# coding=utf-8
# 随即绘画

import turtle
import random
# 绘画
def drawShape(sides, length):
    angle = 360.0 / sides
    for side in range(sides):
        turtle.forward(length)
        turtle.right(angle)

# 移动到某处
def moveTurtle(x, y):
    # 抬笔
    turtle.penup()
    # 移动坐标
    turtle.goto(x, y)
    # 放笔
    turtle.pendown()

# 方形
def drawSquare(length):
    drawShape(4, length)

# 三角形    
def drawTriangle(length):
    drawShape(3, length)

# 圆形    
def drawCircle(length):
    drawShape(360, length)
    
def drawRandom():
    x = random.randrange(-200, 200) 
    y = random.randrange(-200, 200)
    length = random.randrange(75)
    shape = random.randrange(1, 4)
    
    moveTurtle(x, y)
    
    if shape == 1:
        drawSquare(length)
    elif shape == 2:
        drawTriangle(length)
    elif shape == 3:
        length = length % 4
        drawCircle(length)
        
for shape in range(100):
    drawRandom()
              
turtle.done()
