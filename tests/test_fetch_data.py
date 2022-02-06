# import pytest
import requests

from nose.tools import assert_true


def test_request_response():
    # Send a request to the API server and store the response.
    response = requests.get("https://news.ycombinator.com")

    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)
