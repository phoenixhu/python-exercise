# coding=utf-8
# 输入颜色十六进制值变换颜色

import Tkinter as tk

window = tk.Tk()
colour = "#FF0000"
canvas = tk.Canvas(window, height=300, width=300, bg=colour)

canvas.pack()

window.mainloop()