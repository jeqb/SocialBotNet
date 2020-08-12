from datetime import datetime
import calendar
from .WebsiteApi import WebsiteApi

class TwitterApi(WebsiteApi):
    """
    Selenium based class api to utilize twitter
    """
    def __init__(self, **kwargs):
        WebsiteApi.__init__(self, **kwargs)


    def _get_month_name(self, date: datetime) -> int:
        """
        given a datetime object, return the month as an int
        """

        month_int = date.month

        return calendar.month_name[month_int]


    def create_account(self, username: str, email: str, birthday: datetime) -> None:
        """
        username -> "SomeUsername"
        email -> myemail@domain.com
        birthday -> datetime(2020, 1, 25)
        """

        month_name = self._get_month_name(birthday)
        day = birthday.day
        year = birthday.year
        