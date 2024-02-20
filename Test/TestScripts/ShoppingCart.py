from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import unittest, time
import datetime
import os
import psutil
from ddt import ddt, data, idata, file_data, unpack

class ShoppingCart(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(15)
        cls.base_url = "https://www.google.com/"
        # cls.verificationErrors = []
        # cls.accept_next_alert = True
        cls.driver.get("https://www.costco.com")
        cls.driver.maximize_window()

    def test09_logIn(self):
        driver = self.driver
        signinLink = driver.find_element(By.XPATH,  "//a[text()='Sign In / Register']")
        driver.get("https://www.costco.com/LogonForm")
        driver.find_element(By.ID, "signInName").click();
        driver.find_element(By.ID, "signInName").send_keys("test+1@gmail.com");
        driver.find_element(By.ID, "password").click();
        driver.find_element(By.ID, "password").send_keys("Test@1234");
        driver.find_element(By.ID, 'next').submit

        time.sleep(5)
        self.assertEqual(driver.title, 'Sign In | Costco')

    def test01_AddToCart(self):
        driver = self.driver
        driver.find_element(By.ID, 'search-field').click()
        driver.find_element(By.ID, 'search-field').clear()
        driver.find_element(By.ID, 'search-field').send_keys('apple watch')
        driver.find_element(By.ID, 'formcatsearch').submit()
        driver.find_element(By.XPATH, '//*[@id=\"search-results\"]/div[3]/div[2]/div/div/div[2]/div[2]/a/div').click()
        driver.find_element(By.ID, 'addbutton-0').click()
        driver.find_element(By.ID, 'add-to-cart-btn').click()
        driver.find_element(By.LINK_TEXT, 'View Cart').click()

        self.assertEqual(driver.find_element(By.LINK_TEXT, 'Apple Watch Series 9 (GPS)').text,
                         'Apple Watch Series 9 (GPS)')
        self.assertEqual(driver.find_element(By.ID, 'quantity_1').get_attribute('value'), "1")

    def test02_ModifyCartItem_Increase(self):
        self.driver.find_element(By.ID, 'add-1').click()
        quantity = self.driver.find_element(By.ID, 'quantity_1')
        self.assertEqual(quantity.get_attribute('value'), '2')

    def test03_ModifyCartItem_Decrease(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id=\"sub-1\"]/img').click()
        quantity = self.driver.find_element(By.ID, 'quantity_1')
        self.assertEqual(quantity.get_attribute('value'), '1')

    def test04_CartBoundary(self):
        time.sleep(5)
        self.driver.find_element(By.ID, 'quantity_1').click()
        self.driver.find_element(By.ID, 'quantity_1').clear()
        self.driver.find_element(By.ID, 'quantity_1').send_keys('999')
        self.driver.find_element(By.ID, 'cart-body').click()

        inlineErrorMessage = self.driver.find_element(By.XPATH, '//*[@id="errquantity_"]/p[2]')

        self.assertEqual(inlineErrorMessage.text, 'Item 1698456 has a maximum order quantity of 2')
        self.driver.refresh()

    def test05_AddToList(self):
        time.sleep(4)
        self.driver.find_element(By.XPATH, '//*[@id="order-item_1"]/div/div[5]/div[1]/button[1]').click()

        time.sleep(5)
        self.assertEqual(self.driver.title, 'Sign In | Costco')
        self.driver.back()
        self.driver.back()
        self.driver.refresh()

    def test06_SaveForLater(self):
        self.driver.find_element(By.ID, 'cart-d').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="order-item_1"]/div/div[5]/div[1]/button[2]').click()
        time.sleep(3)
        self.assertEqual(self.driver.find_element(By.XPATH, '//*[@id="empty-cart-id"]/div[2]').text,
                         'Your shopping cart is empty. Please add at least one item to your cart before checking out.')
        self.assertEqual(self.driver.find_element(By.XPATH, '//*[@id="order-items-sfl"]/div[1]/h2').text,
                         'Saved for Later')
        self.assertEqual(self.driver.find_element(By.XPATH,
                                                  '//*[@id="sfl-items-container"]/div/div/div/div[1]/div/div/div[2]/div[1]/a').text,
                         'Apple Watch Series 9 (GPS)')
        self.assertEqual(self.driver.find_element(By.XPATH,
                                                  '//*[@id="sfl-items-container"]/div/div/div/div[3]/div[2]/div/button[2]').text,
                         'Move to Cart')

    def test07_RemoveFromSaveForLater(self):
        self.driver.find_element(By.XPATH,
                                 '//*[@id=\"sfl-items-container\"]/div/div/div/div[2]/div/div/div/div/button').click()
        self.driver.refresh()
        try:
            self.driver.find_element(By.XPATH, '//*[@id="order-item_1"]/div/div[5]/div[1]/button[2]').is_displayed()
            present = True
        except:
            present = False
        self.assertFalse(present, False)

    @classmethod
    def tearDownClass(cls):
        # try: self.driver.close()
        # except Exception as e:
        #     print(e)
        if (cls.driver != None):
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
