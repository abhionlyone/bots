from selenium import webdriver
from time import sleep
import os

def say(msg = "Finish", voice = "Victoria"):
    os.system(f'say -v {voice} {msg}')

class PS5Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def checkAndBuyPS5(self):
        self.driver.get('https://www.flipkart.com/sony-playstation-5-cfi-1008a01r-825-gb-astro-s-playroom/p/itma0201bdea62fa')
        sleep(1)   
        try:
            buyNow = self.driver.find_element_by_xpath('//button[text()="BUY NOW"]')
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

    def checkAndBuyXbox(self):
        self.driver.get('https://www.flipkart.com/microsoft-xbox-series-x-1024-gb/p/itm63ff9bd504f27')
        sleep(1)   
        try:
            buyNow = self.driver.find_element_by_xpath('//button[text()="BUY NOW"]')
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