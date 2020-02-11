'''
利用第 l 题定义的 Student类，定义一个列表保存多个 Student对象作为通讯录数据 。
程序 可通过 name、 email、 address 查询，如果找不到数据，则进行友好提示 。
'''
from student6_1 import Student

contacts = [Student('Ly', 14, 'MALE', '19928098767',
    'washington dc', 'aaa@gmail.com'),
     Student('des', 15, 'MALE', '19920390987',
    'tex', 'des@aa.com'),
    Student('lion', 23, 'MALE', '19999999999',
    'ny', 'lion@aa.com'),
    Student('mon', 90, 'MALE', '1999989999',
    'tai', 'monkey@aa.com')]

def find_by_name(name):
    return [x for x in contacts if name in x.name]
def find_by_email(email):
    return [y for y in contacts if email in y.email]
def find_by_address(address):
    return  [z for z in contacts if address in z.address]

if __name__ == '__main__':
    search = input('plz input the search way,name(n),email(e),address(a)')
    key = input('plz input the key')
    if search =='n':
        print(find_by_name(search))
    elif search =='e':
        print(find_by_email(search))
    elif search == 'a':
        print(find_by_address(search))
    else:
        print('wrong query')

