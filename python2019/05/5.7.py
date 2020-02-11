# code learning,practiced by desmond
# date 2019.11.18
'''
定义一个函数，该函数可接收一个list 作为参数，该函数用于去除list 中重复的元素。
'''


def list_remove(list1):
    list_new = list({}.fromkeys(list1).keys())
    return list_new


list_length = int(input("plz input the length of the list"))
list_origin = []
for i in range(list_length):
    list_origin.append(input("plz input the list"))
print("the original list is ",list_origin)

list_after = list_remove(list_origin)
print("the changed list is ", list_after)




