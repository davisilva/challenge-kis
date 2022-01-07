import unittest
from selenium import webdriver
import urllib3
from webdriver_manager.chrome import ChromeDriverManager


class main_driver(unittest.TestCase):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
