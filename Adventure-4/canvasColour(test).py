# coding=utf-8
# 输入颜色十六进制值变换颜色

import Tkinter as tk

window = tk.Tk()
def colours():
    label.config(text="") 
    try:
        colour = entry.get()
        entry.delete(0, tk.END)
        canvas.config(bg=colour)  
    except:
        label.config(text="请输入正确的值")
canvas = tk.Canvas(window, height=300, width=300)
label = tk.Label(window)
entry = tk.Entry(window)
button = tk.Button(window, text="变换颜色", command=colours)
canvas.pack()
label.pack()
entry.pack()
button.pack()
window.mainloop()