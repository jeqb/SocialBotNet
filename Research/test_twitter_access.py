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

class TestCreateTest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_createTest(self):
    self.driver.get("https://twitter.com/")
    self.driver.set_window_size(945, 1020)
    self.driver.find_element(By.CSS_SELECTOR, ".css-4rbku5:nth-child(4) > .css-901oao > .css-901oao > .css-901oao").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".css-4rbku5:nth-child(4) > .css-901oao > .css-901oao > .css-901oao")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.NAME, "name").send_keys("MyCoolName")
    self.driver.find_element(By.NAME, "phone_number").click()
    self.driver.find_element(By.NAME, "phone_number").send_keys("4804869945")
    self.driver.find_element(By.CSS_SELECTOR, ".css-1dbjc4n:nth-child(1) > .css-1dbjc4n > .r-30o5oe").click()
    dropdown = self.driver.find_element(By.CSS_SELECTOR, ".css-1dbjc4n:nth-child(1) > .css-1dbjc4n > .r-30o5oe")
    dropdown.find_element(By.XPATH, "//option[. = 'November']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".css-1dbjc4n:nth-child(1) > .css-1dbjc4n > .r-30o5oe").click()
    self.driver.find_element(By.CSS_SELECTOR, ".css-1dbjc4n:nth-child(2) > .css-1dbjc4n > .r-30o5oe").click()
    dropdown = self.driver.find_element(By.CSS_SELECTOR, ".css-1dbjc4n:nth-child(2) > .css-1dbjc4n > .r-30o5oe")
    dropdown.find_element(By.XPATH, "//option[. = '17']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".css-1dbjc4n:nth-child(2) > .css-1dbjc4n > .r-30o5oe").click()
    self.driver.find_element(By.CSS_SELECTOR, ".css-1dbjc4n:nth-child(3) > .css-1dbjc4n > .r-30o5oe").click()
    dropdown = self.driver.find_element(By.CSS_SELECTOR, ".css-1dbjc4n:nth-child(3) > .css-1dbjc4n > .r-30o5oe")
    dropdown.find_element(By.XPATH, "//option[. = '1942']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".css-1dbjc4n:nth-child(3) > .css-1dbjc4n > .r-30o5oe").click()
    self.driver.find_element(By.CSS_SELECTOR, ".css-18t94o4:nth-child(1) > .css-901oao > .css-901oao > .css-901oao").click()
    self.driver.close()
  