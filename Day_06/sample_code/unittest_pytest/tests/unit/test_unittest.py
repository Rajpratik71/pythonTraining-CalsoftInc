from unittest import TestCase, mock

from parameterized import parameterized
from sample_code.app import Sample, requests, RequestException


class MockResponse:
    def __init__(self, status_code):
        self.status_code = status_code

    def raise_for_status(self, *args, **kwargs):
        raise requests.exceptions.HTTPError(f"Got HTTP error code: {self.status_code}")


class UnitTestSample(TestCase):

    def setUp(self) -> None:
        self.sample = Sample()
        self.url = "http://www.google.com"

    def tearDown(self) -> None:
        self.sample.session.close()

    def test_get_response(self):
        response = self.sample.get_response(self.url)
        self.assertEqual(response.status_code, 200)

    # def test_get_response_without_mock(self):
    #     with self.assertRaises(requests.exceptions.RequestException):
    #         _ = self.sample.get_response("http://www.xfhagfbkjcb.com")

    @parameterized.expand([(400,), (500,)])
    def test_get_response_mock_error(self, status_code):
        with self.assertRaises(RequestException) as ex_info:
            with mock.patch.object(requests.Session, "get") as mock_get:
                mock_get.return_value = MockResponse(status_code)
                sample = Sample()
                sample.get_response(self.url)
        self.assertIn(f"Received error for URL: {self.url}, error:", str(ex_info.exception))

    def test_get_response_mock_side_effect(self):
        with self.assertRaises(RequestException) as ex_info:
            with mock.patch("sample_code.app.requests.Session.get") as mock_get:
                mock_response = mock.Mock()
                mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
                    f"Got HTTP error code: 400")
                mock_get.return_value = mock_response
                sample = Sample()
                sample.get_response(self.url)
        self.assertIn(f"Received error for URL: {self.url}, error:", str(ex_info.exception))
