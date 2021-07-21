'''
今天要設計一款能夠自動對獎的大樂透對獎程式，請試著想想看該如何完成!
假設此樂透只可以選5個號碼，號碼介於1~20，只有再對中三個號碼以上時才算中獎，
對中三個號碼即可得獎金100元，4個號碼獎金1000元，5個號碼獎金10000元

說明:
輸入會有兩"組"值，每組值之間用一個","隔開，每一組值內含有5個數值，每個數值內以一個空白隔開，
第一組值為玩家選擇的號碼，第二組值為開獎的號碼，請回傳最後獎金多少元，如果沒中獎即為0元
'''
in_txt = '1 3 5 10 11,2 4 5 10 11'.split(',') # 輸入資料根據','，使用split切開
# print(in_txt)
my_lotto = in_txt[0].split() # 玩家選擇的號碼 # 把切開後的第一組根據空白使用split切開
result_lotto = in_txt[1].split() # 開獎的號碼 # 把切開後的第二組根據空白使用split切開
# print(result_lotto)

win_lotto = 0 # 中幾個號碼 #設定一個計數變數，以利後續判斷對中幾個數字，初始值為0
for number in my_lotto:
    if number in result_lotto: win_lotto += 1
# print(win_lotto)
if win_lotto >= 3:
    if win_lotto >= 5: print('獎金10000元')
    elif win_lotto >= 4: print('獎金1000元')
    else: print('獎金100元')
else: print('獎金0元')
