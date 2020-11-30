# -*- coding:utf-8 -*-
# 文件名称：Lyy-互检人员替换
# 作者:清许丶
# 谨记:遵守秩序，尊重选择。
# 创建时间：2020/10/12 下午 01:46

operator_list = ['歆雨','维成','雅馨','雅馨','姝锋','维成','雅馨','歆雨','歆雨','姝锋','陈冲','雅馨','嘉媛','嘉媛','雅馨','雅馨','虬珅','虬珅','陈冲','陈冲','姝锋','雅馨','文欣','周猛','姝锋','邹庆','邹庆','虬珅','嘉媛','嘉媛','歆雨','陈冲','陈冲','陈冲','陈冲','陈冲','雅馨','雅馨','雅馨','歆雨','歆雨','歆雨','迟明','迟明','迟明','姝锋','姝锋','姝锋','俊奇','迟明','嘉媛','维成','邹庆','邹庆','姝锋','姝锋','陈冲','陈冲','陈冲','陈冲','陈冲','文欣']

examine_list = []

for i in operator_list:
    if i == '维成' or i == '雅馨':
        examine_list.append('周猛')
    elif i == '歆雨' or i == '陈冲':
        examine_list.append('张波')
    elif i == '张波' or i == '嘉媛' or i == '骆翔':
        examine_list.append('陈冲')
    elif i == '虬珅' or i == '周猛':
        examine_list.append('姝锋')
    elif i == '邹庆' or i == '宇豪':
        examine_list.append('俊奇')
    elif i == '姝锋':
        examine_list.append('甘')
    elif i == '苏航' or i == '施':
        examine_list.append('东')
    elif i == '迟明':
        examine_list.append('宇豪')
    else:
        examine_list.append(i)
for j in examine_list:
    print(j)
