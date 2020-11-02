# -*- coding:utf-8 -*-
# 文件名称：Lyy-函数和类以及引入模块
# 作者:清许丶
# 谨记:遵守秩序，尊重选择。
# 创建时间：2020/10/30 15:43

# 函数：给参数执行相应功能

# 变量


# def sum(x,y):#这个里面的参数是形参
#     sum = x+y
#     return sum

sum(1,2)

# 类
class sum(object):
    # 类的方法
    def sum(self,x,y):
        return x+y

    def diff(self,x,y):
        return  x-y

    def cheng(self,x,y):
        return x * y

    def chu(self,x,y):
        return x / y


if __name__ == '__main__':
    sum = sum(16, 8)
    a = sum.sum()
    b = sum.diff()
    c = sum.cheng()
    d = sum.chu()
    print(a,b,c,d)