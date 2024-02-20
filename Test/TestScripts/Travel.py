import psutil
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
from ddt import ddt, data, unpack
from Test.Utilities.utils import Utils
import datetime
from Test.Pages.TravelPage import TravelPage


@ddt
class TestTravel(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.base_url = "https://www.google.com/"
        # cls.verificationErrors = []
        # cls.accept_next_alert = True
        cls.driver.get("https://www.costco.com/")
        cls.driver.maximize_window()

    @data(*Utils.read_data_from_csv('/Users/mimi/PycharmProjects/pythonProject/Test/TestScripts/travelDetails.csv'))
    @unpack
    def test08_Travel(self, dest, checkindate, checkoutdate, adult, child, childage1, childage2, childage3):
        self.driver.find_element(By.ID, 'Home_Ancillary_8').click()
        time.sleep(3)
        self.driver.find_element(By.ID, 'hotels-tab-id').click()
        time.sleep(3)
        travelpage = TravelPage(self.driver)
        travelpage.searchHotel(dest, checkindate, checkoutdate, adult, child, childage1, childage2, childage3)

        # noinspection PyBroadException
        try:
            loading_image = self.driver.find_element(By.CSS_SELECTOR, 'img.Screen is Loading')
            self.driver.execute_script("arguments[0].click();", loading_image)
            loading_image.is_enabled()
            present = True
        except:
            present = False
            print("Loading screen has issue")
        self.assertFalse(present, False)

    @classmethod
    def tearDownClass(cls):
        # try: self.driver.close()
        # except Exception as e:
        #     print(e)
        if cls.driver != None:
            print('===========================================')
            print('Test Environment Destroyed')
            print("Run completed at: " + str(datetime.datetime.now()))
            cls.driver.quit()

    # solutions to kill the dangling instances
    PROCNAME = "chromedriver"
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROCNAME:
            proc.kill()


if __name__ == "__main__":
    unittest.main()