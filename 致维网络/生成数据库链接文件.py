# -*- encoding：utf-8 -*-
# 文件名称：Lyy-JMP数据库配置查询
# 作者:清许丶
# 谨记:遵守秩序，尊重选择。
# 创建时间：2020/9/18 下午 02:33

import requests
from main import *
from Nacicat密码加密文件.NavicatCipher import *
import json


def wrirte_begin_xml(connect_path):
    with open(connect_path, 'a+') as file:
        file.write('''<?xml version="1.0" encoding="UTF-8"?>''')
        file.write('\n')
        file.write('''<Connections Ver="1.4">''')
        file.write('\n')
        print("写入头文件成功！")
    return 0


def wrirte_end_xml(connect_path):
    with open(connect_path, 'a+') as file:
        file.write('''</Connections>''')
        print("写入末尾文件成功！")
    return 0


def decode_configs(org_code):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "api-gateway-resp": "crm",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Cookie": "Hm_lvt_0c2e41563784bcc9e3dabc630b67ef35=1601446845; _ga=GA1.2.367342996.1601446850; UM_distinctid=174e935c064375-048b5a48dcb821-3323766-1fa400-174e935c065a05; retailer=%7B%22id%22%3A58%2C%22code%22%3A%22ygyj%22%2C%22name%22%3A%22%E9%98%B3%E5%85%89%E7%9B%8A%E4%BD%B3%22%2C%22businesses%22%3A%5B%22payin%22%2C%22consign%22%5D%7D; joowing-staff-jwt=eyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoiY2hvbmcuY2hlbiIsImVtYWlsIjoiY2hvbmcuY2hlbkBqb293aW5nLmNvbSIsInR5cGUiOiJqb293aW5nLXN0YWZmIiwiZXhwIjoxNjAyNTEwNTA5fQ.qF9XNiz1C8uXyewYbK_CYNfsYXczXvRkgHgtx8urtrc; joowing-session-id=8bec860a70572b932010678e3fd3e6e2; login=chong.chen",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    request_url = f'''http://jmp.joowing.com/api/crm/database_agents/{org_code}/configs.json?page%5Bindex%5D=1&page%5Bsize%5D=20'''
    res = requests.get(request_url, headers=headers)
    if res.status_code == 200:
        print("请求成功！")
        decode_config = res.json()[0]
        print("数据解析成功！")
        return decode_config, res.status_code
    else:
        print("%s请求失败：" % org_code, res)
        return None, 0


def get_orgcode():
    db_name = 'database_service_maintenance'
    server, dbconfig, cursor = connect_master_copy_DB(db_name)
    sql = "SELECT org_code FROM retailer_configs WHERE database_type in ('sql_server','mysql') AND activated = '1' AND org_code NOT IN ('carrefour','babybear','lebaby_2');"
    cursor.execute(sql)
    org_codes_dict = cursor.fetchall()
    print("获取商户Code成功！")
    # 关闭数据库和SSH链接
    close_sshserver(server, dbconfig, cursor)
    return org_codes_dict


def write_xmlfile(connect_path, decode_config, org_code):
    org_code = org_code
    ConnType = decode_config['database_type']
    Host = decode_config['host']
    Port = decode_config['port']
    UserName = decode_config['username']
    Password = decode_config['password']
    # NAVICAT密码加密
    cipher = Navicat12Crypto()
    Password = cipher.EncryptStringForNCX(Password)
    database = decode_config['database']
    ConnectionName = org_code + '-' + database
    with open(connect_path, 'a+') as file:
        if ConnType == 'sql_server':
            write_text = f'''<Connection ConnectionName="{ConnectionName}" ProjectUUID="" ConnType="SQLSERVER" OraConnType="" ServiceProvider="Default" Host="{Host}" Port="{Port}" PortSpecified="true" Database="master" OraServiceNameType="" TNS="" MSSQLAuthenMode="SQLSERVER" MSSQLAuthenWindowsDomain="" DatabaseFileName="" UserName="{UserName}" Password="{Password}" SavePassword="true" SettingsSavePath="C:\\Users\\CC\\Documents\\Navicat\\SQL Server\Servers\\{database}" SessionLimit="0" Encoding="" TimeoutReconnection="false" TimeoutReconnectionInterval="240" MySQLCharacterSet="false" Compression="false" AutoConnect="false" NamedPipe="false" NamedPipeSocket="" OraRole="" OraOSAuthen="false" SQLiteEncrypt="false" SQLiteEncryptPassword="" SQLiteSaveEncryptPassword="false" UseAdvanced="false" SSL="false" SSL_Authen="false" SSL_PGSSLMode="REQUIRE" SSL_ClientKey="" SSL_ClientCert="" SSL_CACert="" SSL_Clpher="" SSL_PGSSLCRL="" SSL_WeakCertValidation="false" SSL_AllowInvalidHostName="false" SSL_PEMClientKeyPassword="" SSH="true" SSH_Host="222.73.36.230" SSH_Port="2002" SSH_UserName="chong.chen" SSH_AuthenMethod="PASSWORD" SSH_Password="C711D561A2D110FDD3082CD3B51502C7" SSH_SavePassword="true" SSH_PrivateKey="" SSH_Passphrase="E191AF42327478CC5F143EF279EC4D81" SSH_SavePassphrase="true" SSH_Compress="false" HTTP="false" HTTP_URL="" HTTP_PA="" HTTP_PA_UserName="" HTTP_PA_Password="" HTTP_PA_SavePassword="" HTTP_EQ="" HTTP_CA="" HTTP_CA_ClientKey="" HTTP_CA_ClientCert="" HTTP_CA_CACert="" HTTP_CA_Passphrase="" HTTP_Proxy="" HTTP_Proxy_Host="" HTTP_Proxy_Port="" HTTP_Proxy_UserName="" HTTP_Proxy_Password="" HTTP_Proxy_SavePassword=""/>'''
            file.write('\t')
            file.write(write_text)
            file.write('\n')
        elif ConnType == 'mysql':
            write_text = f'''<Connection ConnectionName="{ConnectionName}" ProjectUUID="" ConnType="MYSQL" OraConnType="" ServiceProvider="Default" Host="{Host}" Port="{Port}" Database="" OraServiceNameType="" TNS="" MSSQLAuthenMode="" MSSQLAuthenWindowsDomain="" DatabaseFileName="" UserName="{UserName}" Password="{Password}" SavePassword="true" SettingsSavePath="C:\\Users\\CC\\Documents\\Navicat\\SQL Server\Servers\\{database}" SessionLimit="0" Encoding="0" Keepalive="false" KeepaliveInterval="240" MySQLCharacterSet="true" Compression="false" AutoConnect="false" NamedPipe="false" NamedPipeSocket="" OraRole="" OraOSAuthen="false" SQLiteEncrypt="false" SQLiteEncryptPassword="" SQLiteSaveEncryptPassword="false" UseAdvanced="false" SSL="false" SSL_Authen="false" SSL_PGSSLMode="REQUIRE" SSL_ClientKey="" SSL_ClientCert="" SSL_CACert="" SSL_Clpher="" SSL_PGSSLCRL="" SSL_WeakCertValidation="false" SSL_AllowInvalidHostName="false" SSL_PEMClientKeyPassword="" SSH="true" SSH_Host="222.73.36.230" SSH_Port="2002" SSH_UserName="chong.chen" SSH_AuthenMethod="PASSWORD" SSH_Password="C711D561A2D110FDD3082CD3B51502C7" SSH_SavePassword="true" SSH_PrivateKey="" SSH_Passphrase="E191AF42327478CC5F143EF279EC4D81" SSH_SavePassphrase="true" SSH_Compress="false" HTTP="false" HTTP_URL="" HTTP_PA="" HTTP_PA_UserName="" HTTP_PA_Password="" HTTP_PA_SavePassword="" HTTP_EQ="" HTTP_CA="" HTTP_CA_ClientKey="" HTTP_CA_ClientCert="" HTTP_CA_CACert="" HTTP_CA_Passphrase="" HTTP_Proxy="" HTTP_Proxy_Host="" HTTP_Proxy_Port="" HTTP_Proxy_UserName="" HTTP_Proxy_Password="" HTTP_Proxy_SavePassword=""/>'''
            file.write('\t')
            file.write(write_text)
            file.write('\n')
    return 0


if __name__ == '__main__':
    connect_path = r"C:\Users\LyyCc\Desktop\connections.ncx"
    org_codes_dict_list = get_orgcode()
    print(org_codes_dict_list)
    wrirte_begin_xml(connect_path)
    for org_code in org_codes_dict_list:
        decode_config, status_code = decode_configs(org_code['org_code'])
        if status_code == 200:
            write_xmlfile(connect_path, decode_config, org_code['org_code'])
        else:
            pass
    wrirte_end_xml(connect_path)
