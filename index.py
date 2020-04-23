from selenium import webdriver
import os
import unittest
from selenium.webdriver.common.keys import Keys


class facebook(unittest.TestCase):
    def test_log(self):
        driver = webdriver.Chrome()
        driver.get("http://www.facebook.com/")
        input1 = driver.find_element_by_id("email")
        input2 = driver.find_element_by_id("pass")
        bton = driver.find_element_by_id("u_0_b")
        input1.send_keys(os.environ['EMAIL'])
        input2.send_keys(os.environ['PASS'])
        bton.click()
        assert "Home" in driver.page_source
        driver.close()
if __name__ == '__main__': 
    unittest.main() 