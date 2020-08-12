class EmailClient:
    """
    The email client is what will be used to interface
    between the fake email API's. This class should be able
    to assume that all email API's have the same set of
    methods.
    """
    def __init__(self, **kwargs):
        self.api = kwargs['email_api']
        self.email_address = None


    def procure_email_address(self):
        """
        Using the client injected to the api attribute,
        procure an email address and set it as the email_address
        attribute.
        """
        email = self.api.get_email_address()

        self.email_address = email

        return self


    def has_mail(self) -> bool:
        """
        Tell me if there's mail or not
        """
        email_address = self.email_address

        if email_address is None:
            raise Exception('No email address has been created.')
        
        has_mail = self.api.has_mail(email_address)

        return has_mail