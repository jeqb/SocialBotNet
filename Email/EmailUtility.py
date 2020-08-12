from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

class EmailUtility:
    """
    Base class to reach out to websites that provide fake emails
    """
    def __init__(self, **kwargs):
        self.driver_path = kwargs['driver_path']

        self.base_url = kwargs['base_url']


    def get_fake_useragent(self):
        """
        In order to obfuscate Selenium from the website, generate
        a fake useragent to circumvent detection.

        sauce:
            https://stackoverflow.com/questions/49565042/way-to-change-google-chrome-user-agent-in-selenium
        """

        options = Options()

        ua = UserAgent()

        userAgent = ua.random

        options.add_argument(f'user-agent={userAgent}')

        return options


    def initialize_driver(self) -> None:
        """
        Separate method to create the driver because when you initialize
        the webdriver, it opens a tab. don't want that for dev purposes.
        """

        chrome_options = self.get_fake_useragent()

        self.driver = webdriver.Chrome(
            executable_path=self.driver_path, chrome_options=chrome_options
            )


    def end_driver(self) -> None:
        """
        quit the driver
        """

        self.driver.quit()


    def get_email_address(self) -> str:
        pass