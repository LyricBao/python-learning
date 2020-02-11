# code learning ,practiced by desmond
# date 2019.11.16

'''
打印出所有的“水仙花数”。 所谓“水仙花数”，是指一个三位数，其各位数字的立方和等 于该数本身。 例如， 153是一个“水仙花数”，因为 153=1^3+5^3+3^3
'''
for i in range(100,1000):
    n1 = i // 100
    n2 = i // 10 % 10
    n3 = i %10

    num = n1 **3 + n2 ** 3 + n3 **3
    if num == i:
        print(num,end=" ")
