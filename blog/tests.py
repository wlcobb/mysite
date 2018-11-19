from django.test import TestCase


import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "wcobb@unomaha.edu"
        time.sleep(5)
        pwd = "Fancyface#1"
        time.sleep(15)
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem: WebElement = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"
        time.sleep(15)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/h2[1]/a").click()
        #this clicks a post.
        time.sleep(15)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/p[3]/a").click()
        #this clicks on the share post button
        time.sleep(15)
        elem = driver.find_element_by_id("id_name")
        #this enters the na,e of who to send to
        elem.send_keys("This is a test post with selenium")
        elem = driver.find_element_by_id("id_email")
        #this enters email of who it is coming from
        elem.send_keys("test@gmail.com")
        time.sleep(15)
        elem = driver.find_element_by_id("id_to")
        #this enters the email to who it is going to.  There is an error shown with no @
        elem.send_keys("John Doe")
        time.sleep(15)
        elem = driver.find_element_by_id("id_comments")
        #this is the comment to send.
        elem.send_keys("test for activity 7")
        time.sleep(15)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/input[2]").click()
        time.sleep(15)
        #this sends the email of the shared blod
        assert "Blog was shared"
        driver.get("http://127.0.0.1:8000")
        time.sleep(15)
        driver.get("http://127.0.0.1:8000")


        def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()
