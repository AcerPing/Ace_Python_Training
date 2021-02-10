#TODO:03 Expression 運算式
#TODO:Import Random Library
import random
# print(random.random()) #Random Float x, 0.0 <= x < 1.0
# print(random.uniform(1,20)) #Random Float x, n <= x < n
# print(random.randint(5,20)) #Integer from n to n, endpoints included
# print(random.choice("abcdefg")) #Choose a random element

items = [0,1,2,3,4,5,5,6,7,8,9]
random.shuffle(items)
# print(items)
print(random.sample(items, 3)) #choose 3 elements