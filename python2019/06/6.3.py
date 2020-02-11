'''
定义代表二维坐标系上某个点的 Point 类(包括 x、 y 两个属性)，
为该类提供一个方法用 于计算两个 Point之间的距离，
再提供一个方法用于判断三个 Point组成的三角形是钝角、锐角还 是直角三角形 。
'''

class Point:
    def __init__(self,x ,y):
        self.x = x
        self.y = y
    def distance(self, p1):
        '''distance'''
        return ((self.x-p1.x)**2 + (self.y -p1.y)**2)**0.5

    def judge(self,p1,p2):
        '''判断三个 Point组成的三角形是钝角、锐角还 是直角三角形 '''
        self_p1 = self.distance(p1)
        self_p2 = self.distance(p2)
        p1_p2 = p1.distance(p2)
        # 如果self_p1的距离最大
        if self_p1 > self_p2 and self_p1 > p1_p2:
            if self_p1 > (self_p2 + p1_p2):
                print('不是三角形')
            else:
                print("钝角三角形") if self_p1 ** 2 > (self_p2 ** 2 + p1_p2 ** 2) \
                    else print("锐角三角形") if self_p1 ** 2 < (self_p2 ** 2 + p1_p2 ** 2) \
                    else print("直角三角形")
        # 如果self_p2的距离最大
        if self_p2 > self_p1 and self_p2 > p1_p2:
            if self_p2 > (self_p1 + p1_p2):
                print('不是三角形')
            else:
                print("钝角三角形") if self_p2 ** 2 > (self_p1 ** 2 + p1_p2 ** 2) \
                    else print("锐角三角形") if self_p2 ** 2 < (self_p1 ** 2 + p1_p2 ** 2) \
                    else print("直角三角形")
        # 如果p1_p2的距离最大
        if p1_p2 > self_p1 and p1_p2 > self_p2:
            if p1_p2 > (self_p1 + self_p2):
                print('不是三角形')
            else:
                print("钝角三角形") if p1_p2 ** 2 > (self_p1 ** 2 + self_p2 ** 2) \
                    else print("锐角三角形") if p1_p2 ** 2 < (self_p1 ** 2 + self_p2 ** 2) \
                    else print("直角三角形")

    def __repr__(self):
        return 'Point(x=%s, y=%s)' % (self.x, self.y)

if __name__ == '__main__':
    pt = Point(1, 1)
    print(pt.distance(Point(2, 3)))
    pt.judge(Point(4, 1), Point(5, 5))