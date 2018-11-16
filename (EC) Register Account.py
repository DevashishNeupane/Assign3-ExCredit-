import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        #driver.maximize_window()
        driver.get("http://devashish77.pythonanywhere.com/home/")
        elem = driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[2]/li/a").click()
        time.sleep(3)

        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/p[2]/a").click()
        time.sleep(3)

        elem = driver.find_element_by_id("id_username")
        elem.send_keys("Tomz")

        elem = driver.find_element_by_id("id_first_name")
        elem.send_keys("Brady")

        elem = driver.find_element_by_id("id_email")
        elem.send_keys("theBrady@gmail.com")

        elem = driver.find_element_by_id("id_password")
        elem.send_keys("oklahomacity7")

        elem = driver.find_element_by_id("id_password2")
        elem.send_keys("oklahomacity7")

        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/p[6]/input").click()
        time.sleep(2)

        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/p/a").click()
        time.sleep(3)

        elem = driver.find_element_by_id("id_username")
        elem.send_keys("Tomz")

        elem = driver.find_element_by_id("id_password")
        elem.send_keys("oklahomacity7")

        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/input[2]").click()

        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
