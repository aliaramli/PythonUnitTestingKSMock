"""
Holiday class
To get holiday list for specific country based on the country code and year

"""
import requests
import certifi

API_BASE_URL = "https://date.nager.at"
API_ENDPOINT = "api/v3/PublicHolidays"


class Holiday:
    """Holiday class
    Using public API to get list of holiday
    """

    def get_holiday(self, year: str, country_code: str) -> dict:
        """get list of holidays based on year and country code

        Args:
            year (str): year
            country_code (str): country_code
        """
        response = requests.get(
            f"{API_BASE_URL}/{API_ENDPOINT}/{year}/{country_code}", verify=certifi.where())
        return response.json()
