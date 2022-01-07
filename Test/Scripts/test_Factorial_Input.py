import sys

sys.path.append(sys.path[0] + "/../..")

from TestBase.WebDriverSetup import main_driver
from PageObject.Pages.HomePage import Home
import unittest
from time import sleep
import numpy
import random



class Factorial_Input(main_driver):

    def test_Factorial_Input_1(self):
        """Test giving inputs from 0 to 170"""
        driver = self.driver
        self.driver.get("http://qainterview.pythonanywhere.com/")
        self.driver.set_page_load_timeout(30)

        # Create an instance of the class so that you we can make use of the methods
        # in the class
        home = Home(driver)

        # wait for page to load completely
        sleep(5)

        # click on the sign in tab
        for n in range(50):
            randomnumber = numpy.random.randint(170)
            home.input_box.send_keys(randomnumber)
            home.calculate_btn.click()
            result = home.getResult(driver)
            self.assertIn('The factorial of', result)
            home.input_box.clear()

        sleep(5)

    def test_Factorial_Input_2(self):
        """Test giving inputs from 171 to 989"""
        driver = self.driver
        self.driver.get("http://qainterview.pythonanywhere.com/")
        self.driver.set_page_load_timeout(30)

        # Create an instance of the class so that you we can make use of the methods
        # in the class
        home = Home(driver)
        for n in range(50):
            randomnumber = random.randrange(171, 989)
            home.input_box.send_keys(randomnumber)
            home.calculate_btn.click()
            result = home.getResult(driver)
            self.assertIn('Infinity', result)
            home.input_box.clear()

        sleep(5)

    def test_Factorial_Input_3(self):
        """Test giving inputs from 990 to 1200"""
        driver = self.driver
        self.driver.get("http://qainterview.pythonanywhere.com/")
        self.driver.set_page_load_timeout(30)

        # Create an instance of the class so that you we can make use of the methods
        # in the class
        home = Home(driver)
        for n in range(3):
            randomnumber = random.randrange(990, 1200)
            home.input_box.send_keys(randomnumber)
            home.calculate_btn.click()
            result = home.getResult(driver)
            home.input_box.clear()

        sleep(5)

if __name__ == '__main__':
    unittest.main()