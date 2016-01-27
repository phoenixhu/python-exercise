# coding=utf-8

import Tkinter as tk

window = tk.Tk()

# 创建滚动条，最小值0,最大值100
slider = tk.Scale(window, from_=0, to=100)
slider.pack()
tk.mainloop()
