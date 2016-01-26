# coding=utf-8
import Tkinter as tk
window = tk.Tk()

def checkPassword():
    # 密码为Oranges
    password = "Oranges"
    # 获取密码输入框中的密码
    enteredPassword = passwordEntry.get()
    
    # 如果密码正确，显示其结果
    if password == enteredPassword:
        confirmLabel.config(text="Correct")
    # 如果不正确，显示其结果
    else:
        confirmLabel.config(text="Incorrect")
        
# 创建标签控件
passwordLabel = tk.Label(window, text="Password：")

# 创建密码输入框，使用*隐藏字符串
passwordEntry = tk.Entry(window, show="*")   

# 创建按钮
button = tk.Button(window, text="Enter", command=checkPassword)

# 创建标签控件，用来显示密码结果
confirmLabel = tk.Label(window) 

# 显示相关控件
passwordLabel.pack()
passwordEntry.pack()
button.pack()
confirmLabel.pack()

# 主循环
window.mainloop()