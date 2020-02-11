'''
给定3， 输出:
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
'''


# from internet
# 参考 https://blog.csdn.net/qq_36652379/article/details/101906112

print("4.11画阵列")
num = int(input("plz input the num"))


char_list = [[col for col in range(4 * num - 3)] for raw in range(2 * num - 1)]
for raw in range(2 * num - 1):
    for col in range(4 * num - 3):  # 先将每一行的元素都赋值为'-'
        char_list[raw][col] = '-'
    if raw < num:  # 上半部分
        for i in range(raw + 1):  # 修改每一行特殊位置的元素
            char_list[raw][2 * num - 2 - 2 * i] = chr(ord('a') + i + abs(num - 1 - raw))
            char_list[raw][2 * num - 2 + 2 * i] = chr(ord('a') + i + abs(num - 1 - raw))
    else:
        for i in range(num - (raw - num) - 1):
            char_list[raw][2 * num - 2 - 2 * i] = chr(ord('a') + i + abs(num - 1 - raw))
            char_list[raw][2 * num - 2 + 2 * i] = chr(ord('a') + i + abs(num - 1 - raw))



for raw in range(2 * num - 1):
    for col in range(4 * num - 3):
        print(char_list[raw][col], end="")
    print("")


