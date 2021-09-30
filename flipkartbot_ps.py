from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
import os
import threading
import datetime

def say(msg = "Finish", voice = "Victoria"):
    os.system(f'echo "{msg}"|espeak')

class PS5Bot():
    def __init__(self):
        say("Flipkart Ps5 is initiated")
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def checkAndBuyPS5(self):
        print(datetime.datetime.now())
        self.driver.get('https://www.flipkart.com/sony-playstation-5-cfi-1008a01r-825-gb-astro-s-playroom/p/itma0201bdea62fa')
        sleep(1)   
        try:
            buyNow = self.driver.find_element_by_xpath('//button[text()="BUY NOW"]')
            buyNow.click()
            n = 5
            while n > 0:
                say("Playstation is back in stock on Flipkart.")
        except Exception as e:
            sleep(300)
            self.checkAndBuyPS5()


class XboxBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def checkAndBuyXbox(self):
        self.driver.get('https://www.flipkart.com/microsoft-xbox-series-x-1024-gb/p/itm63ff9bd504f27')
        sleep(1)   
        try:
            buyNow = self.driver.find_element_by_xpath('//button[text()="BUY NOW"]')
            buyNow.click()
            n = 5
            while n > 0:
                say("Xbox is back in stock on Flipkart.")
        except Exception as e:
            sleep(300)
            self.checkAndBuyXbox()

sleep(20)

ps5bot = PS5Bot()
ps5bot.checkAndBuyPS5()