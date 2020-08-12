import os
from datetime import datetime
from dotenv import load_dotenv; load_dotenv()

from Websites import TwitterApi

print('start: ', datetime.now())

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

# email = email_client.get_email_address()

email = 'Pagel1929@superrito.com'

email_inbox_url = email_client.get_email_url(email)

inbox_html = email_client.get_inbox_html(email_inbox_url)

empty_indication = email_client.is_inbox_empty(inbox_html)

print('email address: ', email)
print('inbox url: ', email_inbox_url)
print('is inbox empty: ', empty_indication)

print('finish: ', datetime.now())
