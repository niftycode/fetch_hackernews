# import pytest
# import requests

from nose.tools import assert_is_not_none

from fetch_hackernews.data_manager import get_hackernews


def test_request_response():
    # Send a request to the server and store the response.
    website_data = get_hackernews()

    # Confirm that the request-response cycle completed successfully.
    # assert_true(website_data.ok)
    assert_is_not_none(website_data)
