# code learning,practiced by desmond
# date 2019.11.17

'''
定义一个 is leap(year)函数，该函数可判断 yea1 是否为闰年。若是闰年，则返回 True;否
则返回 False
'''

def is_leap(year):
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

year = int(input("plz input a year number"))
if is_leap(year):
    print("Yes")
else:
    print("No")
