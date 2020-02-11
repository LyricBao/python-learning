# code learning practiced by desmond
# date 2019.11.17

'''
定义一个函数，该函数可接收一个 list 作为参数，该函数使用直接选择排序对 list 排序 。
前一个和后一个比 两重
'''

def sort(list):
    list_len = len(list)
    for i in range(0, list_len):
        for j in range(i + 1, list_len):
            if list[i] > list[j]:

                num1 = list[i]
                list[i] = list[j]
                list[j] = num1
    print(list)
list_test = [3,4,7,2,1,8,0,5,7]
sort(list_test)
print(list_test)