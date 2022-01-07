import sys

sys.path.append(sys.path[0] + "/....")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObject.Locators import HomePageLocators


class Home(object):
    def __init__(self, driver):
        self.driver = driver
        self.input_box = driver.find_element(By.ID, HomePageLocators.input_box)
        self.calculate_btn = driver.find_element(By.ID, HomePageLocators.calculate_btn)
        self.terms_link = driver.find_element(By.CSS_SELECTOR, HomePageLocators.terms_link)
        self.privacy_link = driver.find_element(By.CSS_SELECTOR, HomePageLocators.privacy_link)

    def getResult(self, driver):
        result_text = WebDriverWait(driver, 30).until(EC.presence_of_element_located
                                                      ((By.XPATH, HomePageLocators.result_text)))
        return result_text.get_attribute("textContent")
