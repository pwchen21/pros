# Generated by Selenium IDE
import pytest
import time
import json
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestUntitled():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_untitled(self):
    self.driver.get("https://www.thsrc.com.tw/")
    self.driver.save_screenshot('test.jpg')
    self.element = driver.find_element_by_id('BookingS1Form_homeCaptcha_passCode')
    self.element.location
    self.element.size
    self.left = element.location['x']
    self.right = element.location['x'] + element.size['width']
    self.top = element.location['y']
    self.bottom = element.location['y'] + element.size['height']
    self.img
    self.driver.set_window_size(1382, 744)
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, "#aIRS img").click()
    self.vars["win6113"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win6113"])
    self.driver.find_element(By.NAME, "selectStartStation").click()
    dropdown = self.driver.find_element(By.NAME, "selectStartStation")
    dropdown.find_element(By.XPATH, "//option[. = '南港']").click()
    self.driver.find_element(By.NAME, "selectDestinationStation").click()
    dropdown = self.driver.find_element(By.NAME, "selectDestinationStation")
    dropdown.find_element(By.XPATH, "//option[. = '台中']").click()
    self.driver.find_element(By.ID, "toTimeInputField").click()
    self.driver.find_element(By.ID, "toTimeInputField").send_keys("2022/05/30")
    self.driver.find_element(By.NAME, "toTimeTable").click()
    dropdown = self.driver.find_element(By.NAME, "toTimeTable")
    dropdown.find_element(By.XPATH, "//option[. = '17:30']").click()
    self.driver.find_element(By.NAME, "ticketPanel:rows:0:ticketAmount").click()
    dropdown = self.driver.find_element(By.NAME, "ticketPanel:rows:0:ticketAmount")
    dropdown.find_element(By.XPATH, "//option[. = '2']").click()
    self.driver.find_element(By.ID, "securityCode").click()
    self.driver.find_element(By.ID, "securityCode").send_keys("HRM4")
    self.driver.find_element(By.ID, "SubmitButton").click()
    self.driver.execute_script("window.scrollTo(0,200)")
    self.driver.find_element(By.NAME, "SubmitButton").click()
    self.driver.find_element(By.ID, "idNumber").click()
    self.driver.find_element(By.ID, "idNumber").send_keys("A123456789")
    self.driver.find_element(By.ID, "mobilePhone").click()
    self.driver.find_element(By.ID, "mobilePhone").send_keys("0912345678")
    self.driver.find_element(By.ID, "name2622").click()
    self.driver.find_element(By.ID, "name2622").send_keys("Test@gmail.com")
  
