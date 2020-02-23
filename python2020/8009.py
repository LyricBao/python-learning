file = open("/Users/lyricbao/Downloads/ip.txt")
for line in file:
    line = line.strip() + ":8009"
    with open('result.txt', 'a+') as r:
        r.write(line + '\n')
file.close()
