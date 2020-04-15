# Selenium ouo.io automation

# Python Natives
import time

# Selenium Driver
from selenium import webdriver

#Selenium Elements
from selenium.webdriver.common.keys import Keys

# Selenium Exceptions
from selenium.common.exceptions import NoSuchElementException

import re

import random

class Selenium_Manager :
    
    def __init__ (self) :
        self.driver = webdriver.Firefox()
        
    def go_url (self, **kwargs):

        try:
            self.driver.get(kwargs.pop('url'))
        except :
            print  ("Cannot acced to this page.")

    def xpath_click() :
        pass

    def xpath_input_text(self, element, text, Enter=False) :
        if isinstance(element, list) :
            for item in element :
                try:
                    target = self.driver.find_element_by_xpath(item)
                    time.sleep(1)
                    try:
                        target.clear()
                    except:
                        pass
                    if (Enter == True) :
                        import pdb; pdb.set_trace()
                        target.send_keys(text + Keys.RETURN)
                    else :
                        target.send_keys(text)
                    return True
                except NoSuchElementException:
                    continue

            return False

    def refresh() :
        pass


class ouoio  :

    def __init__ (self, **kwargs):
        try :
            self.url = kwargs.pop('url')
        except :
            print ("No url sended")
        try:
            self.controller = kwargs.pop('web')
        except:
            print ("No webdriver sended.")

    def ProcessLink (self, Link) :
        self.controller.go_url(url=Link)
        time.sleep(random.randrange(1, 3))
        self.controller.driver.execute_script('''document.getElementById("form-captcha").submit(); ''')
        time.sleep(15) 
        self.controller.driver.execute_script('''document.getElementById("form-go").submit(); ''')
        time.sleep(random.randrange(1, 3))
  

    def start(self, **kwargs):
        Links = kwargs.get('data')
        for Link in Links :
            self.ProcessLink(Link)
            if (self.controller.driver.current_url == Link) :
                print("Repeating because link isn't same")
                time.sleep(random.randrange(1, 3))
                self.ProcessLink(Link)

            with open(OutputFile, 'a') as file:
                time.sleep(random.randrange(1, 3))
                file.write(self.controller.driver.current_url + "\n")
                file.close()


Web = Selenium_Manager()
Plugin_ouoio = ouoio(url="https://ouo.io/", web=Web)
AllLinks_from_txt = open('links.txt', 'r').read()
LinkList = []
for url in re.findall('(https://\S+)', AllLinks_from_txt): LinkList.append(url)
OutputFile='output.txt' 
Plugin_ouoio.start(data=LinkList)
