# code learning,practiced by desmond
# date 2019.11.18
'''
5. 定义一个fn(n）函数，该函数返回l哨的立方和，即求1+2*2*2+3*3*#
'''

n = int(input("plz input the n"))

def fn(n):
    sum = 0
    if   0< n < 2:
        sum = 1
        print("1~%d 的立方和是%d " % (n, sum))
    elif n >= 2:
        for i in range(2,n + 1):
            sum += i ** 3
        print("1~%d 的立方和是%d " % (n, sum))
    else:
        print("plz input n (n>0)")


    return sum

re = fn(n)

