# coding=utf-8
"""
将number.txt文件写入到excel表中
"""
# 导入excel写入模块
import xlwt
# 导入正则表达式模块
import re

class excel(object):
    def __init__(self):
        # 新建excel文件
        self.workbook = xlwt.Workbook(encoding = "ascii")
        # 新建工作表
        self.worksheet = self.workbook.add_sheet('My Worksheet')
    
    def open_file(self, filename):
        # 可读模式打开txt文件
        self.f = open(filename, 'r')
        # 读取文件
        self.r = self.f.read()
        # 将文件转换为列表
        self.list = re.split(r'[\W]*', self.r)
    
    def write_excel(self):
        for i in range(len(self.list)):
            #循环写入文件
            self.worksheet.write(i, 0, label = self.list[i])
        # 保存文件
        self.workbook.save("Excel_Workbook.xls")

myobject = excel()
myobject.open_file("numbers.txt")
myobject.write_excel()