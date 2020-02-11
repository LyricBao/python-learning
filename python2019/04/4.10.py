# code learning
# author desmond
# date 2019.11.15
'''
打印出如下所示的近似圆，只要给定不同的半径，圆的大小就会随之发生改变(如果需要
使用复杂的数学运算，则可使用 Python的 math模块)。
'''
r = int(input("plz input the radius"))
for i in range(2 * r + 1):
    half = round((r ** 2 - (r - i) ** 2) ** 0.5)
    print(" " * (r - half), end = "")
    print("*",end = " ")
    print(" " * half * 2, end = "")
    print("*")
