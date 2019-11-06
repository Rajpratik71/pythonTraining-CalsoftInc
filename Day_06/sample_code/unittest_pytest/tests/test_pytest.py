from unittest import mock

import pytest
from sample_code.app import Sample, requests, RequestException

TEST_URL = "http://www.google.com"


class MockResponse:
    def __init__(self, status_code):
        self.status_code = status_code

    def raise_for_status(self, *args, **kwargs):
        raise requests.exceptions.HTTPError(f"Got HTTP error code: {self.status_code}")


def test_get_response(sample):
    response = sample.get_response(TEST_URL)
    assert response.status_code == 200


@pytest.mark.parametrize("status_code", [400, 500])
def test_get_response_mock_error(status_code):
    with pytest.raises(RequestException) as ex_info:
        with mock.patch.object(requests.Session, "get") as mock_get:
            mock_get.return_value = MockResponse(status_code)
            sample = Sample()
            sample.get_response(TEST_URL)
    assert f"Received error for URL: {TEST_URL}, error:" in str(ex_info.value)


def test_get_response_mock_side_effect():
    with pytest.raises(RequestException) as ex_info:
        with mock.patch("sample_code.app.requests.Session.get") as mock_get:
            mock_response = mock.Mock()
            mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
                f"Got HTTP error code: 400"
            )
            mock_get.return_value = mock_response
            sample = Sample()
            sample.get_response(TEST_URL)
    assert f"Received error for URL: {TEST_URL}, error:" in str(ex_info.value)
