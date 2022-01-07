import sys

sys.path.append(sys.path[0] + "/../..")

from TestBase.WebDriverSetup import main_driver
from PageObject.Pages.HomePage import Home
import unittest



class Factorial_Links(main_driver):
    def test_Factorial_Links(self):
        """Test to verify if the hyperlinks are correct"""
        driver = self.driver
        self.driver.get("http://qainterview.pythonanywhere.com/")
        self.driver.set_page_load_timeout(30)

        # Create an instance of the class so that you we can make use of the methods
        # in the class
        home = Home(driver)
        self.assertEqual(home.terms_link.get_attribute('href'), 'http://qainterview.pythonanywhere.com/terms')
        self.assertEqual(home.privacy_link.get_attribute('href'), 'http://qainterview.pythonanywhere.com/privacy')





if __name__ == '__main__':
    unittest.main()