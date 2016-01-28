# coding=utf-8
# 点击速度的游戏

import Tkinter as tk
import time

window = tk.Tk()

# 记录点击按钮的次数
clicks = 0
# 记录开始点击时间
start = 0 
# 完成游戏所点击的次数
goal = 100

def buttonClick():
    global clicks
    global start
    
    # 如果没有开始点击
    if clicks == 0:
        # 记录开始时间
        start = time.time()
        # 按钮次数+1
        clicks = clicks + 1
    
    # 如果点击的次数大于或等于100,计算点击所花费的时间，并显示到标签上，最后将记录重置为0
    elif clicks + 1 >= goal:
        score = time.time() - start
        label.config(text="Time: " + str(score))
        clicks = 0
    # 如果点击的次数大于0,将点击的次数+1并更新滚动条的值
    else:
        clicks = clicks + 1
        slider.set(clicks)    

button = tk.Button(window, text="Click me", command=buttonClick)
slider = tk.Scale(window, from_=0, to=goal)
label = tk.Label(window)

button.pack()
slider.pack()
label.pack()
window.mainloop()
