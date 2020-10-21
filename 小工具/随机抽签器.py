# -*- coding:utf-8 -*-
# 文件名称：Lyy-随机抽签器
# 作者:清许丶
# 谨记:遵守秩序，尊重选择。
# 创建时间：2020/10/20 13:22
import random

operator_list = ['嘉媛','歆雨','邹庆','迟明']

for i in range(5):
    operator = random.choice(operator_list)
    print(operator)