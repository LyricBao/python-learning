#code learning
# author Desmond
# date 2019.11.14

a = input("please input 1 string")
b = input("please input 2nd string")
c = input("please input 3rd string")

tuple = (a, b, c)
print(tuple * 3)

tuple2 =(tuple,tuple * 3)
print(tuple + tuple2)

