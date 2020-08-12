import re
from .EmailUtility import EmailUtility

class FakeMailGeneratorApi(EmailUtility):
    """
    Api class for http://www.fakemailgenerator.com
    """

    def __init__(self, **kwargs):
        EmailUtility.__init__(self, **kwargs)

    
    def get_website_html(self) -> str:
        """
        call the website and get the html source containing the
        email address
        """

        url = self.base_url

        self.initialize_driver()
        
        self.driver.get(url)

        html_source = self.driver.page_source

        self.end_driver()

        return html_source


    def get_email_from_string(self, html_source: str) -> str:
        """
        Given the HTML of fake mail generator, extract the email address
        from the source
        """

        search_string = 'data-clipboard-text'

        # find the position of the search_string
        # this takes you to the end of:
        #   data-clipboard-text=" <- keep that "
        start = html_source.find(search_string) + 21

        # make a sub string from the start index.
        # the email is the text starting from the beginning
        # of the sub string, until: ">Copy<
        # so find the position of that, and get the stuff in
        # between the start of the substring and ">Copy<
        substring = html_source[start:]

        end = substring.find(r'">Copy<')

        email = substring[:end]

        return email


    def get_email_address(self) -> str:
        """
        Reach out to the website, and grab an email address from the
        html element
        """

        html_source = self.get_website_html()

        email = self.get_email_from_string(html_source)

        return email