from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestWX:

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "6.0"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # noReset 保留缓存， 比如登入状态
        caps["noReset"] = "True"
        # 不停止应用，执行运行测试用例
        # caps['dontStopAppOnReset'] = "true"
        # 跳过设备初始化
        caps['skipDeviceInitialization'] = 'true'
        # 跳过server安装
        caps['skipServerInstallation'] = 'true'

        # setting 可以设置在开始，也可以设置在中间部分
        # caps["settings[waitForIdleTimeout]"] = 0
        # 关键    localhost:4723   本机ip:server端口
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_contact(self):
        name = "hogwarts_002"
        gender = "男"
        phonenum = "13500000002"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 两种方法
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.TextView").send_keys(name)
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(name)
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'性别')]/..//*[@text='男']").click()

        if gender == "男":
            WebDriverWait(self.driver, 10).until(lambda x:x.find_element(MobileBy.XPATH, "//*[@text='女']"))
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'手机') and contains(@class,'android.widget.TextView')]/..//android.widget.EditText").send_keys(phonenum)
        # 功能同上
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机号')]").send_keys(phonenum)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()

        sleep(2)
        # 打印返回页面
        # print(self.driver.page_source)

        # toast 验证
        # toast 正常是获取不到的，但有隐式等待可以获取到
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert '添加成功' == result


