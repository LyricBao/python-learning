#code learning
#practiced by desmond
# date 2019.11.16


'''

3.

给定奇数 5， 输出(横、坚、斜的总和相等) :
17 24 O1 08 15 
23 05 07 14 16 
04 06 13 20 22 
10 12 19 21 03 
11 18 25 02 09
依此类推。
'''
#https://blog.csdn.net/weixin_44208042/article/details/93330954



num = int(input('请输入一个奇数:'))
# 定义一个长为num的列表
high = [[0] * num ]
# 先定义一个num*num的一个列表，之后在往里面赋值
for i in range(num-1):
   high += [[0]*num]
n = 1
# 先确定第一行中间值为1
high[0][num//2] = n
x = 0
y = num//2
# 依次向high列表赋值从2开始
for j in range(1,num*num):
   # x表示第几行，y表示第几列，j表示x，y坐标的值
   j = j + 1
   x = x - 1 
   y = y + 1
   # 判断符合哪几种可能性
   if y > (num - 1) and x < 0 :
      x = x + 2
      y = y - 1
      high[x][y]=j
   elif x < 0 :
      x = num - 1 
      high[x][y]=j
   elif y > num-1 :
      y = 0
      high[x][y]=j
   else:
      if high[x][y] == 0 :
         high[x][y]=j
      elif high[x][y] != 0 :
         x = x + 2
         y = y - 1
         high[x][y]=j
# 依次把high列表中值打印出来
for a in range(num):
   for b in range(num):
      # rjust表示输出01，02，03等这种格式，可看我上篇博文介绍
      print( str(high[a][b]).rjust(2,'0'),end=' ') 
   print()