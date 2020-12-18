import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestTestdemo:
    def setup_method(self, method):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def test_testdemo(self):
        self.driver.get('https://www.baidu.com')

    def test_weixin(self):
        self.driver.find_element(By.ID, "menu_contacts").click()
        sleep(3)

    def test_cookie(self):
        # get_cookies()  可以获取当前打开的页面的cookies 信息
        # add_cookies()  可以把cookie 添加到当前的页面中去
        # cookies = self.driver.get_cookies()
        #  print(cookies)
        cookies = [
            {'domain': '.qq.com', 'expiry': 1608272858, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851925225482'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': '5ZVLmBrMGiPgEpooL431sJClFpHup3MxhdO26DzVKIzKcDwwrWXJd_eFNW7j2EIpwFvtur51IhSv6QH3kyOLHlgHbtaPTwKAPda5rAYry5KsrRhaoTaAAEh41A4VEr6XGMANG_HLSZ1KrVDh2Ylm5bp29u6liTxrIJ-0G-mOm2sLD0FD-tvxemFZcHD7rKDVnf_elkQxHW6pleOpFJmJrgphsaaDR0A-P79D6Kci4yZJPQ2OK3vJRCbI1GOZ5S9hS6FTFgW2g-fl10DLJ07QfQ'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851925225482'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325098167423'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'c03HXNcUhnkyEOn5pJi7JKsoENUwcmqOKm_1h3MjARmTMxLJEFreuygXBCIOSMnH'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a9943790'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1608304077, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '8fo32v1'},
            {'domain': '.qq.com', 'expiry': 1608359065, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.89068897.1608272556'},
            {'domain': '.qq.com', 'expiry': 1671344665, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1834163053.1608272556'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1639808541, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '01340889'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1608272555'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639808555, 'httpOnly': False,
                                  'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                                  'value': '1608272555'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1610864801, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '21dc3f852643e1016f445716664c3fa869808d834d170d4caf327415465a977b'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'SUzwfP2GGq'}]

        # refresh()  刷新页面
        self.driver.refresh()
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        sleep(3)

    def test_shelve(self):
        cookies = [
            {'domain': '.qq.com', 'expiry': 1608272858, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851925225482'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': '5ZVLmBrMGiPgEpooL431sJClFpHup3MxhdO26DzVKIzKcDwwrWXJd_eFNW7j2EIpwFvtur51IhSv6QH3kyOLHlgHbtaPTwKAPda5rAYry5KsrRhaoTaAAEh41A4VEr6XGMANG_HLSZ1KrVDh2Ylm5bp29u6liTxrIJ-0G-mOm2sLD0FD-tvxemFZcHD7rKDVnf_elkQxHW6pleOpFJmJrgphsaaDR0A-P79D6Kci4yZJPQ2OK3vJRCbI1GOZ5S9hS6FTFgW2g-fl10DLJ07QfQ'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851925225482'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325098167423'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'c03HXNcUhnkyEOn5pJi7JKsoENUwcmqOKm_1h3MjARmTMxLJEFreuygXBCIOSMnH'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a9943790'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1608304077, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '8fo32v1'},
            {'domain': '.qq.com', 'expiry': 1608359065, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.89068897.1608272556'},
            {'domain': '.qq.com', 'expiry': 1671344665, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1834163053.1608272556'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1639808541, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '01340889'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1608272555'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639808555, 'httpOnly': False,
                                  'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                                  'value': '1608272555'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1610864801, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '21dc3f852643e1016f445716664c3fa869808d834d170d4caf327415465a977b'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'SUzwfP2GGq'}]
        # shelve python 内置模块，专门用来对数据进行持久化存储的库，相当于小型的数据库
        # 可以通过key,value来被数据保存到shelve中
        # 读取cookie
        db = shelve.open("cookies")
        db['cookie'] = cookies
        db.close()

        # 利用读取的cookie , 完成登入操作
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        sleep(4)

        # 找到 “导入联系人” 按钮
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(2)').click()
        sleep(4)
        # 上传
        self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_uploadInputMask').send_keys(
            'E:\\mydata.xlsx')
        # 验证 上传文件名
        sleep(5)
        filename = self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_fileNames').text
        assert filename == 'mydata.xlsx'
