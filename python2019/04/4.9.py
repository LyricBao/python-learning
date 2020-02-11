# code learning practiced by desmond
# date 2019.11.16

'''
输入 一 行字 符， 分别统计出其中英文字母 、 空格、数字和其他字符的个数
'''

string = str(input("plz input ur string"))
print(string)

space = 0
letters = 0
else_str = 0
for i in string:

    if i == " ":
        space = space +1

    elif i >= "A" and i <= "Z" or i >= "a" and i <= "z":
        letters = letters+1

    else:
        else_str = else_str+1

print("this string has %s space, %s letters, %s other string " % (space, letters, else_str))