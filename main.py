# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pymysql


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


def connect_myselfDB():
    dbname = 'Lyy'
    dbconfig = pymysql.connect(host='localhost', port=3306, database=dbname, user='root', password='ex19950816')
    cursor = dbconfig.cursor()
    return dbconfig, cursor