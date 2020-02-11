# code learning, practiced by desmond
#date 2019,11,18

'''
定义一个fn(n）函数，该函数返回n 的阶乘。
'''

n = int(input("plz input the n"))


def fn(n):
    factorial = 1
    # 查看数字是负数，0 或 正数
    if n < 0:
        print("负数没有阶乘")
    elif n == 0:
        print("0 的阶乘为 1")
    else:
        for i in range(1, n + 1):
            factorial = factorial * i
        print("%d 的阶乘为 %d" % (n, factorial))

re = fn(n)

