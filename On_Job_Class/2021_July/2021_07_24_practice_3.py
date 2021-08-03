'''
說明:
輸入為一串數字，每個數字間以一個空白隔開，數字長度不固定，請把這些數字每個各加1後輸出
'''
int_txt = '1 2 3 4 5'
int_list = int_txt.split()
# print(int_list)
r = 0
string = ''
while r < len(int_list):
    # print(int(int_list[r])+1, end=' ')
    string += str(int(int_list[r])+1) + ' '
    r += 1
print(string.strip())