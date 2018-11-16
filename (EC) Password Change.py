import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "Michael"
        pwd = "oklahoma7"
        driver = self.driver
        #driver.maximize_window()
        driver.get("http://devashish77.pythonanywhere.com/home/")
        elem = driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[2]/li/a").click()

        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        #driver.get("http://mavsystems.pythonanywhere.com/admin/")
        assert "Logged In"
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a").click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("//*[@id=\"PChange\"]").click()
        time.sleep(5)

        elem = driver.find_element_by_id("id_old_password")
        elem.send_keys("oklahoma7")
        time.sleep(2)

        elem = driver.find_element_by_id("id_new_password1")
        elem.send_keys("oklahomacitythunder1")
        time.sleep(2)

        elem = driver.find_element_by_id("id_new_password2")
        elem.send_keys("oklahomacitythunder1")
        time.sleep(2)

        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/p[5]/input").click()
        time.sleep(2)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
