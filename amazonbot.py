from selenium import webdriver
from time import sleep
import os

def say(msg = "Finish", voice = "Victoria"):
    os.system(f'say -v {voice} {msg}')

class PS5Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.amazon.in')
        sleep(50)

    def checkAndBuyPS5(self):
        self.driver.get('https://www.amazon.in/dp/B08FV5GC28')
        sleep(1)   
        try:
            buyNow = self.driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')
            buyNow.click()
            say("Playstation is back in stock.")
            sleep(1.5)
            self.checkAndBuyPS5()
        except Exception as e:
            sleep(300)
            self.checkAndBuyPS5()


class XboxBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.amazon.in')
        sleep(50)

    def checkAndBuyXbox(self):
        self.driver.get('https://www.amazon.in/dp/B08J7QX1N1/?coliid=I3M5N1MPCYZY7F&colid=353KMS360BV6I&psc=0&ref_=lv_ov_lig_dp_it')
        sleep(1)   
        try:
            buyNow = self.driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')
            buyNow.click()
            say("Xbox is back in stock.")
            sleep(1.5)
            self.checkAndBuyXbox()
        except Exception as e:
            sleep(300)
            self.checkAndBuyXbox()

ps5bot = PS5Bot()
ps5bot.checkAndBuyPS5()

xbot = XboxBot()
xbot.checkAndBuyXbox()