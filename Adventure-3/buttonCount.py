# coding=utf-8
# 点击计数

# 导入Tkinter模块，将其重命名为tk
import Tkinter as tk

# 创建窗口
window = tk.Tk()

# 记录按钮点击的次数
count = 0
# 按钮点击调用此函数
def buttonClick():
    # 声明修改全局变量
    global count
    # 改变变量数值
    count = count + 1
    # 按钮点击后改变按钮的文字
    button.config(text=str(count))
    
# 创建按钮，参数依次为位置（window窗口），按钮文字，点击响应（点击按钮调用buttonClick函数）
button = tk.Button(window, text="Click me!", command=buttonClick)

# 计算按钮的大小和位置，并在窗口中显示按钮
button.pack()

# 主循环
window.mainloop()