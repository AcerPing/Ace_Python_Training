# -*- coding: utf-8 -*-

import sys

# cd .\On_Job_Class\2021_July\ # D:\Python_Summarize\Python_Training\On_Job_Class\2021_July
sys.stdin.reconfigure(encoding='utf-8')
# print(sys.stdin.read()) # 標準輸入法
str1 = sys.stdin.read()

# os.chdir(r'D:\Python_Summarize\Python_Training\On_Job_Class\2021_July')
# # with open('in.txt',mode='r',encoding='utf-8') as file:
# #     str1 = file.read()

print(str1)

# str1 = '3 張三 李四 老五'
str_list = str1.split()
print(str_list)
people_num = int(str_list[0])
print(people_num)
# 答案
print(str_list[people_num])
