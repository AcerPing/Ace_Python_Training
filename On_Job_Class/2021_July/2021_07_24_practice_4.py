'''
說明:
小時候一定玩過一個遊戲，從1~100內猜一個數字，如果沒猜到，下一個猜的人會從你所猜的數字得到新的範圍，從新的範圍開始猜

我們來隨機一個1~100數字當作獎品，開始我們的猜數字遊戲

提示:
使用random隨機數字
每次猜完後，要根據所猜的數字重新設定範圍
直到猜中為止
'''
import random

int_txt = random.randint(1,100)
x = 1 
y = 100 
while True:
    guess_number = int(input(f'請從{x}到{y}之間猜一數字'))
    if guess_number == int_txt: break
    if guess_number < int_txt and x < guess_number: x = guess_number
    elif guess_number > int_txt and y > guess_number: y =  guess_number
print(int_txt)