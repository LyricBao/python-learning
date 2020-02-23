import os, sys
from socket import gethostbyname

# DOMAIN= "/Users/lyricbao/Downloads/domain.txt"

def main():
    # domain.txt--->domain
    with open("domain.txt", 'r') as f:
        for line in f.readlines():
            try:
                host = gethostbyname(line.strip('\n'))
            except Exception as e:
                print(e)
            else:
                # result.txt--->ip
                with open('result.txt', 'a+') as r:
                    #r.write(line.strip('\n') + ' ')
                    r.write(host + '\n')


if __name__ == '__main__':
    main()