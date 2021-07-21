'''
小張要設計一款自動計算當日股票成交總額的一個小程式，請你幫他完成這個小程式(此題一次只會有一行資料)
說明:
輸入會有三個值，第一個值是星期幾，第二個值是股票的單價，第三個值是今日成交總量，每個值之間用一個空白隔開，
假設此股票在星期五、六、日是不開市的，所以如果是在這幾天，請回傳"不開市"
'''
# 方法一
in_txt = '星期一 99 1000'.split()
# in_txt = '星期六 100 10'.split()
# print(in_txt)

if in_txt[0] != '星期五' and  in_txt[0] != '星期六' and in_txt[0] != '星期日': print(int(in_txt[1]) * int(in_txt[2]))
else: print('不開市')

# 方法二
import sys
# in_txt = sys.stdin.read()
# in_list = in_txt.split()
in_list = in_txt
check_list = ['星期五', '星期六', '星期日']
if in_list[0] in check_list:
    print('不開市')
else:
    print(int(in_list[1]) * int(in_list[2]))