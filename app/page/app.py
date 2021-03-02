"""
    app.py 模块，存放app相关的一些操作
    比如 应用启动，重启应用，停止应用，进入到首页
"""
import yaml
from appium import webdriver

from app.page.MainPage import MainPage
from app.page.base_page import BasePage

with open("../datas/caps.yml") as f:

    myconfig = yaml.safe_load(f)
    caps = myconfig['desirecaps']
    ip = myconfig['server']['ip']
    port = myconfig['server']['port']



class App(BasePage):
    def start(self):
        # 启动app
        if self.driver == None:
            # caps = {}
            # caps["platformName"] = "Android"
            # caps["platformVersion"] = "6.0"
            # caps["deviceName"] = "hogwarts"
            # caps["appPackage"] = "com.tencent.wework"
            # caps["appActivity"] = ".launch.LaunchSplashActivity"
            # # noReset 保留缓存， 比如登入状态
            # caps["noReset"] = "True"
            # # 不停止应用，执行运行测试用例
            # # caps['dontStopAppOnReset'] = "true"
            # # 跳过设备初始化
            # caps['skipDeviceInitialization'] = 'true'
            # # 跳过server安装
            # caps['skipServerInstallation'] = 'true'

            # setting 可以设置在开始，也可以设置在中间部分
            # caps["settings[waitForIdleTimeout]"] = 0
            # 关键    localhost:4723   本机ip:server端口



            self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        # 重启app
        self.driver.close_app()
        self.driver.launch_app()
        pass

    def stop(self):
        # 停止app
        self.driver.quit()

    def goto_main(self)->MainPage:
        # 进入到首页
        return MainPage(self.driver)