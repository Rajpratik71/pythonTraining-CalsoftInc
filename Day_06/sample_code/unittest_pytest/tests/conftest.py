import pytest
from sample_code.app import Sample


@pytest.fixture(scope="function")
def sample():
    return Sample()
