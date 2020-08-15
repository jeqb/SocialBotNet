from Websites import TwitterApi
from Security import WebsiteCredentials
from Linguistics import generate_username
import Security.Utilities as Utilities

class TwitterBot:
    """
    This is the agent that interacts with twitter through
    the TwitterApi class. All Interaction with twitter should
    pass through this class
    """
    def __init__(self, **kwargs):
        self.api = TwitterApi(**kwargs)
        self.email_client = kwargs['email_client']
        self.credentials = WebsiteCredentials()
        self.utils = Utilities


    def create_account(self) -> WebsiteCredentials:
        """
        Call this method to create a new twitter account.
        it should return the credentials afterwards. Credentials will
        also be stored in an SQLit3 database
        """

        username = generate_username()
        password = self.utils.generate_password()
        email = self.email_client.procure_email_address()
        birthday = self.utils.generate_birthday()

        creds = WebsiteCredentials(
            **{
                'username': username,
                'password': password,
                'email': email,
                'birthday': birthday
            }
        )

        return creds