import requests
from sample_code.exceptions import RequestException


class Sample:
    def __init__(self):
        self.session = requests.Session()

    def get_response(self, url):
        try:
            response = self.session.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as ex:
            raise RequestException(f"Received error for URL: {url}, error: {str(ex)}")
        return response
