# coding=utf-8
# 随机句子生成器

import Tkinter as tk
import random

window = tk.Tk()

# 从列表中随机选择单词
def randomNoun():
    nouns = ["cats", "hippos", "cakes"]
    noun = random.choice(nouns)
    return noun

# 从列表中随机选择动词
def randomVerb():
    verbs = ["eats", "likes", "hates", "has"]
    verb = random.choice(verbs)
    return verb

# 按钮响应函数
def buttonClick():
    # 获取文本框内容
    name = nameEntry.get()
    # 随机生成动词
    verb = randomVerb()
    # 随机生成单词
    noun = randomNoun()
    # 将获取到的文本框内容和随机生成的动词单词组合
    sentence = name + " " + verb + " " + noun
    # 将生成内容文本框的字符串从头到尾删除
    result.delete(0, tk.END)
    # 将组合的内容插入到生成内容文本框中
    result.insert(0, sentence)

# 创建标签    
nameLabel = tk.Label(window, text="Name：")
# 创建文本框，输入Name
nameEntry = tk.Entry(window)
# 创建按钮
button = tk.Button(window, text="Generate", command=buttonClick)
# 创建文本框，用来显示生成内容
result = tk.Entry(window)

# 显示控件
nameLabel.pack()
nameEntry.pack()
button.pack()
result.pack()

#主循环 
window.mainloop()