#code learning
# author Desmond
# date 2019.11.14

string = input("please input ur string")
sub_string = input("please input ur sub_string")


#length
str_len = len(string)
sub_str_len = len(sub_string)
print(str_len, "\n", sub_str_len)
ct = 0
for i in range(str_len-1):
    if string[i:i + sub_str_len] == sub_string:
        ct +=1
print("sub_string show %d times in string" % ct)
