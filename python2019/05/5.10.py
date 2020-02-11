# code learning, practiced by desmond
# date 2019.11.18
'''
定义一个fn(n）函数，其中n 表示输入n 行n 列的矩阵（数的方阵〉。在输出时，先输出n
行n 列的矩阵，再输出该矩阵的转置形式。例如，当参数为3 时，先输出：
123
456
789

再输出：
147
258
369

'''

def fn(n):
    for i in range(0, n):
        for j in range(0, n):
            print("%2d" % (i * n + j + 1), end="    ")
        print()

    print("-----" * 10)

    for i in range(0, n):
        for j in range(0, n):
            print("%2d" % (j * n + i + 1), end="    ")
        print()

    print("finish")




n = int(input("plz input a n"))

if n >0:
    fn(n)
else:
    print("plz input a right num")