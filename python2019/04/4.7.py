#code learning practiced by desmond
# date 2019.11.16

'''

判断 101~200之间有多少个素数，并输出所有的质数。

'''

prime_list = []

for i in range(101,201):
    is_prime = True
    for j in range(2,i):
        if i % j ==  0:
            is_prime = False
            break
    if is_prime:
        prime_list.append(i)

print("101~200 has " + str(len(prime_list)) + " prime bumber")
print(prime_list)
