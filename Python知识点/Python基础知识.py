# -*- coding:utf-8 -*-
# 文件名称：Lyy-20201023001
# 作者:清许丶
# 谨记:遵守秩序，尊重选择。
# 创建时间：2020/10/23 17:16

'''
注释：
    1.在要注释的内容前面加#，#之后的所有内容都会注释掉
    2.三个单引号加三个单引号，三个单引号之间的内容都会被注释掉
'''

# a = 1213131

# print("hello world!")
# 打印：将数据在显示器上显示

'''
数据类型：
Number（数字）          Int,float 123456
String（字符串）         str  '123455'或者"sdadsadsa"   在某些字符串里面需要用到引号，注意单双引号的自动匹配
List（列表）            list
Tuple（元组）           tuple 元组的数据不能修改
Set（集合）             set
Dictionary（字典）      dic

int = 121313
str = '汉字GBK，国际通用utf8'
list = ['1',2,[1,2],'1']
tuple = (1,2,3,1)
set = (1,2,3,1)
dic = {'name':'chenchong','age':'18','address':'上海'}

type(parse)函数用来获取当前数据的数据类型，parse指数据或者变量
print(type(int))
print(type(str))
print(type(list))
print(type(tuple))
print(type(set))
print(type(dic))
'''

'''
索引：针对可迭代的元素（list，set）
    对元素标号（0开始依次加1）
    list  = [1,2,3,4,5,6,7,8]
    str = '12345678'
    print(list[1:2]) 切片
    print(str[1:2])
    
    list = [1, 2, 3, 4, 5, 6, 7, 8]
    print(list[0:-3:1])

'''

'''
运算符：
    sum  = 1+1
    jian = 2-1
    cheng = 2*2
    chu = 16/2
    qumo = 16%5   等于3余1  #取模就是取余数
    乘方 =  2**3  2的三次方/三次幂
    取整除 = 16//5 等于3余1  #取整数就是取的商
        取整除操作是向下取整，如果是复数的话要特别注意，如：
            a = 3 // -2
            print(a)
            # >>>-2
    比较运算：
        ==:比较两个对象是否相等
        !=:比较两个对象是否不相等  SQL：<>
        <
        >
        <=
        >=
    赋值运算：
        =:简单的赋值运算符 
        +=:加法赋值运算符    a += 2   a = a+2    
        -=:减法赋值运算符              a = a-2                       
        *=:乘法赋值运算符      a = a*2
        /=:除法赋值运算符      a = a/2
        %=:取模赋值运算符      a = a%2
        **=:幂赋值运算符
        //=:取整除赋值运算符
    位运算（两个数值都要先转成二进制数字计算）：
        &：按位与，同1才为1
        |：按位或，有1为1
        ~：按位非，按位取反
        ^：按位异或，相同为0，不同为1
        <<：左移运算  左移乘以2的N次方，右移除以2的N次方
        >>：右移运算  左移乘以2的N次方，右移除以2的N次方
'''

'''
循环
while循环：当什么条件满足的时候，才循环
    
    while 条件判断：（如果条件满足，执行循环体）
        循环体
        
        
for循环：当什么条件不满足时，才停止循环
    
    for 条件：
        循环体
        
        i = 0
while i < 100:
    print("循环")
    i += 1


for i in range(100):
    print("循环")


循环退出：
break 退出本层循环
continue 退出本次循环

# for i in range(100):
#     if i == 59:
#         continue
#     print(i)

for i in range(100):
    print("a")
    for j in range(100):
        print("b")
        break


'''

'''
判断：
if 条件：
    满足
else 条件：
    不满足
    
if a == 1:
    print(1)
elif a == 2:
    print(2)
elif a == 3:
    print(3)
elif a == 4:
    print(4)
else:
    print(0)
'''

a = 1
b1 = a

# a = a+1

a += 1
print(b1,a)