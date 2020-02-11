# 使用循环输 出空心菱形 。 例如用户输入 7 (用户输入偶数， 则提示不能打印 )， 输出如下结果:

height = int(input("plz input the height"))
if height % 2 == 0:
    print("can not print")
else:
    half_height = height // 2
    print(half_height)
    for i in range(half_height):
        half_blank = " " *(int((2 * half_height -1-(2 * i + 1)/2)))
        if i == 0:
            print(half_blank,"*",half_blank,sep = '')
        else:
            mid_blank = " " * (2 * i -1)
            print(half_blank,"*",mid_blank,"*",half_blank,sep = '')
