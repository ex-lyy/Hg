# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pymysql
import copy
from ast import literal_eval
import json

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    return 0




# 连接致维公司备库
def connect_master_copy_DB(master_dbname):
    from sshtunnel import SSHTunnelForwarder
    # 指定SSH远程跳转
    server = SSHTunnelForwarder(
        ssh_address_or_host=('222.73.36.230', 2002),  # 指定SSH中间登录地址和端口号
        ssh_username='chong.chen',  # 指定地址B的SSH登录用户名
        ssh_password='ex19950816',  # 指定地址B的SSH登录密码
        # local_bind_address=('127.0.0.1'),
        # 绑定本地地址A（默认127.0.0.1）及与B相通的端口（根据网络策略配置，若端口全放，则此行无需配置，使用默认即可）
        remote_bind_address=('mysql3307.service.consul', 3307)  # 指定最终目标C地址，端口号为mysql默认端口号3306
    )
    server.start()
    # 打印本地端口，以检查是否配置正确
    # print(server.local_bind_port)

    # 设置mysql连接参数，地址与端口均必须设置为本地地址与端口
    # 用户名和密码以及数据库名根据自己的数据库进行配置
    dbconfig = pymysql.connect(
        host="127.0.0.1",
        port=server.local_bind_port,
        user="chong_chen_st",
        passwd="rdvYPB3cX4XbUYhwmQzj",
        db=master_dbname,
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = dbconfig.cursor()
    return server, dbconfig, cursor


# 连接致维公司主库
def connect_masterDB(master_dbname):
    from sshtunnel import SSHTunnelForwarder
    # 指定SSH远程跳转
    server = SSHTunnelForwarder(
        ssh_address_or_host=('222.73.36.230', 2002),  # 指定SSH中间登录地址和端口号
        ssh_username='chong.chen',  # 指定地址B的SSH登录用户名
        ssh_password='ex19950816',  # 指定地址B的SSH登录密码
        # local_bind_address=('127.0.0.1'),
        # 绑定本地地址A（默认127.0.0.1）及与B相通的端口（根据网络策略配置，若端口全放，则此行无需配置，使用默认即可）
        remote_bind_address=('rm-uf6f05k2rg95s23bp.mysql.rds.aliyuncs.com', 3306)  # 指定最终目标C地址，端口号为mysql默认端口号3306
    )
    server.start()
    # 打印本地端口，以检查是否配置正确
    # print(server.local_bind_port)

    # 设置mysql连接参数，地址与端口均必须设置为本地地址与端口
    # 用户名和密码以及数据库名根据自己的数据库进行配置
    dbconfig = pymysql.connect(
        host="127.0.0.1",
        port=server.local_bind_port,
        user="chong_chen_st",
        passwd="rdvYPB3cX4XbUYhwmQzj",
        db=master_dbname,
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = dbconfig.cursor()
    return server, dbconfig, cursor


# 链接致维DW库
def connect_DWDB(DW_dbname):
    from sshtunnel import SSHTunnelForwarder
    # 指定SSH远程跳转
    server = SSHTunnelForwarder(
        ssh_address_or_host=('222.73.36.230', 2002),  # 指定SSH中间登录地址和端口号
        ssh_username='chong.chen',  # 指定地址B的SSH登录用户名
        ssh_password='ex19950816',  # 指定地址B的SSH登录密码
        # local_bind_address=('127.0.0.1'),
        # 绑定本地地址A（默认127.0.0.1）及与B相通的端口（根据网络策略配置，若端口全放，则此行无需配置，使用默认即可）
        remote_bind_address=('mysql3306.service.consul', 3306)  # 指定最终目标C地址，端口号为mysql默认端口号3306
    )
    server.start()
    # 打印本地端口，以检查是否配置正确
    # print(server.local_bind_port)

    # 设置mysql连接参数，地址与端口均必须设置为本地地址与端口
    # 用户名和密码以及数据库名根据自己的数据库进行配置
    dbconfig = pymysql.connect(
        host="127.0.0.1",
        port=server.local_bind_port,
        user="chong_chen_st",
        passwd="rdvYPB3cX4XbUYhwmQzj",
        db=DW_dbname,
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = dbconfig.cursor()
    return server, dbconfig, cursor


# 关闭ssh服务/游标/数据库配置
def close_sshserver(server, dbconfig, cursor):
    cursor.close()
    dbconfig.close()
    server.close()
    return 0

# 关闭数据库链接
def close_databsesconn(dbconfig, cursor):
    cursor.close()
    dbconfig.close()
    return 0


# 打开谷歌浏览器
def open_chrome(url):
    from selenium import webdriver
    import os
    import time
    chromedriver = "E:\chromedriver_win32/chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)  # 模拟打开浏览器
    driver.get(url)  # 打开网址
    driver.maximize_window()  # 窗口最大化（无关紧要哈）
    time.sleep(1200)
    driver.quit()


# 链接个人数据库
def connect_myselfDB():
    dbname = 'Lyy'
    dbconfig = pymysql.connect(host='localhost', port=3306, database=dbname, user='root', password='ex19950816')
    cursor = dbconfig.cursor()
    return dbconfig, cursor

# 获取当前时间戳
def get_time_str():
    import time
    time_time = str(time.time()).replace('.','')
    return  time_time

# 查询礼券包基本信息
def query_couponbag_info(org_code,package_code):
    query_couponbag_info_sql = "SELECT total,`name`,optional,`desc`,related_coupon,prize_items FROM pomelo_backend_production.prize_coupon_bags WHERE org_code='%s' AND code='%s';"%(org_code,package_code)
    server, dbconfig, cursor = connect_master_copy_DB('pomelo_backend_production')
    cursor.execute(query_couponbag_info_sql)
    couponbag_info_sql_data = cursor.fetchone()
    close_sshserver(server, dbconfig, cursor)
    if couponbag_info_sql_data['related_coupon'] != '{"type": "", "params": {}, "valid_days": 7, "offset_days": 1}':
        print("礼券包‘%s‘配置的有领取后关联优惠，请进行额外的检查!"%couponbag_info_sql_data['name'])
    couponbag_base_info = copy.deepcopy(couponbag_info_sql_data)
    couponbag_base_info.pop('related_coupon')
    couponbag_base_info.pop('prize_items')
    couponbag_info_list = []
    # 处理配置的奖励数据
    couponbag_prize_items = json.loads(couponbag_info_sql_data['prize_items'])
    for prize_items in couponbag_prize_items:
        prize_items_dict = {'type':'优惠券','serial_no':'','serial_name':'','min_price':'','max_price':''}   #定义字典，储存我们配置的每一项的数据
        if prize_items['type']  == 'coupon':
            prize_items_dict['type'] = '优惠券'
            prize_items_dict['serial_no'] = prize_items['params']['serial_no']
            prize_items_dict['serial_name'] = prize_items['prize_name']
        elif prize_items['type']  == 'ticket':
            prize_items_dict['type'] = '兑换券'
            prize_items_dict['serial_no'] = prize_items['params']['activity_id']
            prize_items_dict['serial_name'] = prize_items['params']['name']
        elif prize_items['type']  == 'virtual_product':
            prize_items_dict['type'] = '积分'
            prize_items_dict['score_num'] = prize_items['params']['num']
            prize_items_dict['serial_name'] = prize_items['prize_name']
        elif prize_items['type']  == 'red_envelope':
            prize_items_dict['type'] = '红包'
            prize_items_dict['min_price'] = prize_items['params']['min_price']
            prize_items_dict['max_price'] = prize_items['params']['max_price']
            prize_items_dict['serial_name'] = prize_items['prize_name']
        elif prize_items['type']  == 'intelligent_package':
            prize_items_dict['type'] = '会员智能礼包'
            prize_items_dict['name'] = 'NA'
            prize_items_dict['serial_no'] = prize_items['params']['code']
        else:
            print("礼券包%s出现了点问题，请手动检查！"%couponbag_info_sql_data['name'])
        couponbag_info_list.append(prize_items_dict)
    # 返回活动基本信息、活动配置的奖励信息
    return couponbag_info_sql_data,couponbag_info_list

if __name__ == '__main__':
    print(sss)