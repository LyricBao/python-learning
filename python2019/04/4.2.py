# code learning
# practiced by Desmond
# date 2019.11.16

#使用循环输出等腰三角形**

height = int(input("plz input the height"))
for i in range(height):
    star = "*" * (2 * i + 1)
    half_blank = "a" * (int((height * 2 - 1 - (2 * i + 1 )/2)))
    print(half_blank,star,half_blank)


#方便调试因此用a，可把a变成空格