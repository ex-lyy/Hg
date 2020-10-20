# -*- encoding：utf-8 -*-
# 文件名称：Lyy-批量发优惠券尝试
# 作者:清许丶
# 谨记:遵守秩序，尊重选择。
# 创建时间：2020/9/7 下午 05:02

import requests
import json
import sys
import re, json
import tkinter.messagebox
import pymysql
from sshtunnel import SSHTunnelForwarder
from selenium import webdriver
import time
from multiprocessing import pool

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}

cookie = 'SESSION=d4cbc4e9-3424-4db2-80c2-c20d5f55ac1d; UM_distinctid=1741a499cd05c6-0caedca49aab0f-3323766-1fa400-1741a499cd1706; JSESSIONID=node0awx1c5m8zfce1fe9z7rprirwd555.node0; retailer-jwt=eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoianMxQGp3YmFieS5jb20iLCJ1c2VyX2F0dHJpYnV0ZXMiOnt9LCJleHAiOjE1OTk0NzUwNTh9.rq3LqWR-R7A1lJb543-RI_6T_YwLgWbZy9aDGiWsbNY; _newbee_session=BAh7DEkiD3Nlc3Npb25faWQGOgZFVEkiJTc1ZTQ4NjVjYmRmNDFkYzIyMjk2YzY4NTU3NDc4YTYzBjsAVEkiDHVzZXJfaWQGOwBGaQJH1UkiD2V4cGlyZXNfYXQGOwBGVTogQWN0aXZlU3VwcG9ydDo6VGltZVdpdGhab25lWwhJdToJVGltZQ3pIB7AaRRvlgk6DW5hbm9fbnVtaQJgAToNbmFub19kZW5pBjoNc3VibWljcm8iBzUgOgl6b25lSSIIVVRDBjsARkkiDEJlaWppbmcGOwBUSXU7Bw3xIB7AaRRvlgk7CGkCYAE7CWkGOwoiBzUgOwtJIghVVEMGOwBGSSINbmVidWxhLTMGOwBGVEkiEV9saXN0X2ZpbHRlcgY7AEZ7AEkiEl9saXN0X29wdGlvbnMGOwBGewBJIhBfY3NyZl90b2tlbgY7AEZJIjEzNG9kOW54T0R3K1ZBK3pLWEtiOEZIQ3ptVWd1VFdENWtEeDZnNWdBTTRVPQY7AEY%3D--9b43dd2bbfe897b0f66304d8118837a26a81081d; login=js1%40jwbaby.com; joowing-session=85acfcb7e5d5381cc51f852498d90d93; serial=%7B%22code%22%3A%22RUIBUEN_1%22%2C%22name%22%3A%22%E7%91%9E%E5%93%BA%E6%81%A9%E6%9C%89%E6%9C%BA%22%7D'
