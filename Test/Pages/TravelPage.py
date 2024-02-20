
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TravelPage():
    def __init__(self, driver):
        self.driver = driver

    # Locator
    DEST_FROM_FIELD = 'hotelDestination'
    CHECK_IN_FIELD = 'checkInDateWidget'
    CHECK_OUT_FIELD = 'checkOutDateWidget'
    ADULT_FIELD = 'hotelAdultsInRoomForWidget_1'
    CHILD_FIELD = 'hotelChildrenInRoomForWidget_1'
    CHILD1_AGE_FIELD = 'hotelChildAgeForWidget_1_1'
    CHILD2_AGE_FIELD = 'hotelChildAgeForWidget_1_2'
    CHILD3_AGE_FIELD = 'hotelChildAgeForWidget_1_3'
    SEARCH_FIELD = '//*[@id="ageAndSubmitDiv"]/div[2]/button'

    def getDestinationFromField(self):
        return self.driver.find_element(By.ID, self.DEST_FROM_FIELD)

    def enterDestination(self, destination):
        self.getDestinationFromField().click()
        self.getDestinationFromField().send_keys(destination)
        self.getDestinationFromField().send_keys(Keys.ENTER)
        time.sleep(1)

    def getCheckInFromField(self):
        return self.driver.find_element(By.ID, self.CHECK_IN_FIELD)

    def enterCheckIn(self, checkindate):
        self.getCheckInFromField().click()
        self.getCheckInFromField().send_keys(checkindate)

    def getCheckOutFromField(self):
        return self.driver.find_element(By.ID, self.CHECK_OUT_FIELD)

    def enterCheckOut(self, checkoutdate):
        self.getCheckOutFromField().click()
        self.getCheckOutFromField().send_keys(checkoutdate)

    def getAdultField(self):
        return self.driver.find_element(By.ID, self.ADULT_FIELD)

    def enterAdult(self, numofadult):
        self.getAdultField().click()
        self.getAdultField().send_keys(numofadult)

    def getChildField(self):
        return self.driver.find_element(By.ID, self.CHILD_FIELD)

    def enterChild(self, numofchild):
        self.getChildField().click()
        self.getChildField().send_keys(numofchild)

    def getChildAge1FromField(self):
        return self.driver.find_element(By.ID, self.CHILD1_AGE_FIELD)
    def enterChildAge1(self, childage1):
        self.getChildAge1FromField().click()
        self.getChildAge1FromField().send_keys(childage1)

    def getChildAge2FromField(self):
        return self.driver.find_element(By.ID, self.CHILD2_AGE_FIELD)
    def enterChildAge2(self, childage2):
        self.getChildAge2FromField().click()
        self.getChildAge2FromField().send_keys(childage2)

    def getChildAge3FromField(self):
        return self.driver.find_element(By.ID, self.CHILD3_AGE_FIELD)

    def enterChildAge3(self, childage3):
        self.getChildAge3FromField().click()
        self.getChildAge3FromField().send_keys(childage3)

    def getSearchButtonFromField(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_FIELD)
    def clicksearch(self):
        self.getSearchButtonFromField().click()
        # self.driver.execute_script("arguments[0].click();", search)

    def searchHotel(self, dest, checkindate, checkoutdate, adult, child, childage1, childage2, childage3):
        self.enterDestination(dest)
        self.enterCheckIn(checkindate)
        self.enterCheckOut(checkoutdate)
        self.enterAdult(adult)
        self.enterChild(child)
        self.enterChildAge1(childage1)
        self.enterChildAge2(childage2)
        self.enterChildAge3(childage3)
        self.clicksearch()
        self.driver.refresh()
        # time.sleep(4)
