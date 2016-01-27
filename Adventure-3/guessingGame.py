# coding=utf-8
import random
import Tkinter as tk

window = tk.Tk()

maxNo = 10
score = 0
rounds = 0

# 按钮响应函数
def buttonClick():
    # 声明修改全局变量
    global score
    global rounds
    
    # 执行try语句块的代码并捕获异常
    try:
        # 获取文本框内容并转化为整型
        guess = int(guessBox.get())
        # 如果数字大于0小于或等于maxNo变量，判断成立
        if 0 < guess <= maxNo:
            # 随机生成1-10之间的数字
            result = random.randrange(1, maxNo + 1)
            # 如果文本框得到的值等于随机生成的数字
            if guess == result:
                # 将score变量值+1
                score = score + 1
            # 将rounds值+1
            rounds = rounds + 1
        # 判断不成立，提示输入无效
        else:
            result = "Entry not valid"
    # 处理异常，如果try语句块中的代码执行出错，执行 except语句块的代码    
    except:
        result = "Entry not valid"
    
    # 添加第一个标签控件的文本内容
    resultLabel.config(text=result)
    # 添加第二个标签控件的文本内容
    scoreLabel.config(text=str(score) + "/" + str(rounds)) 
    # 将文本框内容从头到尾清空
    guessBox.delete(0, tk.END)

# 创建标签，输入1-10的数字
guessLabel = tk.Label(window, text="Enter a number from 1 to" + str(maxNo))
# 创建文本框
guessBox = tk.Entry(window)
# 创建标签
resultLabel = tk.Label(window)
# 创建标签
scoreLabel = tk.Label(window)
# 创建按钮
button = tk.Button(window, text="guess", command=buttonClick)

# 显示控件
guessLabel.pack()
guessBox.pack()
resultLabel.pack()
scoreLabel.pack()
button.pack()

# 主循环
tk.mainloop() 
      