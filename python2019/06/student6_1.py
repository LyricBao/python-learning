'''
编写一个学生类，提供 name、 age、 gender、 phone、 address、巳mail等属性，为学生类提供 带所有成员变量的构造器，
为学生类提供方法，
用于描绘吃、喝、玩、睡等行为。
'''

class Student:
    def __init__(self, name, age, gender, phone, address, email):
        '''构造器'''
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.address = address
        self.email = email

    def eat(self, food):
        '''eat'''
        print('%s is eating %s' % (self.name, food))

    def drink(self, drink):
        print('%s is drinking %s' % (self.name, drink))

    def havefun(self,fun):
        print('I am %s years old and like having fun with %s ' % (self.age,fun))
    def sleep(self):
        print('%s is sleeping at %s' % (self.name,self.address))

    def __repr__(self):
        return 'student(name=%s,age=%d, phone=%s,address = %s ,email=%s ' % (self.name, self.age,self.phone, self.address, self.email)


if __name__ == '__main__':
    student1 =Student("Ly",14,'Male','19908907680', 'Washington DC','aaa.gmail.com')
    student1.eat('hamberger')
    student1.drink('orange juice')
    student1.havefun('basketball')
    student1.sleep()


