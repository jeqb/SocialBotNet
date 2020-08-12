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
from Clients import EmailClient

config = {
    'driver_path': PATH,
    'base_url': 'http://www.fakemailgenerator.com'
}


email_api = FakeMailGeneratorApi(**config)
email_client = EmailClient(email_api=email_api)
email_client.procure_email_address()
has_mail = email_client.has_mail()

print('email address: ', email_client.email_address)
print('inbox has mail: ', has_mail)

print('finish: ', datetime.now())