#code learning
# author DesMond
# date 2019.11.14

string = input("请输入字符串")
i = input("请输入位置")
character = input("请输入替换字符")
position = int(i)
str_new = string[:position]+ character + string[position+1:]
print(string)
print(str_new)