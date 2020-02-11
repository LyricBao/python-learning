# code learning
# practiced by desmond
# date 2019.11.14
# 3.3-3.5
import random

length = int(input("please input the list length"))
my_list = []
for ii in range(length):
    num = random.random()
    my_list.append(num)
print(my_list)


#random.randint
my_list2 = []
for i in range(length):
    num = random.randint(1,100)
    if num % 2 ==0:
        my_list2.append(num+1)
    else:
        my_list2.append(num)
print(my_list2)


my_list3 = []
for i in range(length):
    num = random.randint(65,65+26)
    my_list3.append((chr(num)))
print(my_list3)

