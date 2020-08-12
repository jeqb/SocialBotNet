import os
from datetime import datetime
from dotenv import load_dotenv; load_dotenv()

from Websites import TwitterApi

print(datetime.now())

# twitter API testing
PATH = os.environ.get('DRIVER_PATH')
BASE_URL = 'https://www.google.com'

config = {
    'driver_path': PATH,
    'base_url': BASE_URL
}

api = TwitterApi(**config)



# email generator stuff
from Email import FakeMailGeneratorApi

config = {
    'driver_path': PATH,
    'base_url': 'http://www.fakemailgenerator.com'
}

email_client = FakeMailGeneratorApi(**config)

# for the button copy thingy
button_full_xpath = '/html/body/div[1]/div[1]/div[1]/div[3]/div/button'

# from the string thingy
paragraph_full_xpath = '/html/body/div[1]/div[1]/div[5]/div/p/strong/span'

email = email_client.get_email_address()
# email = email_client.get_website_html()

print(email)

print(datetime.now())