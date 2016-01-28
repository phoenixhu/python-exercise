# coding=utf-8

import pygame

# 初始化pygame
pygame.init()

# 设置窗口大小
windowSize = [400, 300]
screen = pygame.display.set_mode(windowSize)

# 设置窗口标题
pygame.display.set_caption("Circles")

# 设置颜色
colour = pygame.color.Color('#FFFFFF')

done = False
# 如果为True开始循环，直至为False
while not done:
    # 画出一个圆形
    pygame.draw.circle(screen, colour, [200, 150], 50)
    # 更新窗口
    pygame.display.flip()
    
    # 循环所有事件
    for event in pygame.event.get():
        # 如果有事件尝试关闭窗口，done为True，while循环结束
        if event.type == pygame.QUIT:
            done = True

# 退出游戏            
pygame.quit()            