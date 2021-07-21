      
#數字轉換
def ConvertNum(s):
    try:
        s = str(float(str(s).strip().replace(',', '')))
        if s.count('.') == 0:
            s = s.replace('.0', '')
            return int(s)
        if s.count('.') == 1:
            sl = s.split('.')
            left = sl[0]
            right = sl[1]
            if int(right) == 0:
                return int(left)
            else:
                return float(s)
        else: raise Exception
    except:
        return s


in_txt = '0*99999'
if '+' in in_txt:
    in_list = in_txt.split('+')
    try:
        int(in_list[0])
        int(in_list[1])
    except: raise ValueError
    print(ConvertNum(in_list[0]) + ConvertNum(in_list[1]))

elif '-' in in_txt:
    in_list = in_txt.split('-')
    try:
        int(in_list[0])
        int(in_list[1])
    except: raise ValueError
    print(ConvertNum(in_list[0]) - ConvertNum(in_list[1]))

elif '-' in in_txt:
    in_list = in_txt.split('-')
    try:
        int(in_list[0])
        int(in_list[1])
    except: raise ValueError
    print(ConvertNum(in_list[0]) - ConvertNum(in_list[1]))

elif '*' in in_txt:
    in_list = in_txt.split('*')
    try:
        int(in_list[0])
        int(in_list[1])
    except: raise ValueError
    print(ConvertNum(in_list[0]) * ConvertNum(in_list[1]))

elif '/' in in_txt:
    in_list = in_txt.split('/')
    try:
        int(in_list[0])
        int(in_list[1])
    except: raise ValueError
    print(ConvertNum(in_list[0]) // ConvertNum(in_list[1]))

else: raise ValueError
