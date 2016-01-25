# coding=utf-8
# 多形状
import turtle

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
        
drawShape(4, 10)
moveTurtle(60, 30)
drawShape(3, 20)
#moveTurtle(-100, 60)
#drawShape(5, 100)
#drawShape(10, 100)

moveTurtle(-100, 20)
drawSquare(30)
moveTurtle(- 10, 20)
drawCircle(1)
drawCircle(2)
moveTurtle(75, -75)
drawSquare(60)

turtle.done()
