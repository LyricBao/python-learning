#code learning
#practiced by desmond
# date 2019.11.16

'''
使用循环输出菱形 。
例如用户输入 7
(用户输入偶数，则提示不能打印〉 ，
输出如下结果
     *
    ***
   *****
  *******
   *****
    ***
     *

'''
height = int(input("plz input the height"))
half_height = (height + 1 ) // 2
for i in range(half_height):
    star = "*" * (2 * i + 1)
    half_blank = "a"*(int((2 * half_height-1-(2 * i + 1))/2))
    print(half_blank, star, half_blank)
for i in range(half_height-2,-1,-1):
    star = "*" * (2 * i + 1)
    half_blank = "a"*(int((2 * half_height-1-(2 * i + 1))/2))
    print(half_blank, star, half_blank)
#a 用于调试，可把a变成空格