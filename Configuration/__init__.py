import os
from dotenv import load_dotenv; load_dotenv()

PATH = os.environ.get('DRIVER_PATH')

twitter_bot_config = {
    'driver_path': PATH,
    'base_url': 'https://twitter.com/'
}


fake_mail_generator_config = {
    'driver_path': PATH,
    'base_url': 'http://www.fakemailgenerator.com'
}