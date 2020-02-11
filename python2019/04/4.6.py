# code learning by desmond
#date 2019.11.16

'''
用户输入自己的成绩，程序会自动判断该成绩的类型: 成绩>=90分用 A表示， 80~89分用 B表示， 70~79分用C表示，其他的用D表示
'''

score = int(input("plz input ur exam score"))
print("ur score grade is:",end="")
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")