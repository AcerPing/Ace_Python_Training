'''
請使用while迴圈，印出指定數乘法表
說明:
輸入為兩個數字(x,y)，每個數字以一個空白隔開，請印出此 x×y 乘法表
'''
in_txt = '3 4'
in_list = in_txt.split()
# print(in_list)
x,y = 1,1

while x <= int(in_list[0]):
    while y <= int(in_list[1]):
        print(f'{x}x{y}={x*y}')
        y += 1
    x += 1
    y = 1