import random
key_word = ['剪刀', '石頭', '布']
user = int(input('[0]剪刀, [1]石頭, [2]布'))
rand_num = random.randint(0, 2)
print('你出了: ', key_word[user])
print('電腦出了: ', key_word[rand_num])

# ----------比較----------
# 背後是數字的比較
# 1. 是不是平手
if user == rand_num:
    print("平手")
# 2. 我是不是贏了
elif user == (rand_num+1)%3:
    print("I Win")
# 3. 電腦贏了
else:
    print("Loser")