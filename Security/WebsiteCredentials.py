class WebsiteCredentials:
    def __init__(self, **kwargs):
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.email = kwargs.get('email')
        self.birthday = kwargs.get('birthday')

    def __str__(self) -> str:
        stuff = {
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'birthday': self.birthday
        }

        return str(stuff)


    def __dict__(self) -> str:
        stuff = {
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'birthday': self.birthday
        }

        return stuff