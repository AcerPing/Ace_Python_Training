age = 18
money = 20000

# 如果年紀大於等於18，顯示歡迎光臨
if age >= 18: print('歡迎光臨')
# 如果年紀小於18，但是money大於10000也顯示歡迎光臨
elif age < 18 and money > 10000: print('歡迎光臨')
# 否則顯示謝謝惠顧
else: print('謝謝惠顧')

# 巢狀
if age >= 18: print('歡迎光臨')
else:
    if money > 10000: print('歡迎光臨')
    else: print('謝謝惠顧')