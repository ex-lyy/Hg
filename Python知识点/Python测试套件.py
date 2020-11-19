# -*- coding:utf-8 -*-
# 文件名称：Lyy-test20201026001
# 作者:清许丶
# 谨记:遵守秩序，尊重选择。
# 创建时间：2020/10/26 18:00

import unittest
import requests
import HTMLTestRunner


class logintest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://nb3.joowing.com/nebula/v3/promotion/coupon_definitions.json?coupon_type=mall&display_in_list=1&org_code=wanpf&page%%5Bindex%%5D=1&page%%5Bsize%%5D=1000&state=online'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36', 'Cookie': 'id5AA=c5/nn1vC8o4vZul8i2zJAg==; Hm_lvt_b4a22b2e0b326c2da73c447b951236d6746=1539760959; xxzl_deviceid=F 3hTrG /V/iuVTvmXAxCandrfhokre4OxgMOfI7Tgxtvi1aO/IsvAfVCg7v1KEn;;_newbee_session=9a8283ce474d8d9b5c705c16b0957ad4;joowing-session-id=9a8283ce474d8d9b5c705c16b0957ad4;retailer-staff-jwt=eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MzgzNTYsIm5hbWUiOiJqczFAd2FucGYuY29tIiwibmlja19uYW1lIjoi5oqA5pyvMS3njqnnmq7lnYoiLCJubyI6IkpXMDAxIiwicGhvbmUiOiIxMjM0NTY3ODkwIiwidHlwZSI6Impvb3dpbmctc3RhZmYiLCJvcmdfaWQiOjg3LCJvcmdfY29kZSI6IndhbnBmIiwicmV0YWlsZXJfaWQiOjg3LCJyZXRhaWxlcl9jb2RlIjoid2FucGYiLCJleHAiOjE2MDM4NzQ1MjB9.kNpQjPNFX6e2G8umZHbmOxwBzfXjBzHnRCd60Po48K0'}


    def testlogin1(self):
        r = requests.get(self.url, headers = self.headers)
        self.assertEqual(r.status_code, 200)


def suite():
    loginTestCase = unittest.TestSuite()
    loginTestCase.addTest(logintest("testlogin1"))
    return loginTestCase

#
# if __name__ == "__main__":
#     fr = open(r"C:\Users\LyyCc\Desktop\res1.html","wb")
#     # runner = unittest.TextTestRunner()
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fr,title="测试报告",description="详情")
#     runner.run(suite())
#     fr.close()



fr = open(r"C:\Users\LyyCc\Desktop\res1.html","wb")
# runner = unittest.TextTestRunner()
runner = HTMLTestRunner.HTMLTestRunner(stream=fr,title="测试报告",description="详情")
runner.run(suite())
fr.close()