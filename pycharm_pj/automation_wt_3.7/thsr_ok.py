# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestT1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome('D:\GitRoot\pros\Selenium\chromedriver\chromedriver_win32_104\chromedriver.exe')
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_t1(self):
    self.driver.get("https://www.thsrc.com.tw/")
    self.driver.set_window_size(1327, 708)
    self.driver.find_element(By.CSS_SELECTOR, ".swal2-confirm").click()
    self.driver.find_element(By.ID, "select_location01").click()
    dropdown = self.driver.find_element(By.ID, "select_location01")
    dropdown.find_element(By.XPATH, "//option[. = '台中']").click()
    self.driver.find_element(By.ID, "select_location02").click()
    dropdown = self.driver.find_element(By.ID, "select_location02")
    dropdown.find_element(By.XPATH, "//option[. = '台南']").click()
    self.driver.find_element(By.ID, "Departdate01").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) > .day:nth-child(7)").click()
    self.driver.find_element(By.ID, "outWardTime").click()
    self.driver.find_element(By.CSS_SELECTOR, ".timepicker-hour").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(5) > .hour:nth-child(2)").click()
    self.driver.find_element(By.ID, "start-search").click()
  
