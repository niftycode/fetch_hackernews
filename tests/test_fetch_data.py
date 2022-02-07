# import pytest
import requests

from nose.tools import assert_true

from fetch_hackernews.data_manager import get_hackernews


def test_request_response():
    # Send a request to the server and store the response.
    response = get_hackernews()

    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)
