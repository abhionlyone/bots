from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
import os
import datetime

def say(msg = "Finish", voice = "Victoria"):
    os.system(f'echo "{msg}"|espeak')
class PS5Bot():
    def __init__(self):
        say("Amazon PS5 is initiated")
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def login(self):
        self.driver.get('https://www.amazon.in')
        sleep(50)

    def checkAndBuyPS5(self):
        print(datetime.datetime.now())
        # IS4QUSXAD5WAN PS5
        # I2YD6TMH5K1GQG XBOX
        self.driver.get('https://www.amazon.in/hz/wishlist/ls/20CFY3QB7ICYC?ref_=wl_share')
        try:
            buyNow = self.driver.find_element_by_xpath('//*[@id="pab-IS4QUSXAD5WAN"]')
            if buyNow.text == 'Add to Cart':
                buyNow.click()
            else:
                raise Exception(buyNow.text)
            n = 5
            while n > 0:
                say("Playstation is back in stock on Amazon.")
        except Exception as e:
            print(e)
            sleep(60)
            self.checkAndBuyPS5()

ps5bot = PS5Bot()
ps5bot.checkAndBuyPS5()