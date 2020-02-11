# code learning
# practiced by desmond
# date 2019.11.14

import random

length = int(input("input the length of list"))
my_list = []
for i in range(length):
    my_list.append(input("please input strings"))
print(my_list)

new_list = []
[new_list.append(i) for i in my_list if not i in new_list]
print(new_list)


#anothor method
new_list = list({}.fromkeys(my_list).keys())
print(new_list)
