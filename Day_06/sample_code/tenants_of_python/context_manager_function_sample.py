from contextlib import contextmanager

import requests


@contextmanager
def request_session():
    session = requests.Session()
    try:
        print("Starting session")
        yield session
    finally:
        print("Closing seesion")
        session.close()


if __name__ == "__main__":
    with request_session() as session:
        response = session.get("http://www.google.com")
        print(f"response status code: {response.status_code}")
