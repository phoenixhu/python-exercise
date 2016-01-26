# coding=utf-8

import Tkinter as tk

window = tk.Tk()

def changeString():
    # 获取文本框中的字符串
    stringToCopy = entry.get()
    # 把字符串插入到文本框位置0
    entry.insert(0, stringToCopy)

# 创建文本输入框
entry = tk.Entry(window)

# 创建按钮
button = tk.Button(window, text="Change", command=changeString) 

entry.pack()
button.pack()
window.mainloop()  
    