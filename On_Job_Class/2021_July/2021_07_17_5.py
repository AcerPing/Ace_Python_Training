'''
今天要設計一款能夠自動判斷身分證是否合法的程式，身分證的判斷是有既定的公式的，公式如下:
<身分證公式>
戶籍代表字母
A台北市　B台中市　C基隆市　D台南市　E高雄市　F台北縣
G宜蘭縣　H桃園縣　I 嘉義市　J新竹縣　K苗栗縣　L台中縣
M南投縣　N彰化縣　O新竹市　P雲林縣　Q嘉義縣　R台南縣
S高雄縣　T屏東縣　U花蓮縣　V台東縣　W金門縣　X澎湖縣
Y陽明山　Z連江縣

英文字母代表的數字
A=10 B=11 C=12 D=13 E=14 F=15 G=16 H=17 I=34 J=18 K=19 L=20
M=21 N=22 O=35 P=23 Q=24 R=25 S=26 T=27 U=28 V=29 W=32 X=30
Y=31 Z=33

性別代表數字
1：男性
2：女性

<步驟?
查出英文字所代表的數字
再將所查出的數字 “十位數+個位數x9”
例: 台北市=10 => 1 + 0x9 =1
台中市=11 => 1 + 1x9 =10

N2x8 + N3x7 + N4x6 + N5x5 + N6x4 + N7x3 + N8x2 + N9x1 + N10x1
將流水碼依序乘876543211
一個個乘.乘完要加起來.（別忘了先乘除後加減）
例: 123456789 =>
1×8+2×7+3×6+4×5+5×4+6×3+7×2+8×1+9×1

3.將步驟1 和步驟2 的兩個數加起來除以10.
例:
步驟1 台北計算結果 =1
步驟2 1x8 + 2x7 + 3x6 + 4x5 + 5x4 + 6x3 + 7x2 + 8 + 9 =129 
(1+129)/10
除10後看看是否可以整除.如可以整除即為正確的
身份證字號. 如無法整除即是錯誤的身份證字號
(1+129)/10 = 13 => 可以整除.正確

說明:
輸入為一個長度與性別皆為正確的身分證字號，請回傳合法、不合法
'''

city_dict = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':34,'J':18,'K':19,'L':20,'M':21, 'N':22, 'O':35, 'P':23, 'Q':24, 'R':25, 'S':26, 'T':27, 'U':28, 'V':29, 'W':32, 'X':30,'Y':31,'Z':33,}

in_txt = 'W234567844'
sum_first = int(str(city_dict[in_txt[0]])[0]) + (int(str(city_dict[in_txt[0]])[1])*9)
# print(sum_first)

sum_second = 0
for i in range(1, len(in_txt)):
    # print(in_txt[i], 9-i)
    sum_second += (int(in_txt[i]) * (9-i))
sum_second += (int(in_txt[-1]) * 1)
# print(sum_second)
# print(1*8+2*7+3*6+4*5+5*4+6*3+7*2+8*1+9*1)

result_sum = sum_first + sum_second
# print(result_sum)
if result_sum % 10 == 0: print('合法')
else: print('不合法')

