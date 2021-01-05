from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

ACCOUNT_EMAIL = "" 
ACCOUNT_PASSWORD = ""
SIMILAR_ACCOUNT = ""
chrome_driver_path = "C:\Development\chromedriver.exe"


class InstaFollower:
    def __init__(self, chrome_driver_path):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(3)
        cookie_accept = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]')
        cookie_accept.click()
        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        username.send_keys(ACCOUNT_EMAIL)
        password.send_keys(ACCOUNT_PASSWORD)
        sleep(1)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        # self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        sleep(3)
        search_account = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_account.send_keys(SIMILAR_ACCOUNT)
        sleep(2)
        acc_click = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]')
        sleep(1)
        acc_click.click()
        sleep(3)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_button.click()



# driver = webdriver.Chrome(executable_path=chrome_driver_path)


# driver.get("https://twitter.com/")


bot = InstaFollower(chrome_driver_path)
bot.login()
bot.find_followers()
bot.follow()
