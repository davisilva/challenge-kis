import sys

sys.path.append(sys.path[0] + "/../..")

from TestBase.WebDriverSetup import main_driver
import unittest


class Factorial_HomePage(main_driver):

    def test_Home_Page(self):
        """Test to verif if the Home Page was loaded successfully"""
        driver = self.driver
        self.driver.get("http://qainterview.pythonanywhere.com/")
        self.driver.set_page_load_timeout(30)

        web_page_title = "Factoriall"

        try:
            if driver.title == web_page_title:
                print("WebPage loaded successfully")
                self.assertEqual(driver.title, web_page_title)
        except Exception as error:
            print(error + "WebPage Failed to load")


if __name__ == '__main__':
    unittest.main()