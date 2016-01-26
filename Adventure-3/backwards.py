# coding=utf-8

import Tkinter as tk

window = tk.Tk()

def changeString():
    # 获取文本框中的字符串
    stringToCopy = entry.get()
    # 将字符串反转
    stringToCopy = stringToCopy[::-1]
    # 将字符串从头到尾删除
    entry.delete(0, tk.END)
    
    # 把字符串插入到文本框位置0
    entry.insert(0, stringToCopy)

# 创建文本输入框
entry = tk.Entry(window)

# 创建按钮
button = tk.Button(window, text="Change", command=changeString) 

entry.pack()
button.pack()
window.mainloop()  
    