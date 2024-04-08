from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options

dir_path = os.getcwd()
chrome_options2 = Options()
chrome_options2.add_argument(r"user-data-dir=" + dir_path + "profile/zap")
driver = webdriver.Chrome(chrome_optations=chrome_options2)
driver.get('https://web.whatsapp.com/')
time.sleep(120)


class WhatsappBot:
    def__init__(self):
        self.mensagem = 'Bom dia, guys'
        self.grupos = ['Reunião familia']
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
       self.driver.get('https://web.whatsapp.com/')
       time.sleep(30)
       for group in self.groups:
        group = self.driver.find_element_by_xpath(f"//atributo[@title='{group}']")
        time.sleep(3)
        group.click()
        chat_box = self.driver.find_elements_by_class_name() 
        time.sleep(3)
        chat_box.click()
        chat_box.send_keys(self.mensagem)
        button_send = self.driver.find_element_by_xpath('//atributo[@propriedade="valor"]')
        time.sleep(3)
        button_send.click()
        time.sleep(5)

bot = WhatsappBot()
bot.EnviarMensagens()
