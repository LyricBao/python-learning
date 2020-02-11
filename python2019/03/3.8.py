# practiced by DesMond
# date 2019.11.14
char_list = input("A-Z".split())
char_dict = {}.fromkeys(char_list)
print(char_list)
print(char_dict)
for k in char_dict.keys():
    char_dict[k] = char_list.count(k)
print(char_dict)