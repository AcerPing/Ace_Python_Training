'''
起始條件，第一個數字為0，第二個數字為1，後面的數字為前面兩個數字的相加
0 1 1 2 3 5 8 13 21 …

說明:
輸入唯一個數字i，請試試看印出指定數字的(以人類的索引直)第i個數字是多少
'''

int_txt = '10'

a = 0
b = 1

int_list = [a, b]
while len(int_list) <= int(int_txt):
    c = int_list[-1] + int_list[-2]
    int_list.append(c)
# print(int_list)
print(int_list[int(int_txt)-1])