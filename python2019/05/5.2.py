# code learning,practiced by desmond
# date 2019.11.17

'''
定义一个函数，该函数可接收一个 list作为参数，该函数使用冒泡排序对 list排序
一个和后面的比,后面的都有序
'''

def bubble_sort(list):
    list_len = len(list)

    for i in range(0, list_len):
        is_sorted = True
        for j in range(0, list_len-i-1):
            if list[j] > list[j + 1]:
                tmp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = tmp
                is_sorted = False


list_test = [3,1,9,-100,34,78,34,55,55]
bubble_sort(list_test)
print(list_test)