# code learning,practiced by desmond
# date 2019.11.17
'''
定义一个 count_str_char(my_st1)函数，该函数返回参数字符串中包含多少个数字、 多 少个
英文字母、多少个空白字符、多少个其他字符 。
'''
import sys

def count_str_char(my_st1):
    num, alpha, space, other = 0, 0, 0, 0
    for i in my_st1:
        if i.isdigit():
            num = + 1
        elif i.isalpha():
            alpha = + 1
        elif i.isspace():
            space = + 1
        else:
            other = + 1
    return num, alpha, space, other

string = input("plz input a string")

digit_num, alpha_num, space_num,other_num = count_str_char(string)
print("digit number: %s" % digit_num)
print("alpha number: %s" % alpha_num)
print("space num : %s" % space_num)
print("else: %s " %  other_num)
