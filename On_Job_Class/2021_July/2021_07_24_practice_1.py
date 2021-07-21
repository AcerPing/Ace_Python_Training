'''
說明:
請使用while迴圈，印出指定數字的跌代加總。
例如題目是5
必須輸出從1開始加到5的答案15
1+2+3+4+5=15
'''

in_txt = int('10')

r = 1
sum = 0
while r <= in_txt:
    sum = sum + r
    r = r+1

print(sum)