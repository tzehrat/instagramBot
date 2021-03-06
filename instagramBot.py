from main import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Instagram():
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def sıgnIn(self):

        self.browser.get('https://www.instagram.com/accounts/login/?hl=tr')
        time.sleep(3)
        usernameInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(3)

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        followersLink = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(3)
        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followerCount = len(dialog.find_elements_by_css_selector("li"))
        print(f"firs count {followerCount}")
        action = webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(3)
            newCount = len(dialog.find_elements_by_css_selector("li"))
            break

            if followerCount != newCount:
                followerCount = newCount
                print(f"upload count {newCount}")
                time.sleep(3)
            else:
                break

        followers = dialog.find_elements_by_css_selector("li")

        for user in followers:
            user = self.browser.find_element_by_css_selector("a").get_attribute("href")
            print(user)


a = Instagram(username, password)

a.sıgnIn()
a.getFollowers()
