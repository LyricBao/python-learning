# code learning, practiced by desmond
# date 2019.11.18

'''
5.9定义一个fn(n）函数，该函数返回一个包含n 个不重复的大写字母的元组。
'''

import random

def fn(n):
    i = 0
    tuple_init = []

    while True:
        num = random.randint(65, 65+25)

        if num not in tuple_init:
            tuple_init.append(chr(num))
            i += 1
        if i == n:
            break
    return tuple(tuple_init)



n = int(input("plz input a num"))
tuple_list = fn(n)
print(tuple_list)
print(len(tuple_list))