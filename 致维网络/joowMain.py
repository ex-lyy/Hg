# -*- encoding：utf-8 -*-
# 文件名称：Lyy-joowMain
# 作者:清许丶
# 谨记:遵守秩序，尊重选择。
# 创建时间：2020/9/29 下午 09:22

from main import *
import calendar
import time
import requests
import re


# 查询导购今日销售
def find_guider_daily_sale_amount(org_code, guider_no):
    master_dbname = org_code + 'dw'
    server, dbconfig, cursor = connect_DWDB(master_dbname)
    sql = f'''SELECT SUM(real_amount) AS 'sales_performance',COUNT(DISTINCT order_no) AS 'order_count' FROM `prt_sales` WHERE guider_code = '{guider_no}';'''
    cursor.execute(sql)
    guider_data = cursor.fetchone()
    sales_performance = guider_data['sales_performance']
    order_count = guider_data['order_count']
    close_sshserver(server, dbconfig, cursor)
    return sales_performance, order_count


# 查询导购上月销售额
def find_guider_last_month_sale_amout(org_code, guider_no):
    day_now = time.localtime()
    day_begin = '%d-%02d-01' % (day_now.tm_year, day_now.tm_mon - 1)  # 月初肯定是1号
    wday, monthRange = calendar.monthrange(day_now.tm_year, day_now.tm_mon)  # 得到本月的天数 第一返回为月第一日为星期几（0-6）, 第二返回为此月天数
    day_end = '%d-%02d-%02d' % (day_now.tm_year, day_now.tm_mon - 1, monthRange)
    master_dbname = org_code + 'dw'
    server, dbconfig, cursor = connect_DWDB(master_dbname)
    sql = f'''SELECT SUM(amount) AS 'sales_performance',COUNT(DISTINCT order_no) AS 'order_count' FROM `fct_sales` WHERE sales_time BETWEEN '{day_begin}' AND '{day_end}' AND guider_code = '{guider_no}';'''
    cursor.execute(sql)
    guider_data = cursor.fetchone()
    sales_performance = guider_data['sales_performance']
    order_count = guider_data['order_count']
    close_sshserver(server, dbconfig, cursor)
    return sales_performance, order_count


# 查询导购本月销售额
def find_guider_monthly_sale_amout(org_code, guider_no):
    day_now = time.localtime()
    day_begin = '%d-%02d-01' % (day_now.tm_year, day_now.tm_mon)  # 月初肯定是1号
    wday, monthRange = calendar.monthrange(day_now.tm_year, day_now.tm_mon)  # 得到本月的天数 第一返回为月第一日为星期几（0-6）, 第二返回为此月天数
    day_end = '%d-%02d-%02d' % (day_now.tm_year, day_now.tm_mon, monthRange)
    master_dbname = org_code + 'dw'
    server, dbconfig, cursor = connect_DWDB(master_dbname)
    sql = f'''SELECT SUM(amount) AS 'sales_performance',COUNT(DISTINCT order_no) AS 'order_count' FROM `fct_sales` WHERE sales_time BETWEEN '{day_begin}' AND '{day_end}' AND guider_code = '{guider_no}';'''
    cursor.execute(sql)
    guider_data = cursor.fetchone()
    sales_performance = guider_data['sales_performance']
    order_count = guider_data['order_count']
    close_sshserver(server, dbconfig, cursor)
    return sales_performance, order_count


# 对员工表的密码进行简单解密
def decode_MD5(org_code, guider_no):
    master_dbname = 'ris_production'
    server, dbconfig, cursor = connect_master_copy_DB(master_dbname)
    sql = f'''SELECT password FROM ris_production.staffs a LEFT JOIN ris_production.retailer_configs b on b.retailer_id = a.retailer_id WHERE b.org_code = '{org_code}' AND no = '{guider_no}';'''
    cursor.execute(sql)
    password = cursor.fetchone()
    password = password['password']
    close_sshserver(server, dbconfig, cursor)
    return password


# 查询PLUS会员返豆记录
def find_plus_member_bean_list(org_code, jw_id):
    master_dbname = 'account_backend_production'
    server, dbconfig, cursor = connect_masterDB(master_dbname)
    sql = f'''SELECT amount,pre_amount,post_amount,source_code,uniq_id,source_payload FROM account_backend_production.account_portion_history WHERE account_id = (SELECT id FROM account_backend_production.account WHERE org_code='{org_code}' AND account_owner_id = '{jw_id}');'''
    cursor.execute(sql)
    bean_info_list = cursor.fetchall()
    close_sshserver(server, dbconfig, cursor)
    return bean_info_list

# 查询会员的基本信息
def find_member_info_by_phone(org_code,phone):
    master_dbname = 'ris_production'
    server, dbconfig, cursor = connect_master_copy_DB(master_dbname)
    sql = f'''SELECT name,member_no,phone,jw_id,birthday,seq,created_at,referee_shop FROM ris_production.members WHERE org_code = '{org_code}' AND phone = '{phone}';'''
    cursor.execute(sql)
    member_data = cursor.fetchone()
    close_sshserver(server, dbconfig, cursor)
    # name, member_no, phone, jw_id, birthday, seq, created_at, referee_shop
    return member_data
