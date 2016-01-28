# coding=utf-8

import Tkinter as tk

window = tk.Tk()

def sliderUpdate(Source):
    # 获取RGB滚动条的位置
    red = redSlider.get()
    green = greenSlider.get()
    blue = blueSlider.get()
    
    # 将RGB的位置格式化为十六进制
    colour = "#%02x%02x%02x" % (red, green, blue)
    # 填充画布颜色
    canvas.config(bg=colour)
    # 将文本框内容清空
    hexText.delete(0, tk.END)
    hexText.insert(0, colour)
    
# 创建滚动条
redSlider = tk.Scale(window, from_=0, to=255, command=sliderUpdate)
greenSlider = tk.Scale(window, from_=0, to=255, command=sliderUpdate)
blueSlider = tk.Scale(window, from_=0, to=255, command=sliderUpdate)

# 创建画布
canvas = tk.Canvas(window, width=200, height=200)

hexText = tk.Entry()

# 删格显示控件
redSlider.grid(row=1, column=1)
greenSlider.grid(row=1, column=2)
blueSlider.grid(row=1, column=3)
canvas.grid(row=2, column=1, columnspan=3)
hexText.grid(row=3, column=1, columnspan=3)

# 叠加显示控件，不推荐使用
"""
redSlider.pack()
greenSlider.pack()
blueSlider.pack()
canvas.pack()
"""
tk.mainloop()