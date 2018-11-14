import csv
from selenium import webdriver
File = "Service_Info.csv"
import unittest
import time
from selenium.webdriver.common.keys import Keys

def insert_values():

    my_list = read_mpg()

    driver = webdriver.Chrome()
    user = "instructor"
    pwd = "instructor1a"
    #driver = self.driver
    # driver.maximize_window()
    driver.get("http://devashish77.pythonanywhere.com/home/")
    elem = driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[2]/li/a").click()

    elem = driver.find_element_by_id("id_username")
    elem.send_keys(user)
    elem = driver.find_element_by_id("id_password")
    elem.send_keys(pwd)
    elem.send_keys(Keys.RETURN)
    # driver.get("http://mavsystems.pythonanywhere.com/admin/")
    assert "Logged In"
    time.sleep(2)
    elem = driver.find_element_by_xpath(
        "//*[@id=\"app-layout\"]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[2]/a").click()
    time.sleep(3)
    elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[3]/div/a/span").click()
    time.sleep(3)

    for i in range(0, len(my_list)):
        service = my_list[i][0]
        description = my_list[i][1]
        location = my_list[i][2]
        service_charge = my_list[i][3]

    elem = driver.find_element_by_xpath("//*[@id=\"id_cust_name\"]/option[2]").click()

    elem = driver.find_element_by_id("id_service_category")
    elem.send_keys(service)

    elem = driver.find_element_by_id("id_description")
    elem.send_keys(description)

    elem = driver.find_element_by_id("id_location")
    elem.send_keys(location)

    elem = driver.find_element_by_id("id_service_charge")
    elem.send_keys(service_charge)

    elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/button").click()
    time.sleep(4)



def read_mpg():
    my_list = []
    with open(File, newline="") as Customer_File:
        reader = csv.reader(Customer_File)
        for each_row in reader:
            my_list.append(each_row)

    return my_list


insert_values()