import os
from datetime import datetime

from Configuration import twitter_bot_config, fake_mail_generator_config

# email generator stuff
from Email import FakeMailGeneratorApi
from Clients import EmailClient
email_api = FakeMailGeneratorApi(**fake_mail_generator_config)
email_client = EmailClient(email_api=email_api)
# email generator stuff

# twitter bot stuff
from Bots import TwitterBot
twitter_bot_config.update({'email_client': email_client})
twitter_bot = TwitterBot(**twitter_bot_config)
# twitter bot stuff

