# coding=utf-8
import xlwt
workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('My Worksheet')
worksheet.write(0, 0, label = 'Row 0, Column 0 Value')
worksheet.write(1, 0, label = 'huping')
workbook.save('Excel_Workbook.xls')