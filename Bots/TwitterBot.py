from Websites import TwitterApi

class TwitterBot:
    def __init__(self, **kwargs):
        self.api = TwitterApi(**kwargs)
        self.email_client = kwargs['email_client']