import time
from random import randrange
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class WebsiteApi:
    """
    Base class that all Social network websites will in herit
    """
    def __init__(self, **kwargs):
        self.driver_path = kwargs['driver_path']

        self.base_url = kwargs['base_url']


    def initialize_driver(self) -> None:
        """
        Separate method to create the driver because when you initialize
        the webdriver, it opens a tab. don't want that for dev purposes.
        """

        self.driver = webdriver.Chrome(executable_path=self.driver_path)