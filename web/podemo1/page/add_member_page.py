import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.podemo1.page.base_page import BasePage


class AddMemberPage(BasePage):
    #
    # def __init__(self, driver:WebDriver):
    #     self.driver = driver

    def add_member(self, username, account, phonenum):
        # 添加联系人
        # username= 'aaaaaaa'
        # account = 'aaaaaa__hogwarts'
        # phonenum = '13200000000'
        time.sleep(2)
        # self.driver.find_element(By.ID, 'username').send_keys(username)
        # self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys(account)
        # self.driver.find_element(By.ID, 'memberAdd_phone').send_keys(phonenum)
        # self.driver.find_element(By.CSS_SELECTOR,'.js_btn_save').click()

        self.find(By.ID, 'username').send_keys(username)
        self.find(By.ID, 'memberAdd_acctid').send_keys(account)
        self.find(By.ID, 'memberAdd_phone').send_keys(phonenum)
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        # time.sleep(2)

        checkbox = (By.CSS_SELECTOR, '.ww_checkbox')
        self.wait_for_click(checkbox)

        return True

    def get_member(self, value):
        # 验证联系人是否添加成功

        # 方法一：只验证第一页
        # contactlist = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        # titlelist = [element.get_attribute("title") for element in contactlist]

        # titlelist = []
        # for element in contactlist:
        #     titlelist.append(element.get_attribute("title"))

        # # 方法二：验证所有页面的数据
        # total_list = []
        # while True:
        #     contactlist = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        #     titlelist = [element.get_attribute("title") for element in contactlist]
        #     total_list = total_list + titlelist
        #
        #     result:str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
        #     num , total = result.split('/', 1)
        #     if int(num) == int(total):
        #         break
        #     else:
        #         self.find(By.CSS_SELECTOR, '.ww_commonImg_PageNavArrowRightNormal').click()

        # 方法三：获取到对应的数据就返回，不需要查找到所有的页面数据，传参value,是本次新增的用户名

        while True:
            contactlist = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            titlelist = [element.get_attribute("title") for element in contactlist]

            if value in titlelist:
                return True

            result: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
            num, total = result.split('/', 1)
            if int(num) == int(total):
                return False
            else:
                self.find(By.CSS_SELECTOR, '.ww_commonImg_PageNavArrowRightNormal').click()

        # return total_list
