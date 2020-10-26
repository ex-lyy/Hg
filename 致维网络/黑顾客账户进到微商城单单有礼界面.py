# -*- encoding：utf-8 -*-
# 文件名称：Lyy-黑顾客账户进到微商城单单有礼界面
# 作者:清许丶
# 谨记:遵守秩序，尊重选择。
# 创建时间：2020/8/22 17:44


# import sys
# sys.path.append(r'D:\Lyy\main.py')
from main import *


org_code = 'chenbaby'
member_no = '1380809'
phone = '15068250848'
admin_phone = '17633705244'


if __name__ == '__main__':
    master_dbname = 'ris_production'
    server, dbconfig, cursor = connect_masterDB(master_dbname)
    while True:
        print("欢迎使用!", '*' * 50, "\n请按照下列规则输入您需要的操作：\n1：使用会员号进行；\n2：使用手机号进行；\n3：使用管理员手机号进行；")
        choose = input("请输入您的选择：")
        if choose == '1':
            sql = "SELECT * FROM ris_production.members WHERE org_code = '%s' AND member_no = '%s';" % (
                org_code, member_no)
            break
        elif choose == '2':
            sql = "SELECT * FROM ris_production.members WHERE org_code = '%s' AND phone = '%s';" % (org_code, phone)
            break
        elif choose == '3':
            sql = "SELECT * FROM ris_production.members WHERE org_code = '%s' AND phone = '%s';" % (
            org_code, admin_phone)
            break
        else:
            print("您的输入有误，请重新输入!")
    res = cursor.execute(sql)
    data = cursor.fetchone()
    try:
        member_no = data['member_no']
        phone = data['phone']
        name = data['name']
        seq = data['seq']
        jw_id = data['jw_id']
        print("姓名：", name)
        print("会员号：", member_no)
        print("手机号：", phone)
        print("jw_id：", jw_id)
        print("序列号：", seq)
        url = "https://%s.w.joowing.com/org/%s/prize_histories?activity_type=prize&app_code=477710&app_type=app&usr=%s" % (org_code, org_code, seq)
        print("微商城链接：",url)
        open_chrome(url)
        close_sshserver(server, dbconfig, cursor)
    except Exception  as e:
        close_sshserver(server, dbconfig, cursor)
        print("您查询的会员信息不存在，请确认！！")
