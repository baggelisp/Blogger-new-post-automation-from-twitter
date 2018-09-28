from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class BloggerBot:

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        while True:
            try:
                self.driver.close()
                break
            except Exception as e:
                print (e)
                time.sleep(2)
                pass
        

    def login(self):
        driver = self.driver
        while True:
            try:
                driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fwww.blogger.com%2Fhome&ltmpl=blogger&service=blogger&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
                break
            except Exception as e:
                print (e)
                time.sleep(2)
                pass
        time.sleep(2)
        print ("Logging in...")
        time.sleep(2)
        while True:
            try:
                user_name_elem = driver.find_element_by_xpath(""" //*[@id="identifierId"] """)
                user_name_elem.clear()
                user_name_elem.send_keys(self.email)
                break
            except Exception as e:
                print (e)
                time.sleep(2)
                pass
        while True:
            try:
                next_button = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/content")
                next_button.click()
                break
            except Exception as e:
                print (e)
                time.sleep(2)
                pass
        time.sleep(4)
        while True:
            try:
                passworword_elem = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/content/section/div/content/div[1]/div/div[1]/div/div[1]/input")
                passworword_elem.clear()
                passworword_elem.send_keys(self.password)
                passworword_elem.send_keys(Keys.RETURN)
                break
            except Exception as e:
                print (e)
                time.sleep(2)
                pass
        print ("You logged in!")


            
    def new_post(self,post):
        
        driver = self.driver
        time.sleep(7)
        # ------ press new post -------
        while True:
            try:
                new_post_button = driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/div[1]/div[1]/a")
                new_post_button.click()
                break
            except Exception as e:
                print (e)
                pass
        time.sleep(8)
        # ------ write post -------
        while True:
            try:
                driver.find_element_by_xpath(""" /html """).click()
                entry=driver.find_element_by_xpath(""" //*[@id="postingComposeBox"] """)
                for letter in post:
                    entry.send_keys(letter)
                    time.sleep((random.randint(1, 5) / 200))
                break
            except Exception as e:
                print (e)
                pass        
        time.sleep(10)

        # ------ press post -------
        
        while True:
            try:
                post_button = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div/form/div[1]/span/button[1]")
                post_button.click()
                break
            except Exception as e:
                print (e)
                pass        
        time.sleep(6)        
       



                                                      
