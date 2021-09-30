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
        self.driver.get('https://www.amazon.in/dp/B08FV5GC28')
        sleep(1)   
        try:
            buyNow = self.driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')
            buyNow.click()
            n = 5
            while n > 0:
                say("Playstation is back in stock on Amazon.")
        except Exception as e:
            sleep(300)
            self.checkAndBuyPS5()


class XboxBot():
    def __init__(self):
        say("Amazon Xbox is initiated")
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def login(self):
        self.driver.get('https://www.amazon.in')
        sleep(50)

    def checkAndBuyXbox(self):
        print(datetime.datetime.now())
        self.driver.get('https://www.amazon.in/dp/B08J7QX1N1/?coliid=I3M5N1MPCYZY7F&colid=353KMS360BV6I&psc=0&ref_=lv_ov_lig_dp_it')
        sleep(1)   
        try:
            buyNow = self.driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')
            buyNow.click()
            n = 5
            while n > 0:
                say("Xbox is back in stock on Amazon.")
        except Exception as e:
            sleep(300)
            self.checkAndBuyXbox()

sleep(10)

xbot = XboxBot()
xbot.checkAndBuyXbox()