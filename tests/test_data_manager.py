# import pytest

from unittest.mock import patch

from nose.tools import assert_is_not_none, assert_is_none

from fetch_hackernews.data_manager import get_hackernews


@patch('fetch_hackernews.data_manager.requests.get')
def test_response_is_ok(mock_get):
    # Configure the mock to return a response with an OK status code.
    mock_get.return_value.ok = True

    # Send a request to the server and store the response.
    website_data = get_hackernews()

    # Confirm that the website data will be returned (and not None)
    assert_is_not_none(website_data)


@patch('fetch_hackernews.data_manager.requests.get')
def test_response_is_not_ok(mock_get):
    mock_get.return_value.ok = False
    website_data = get_hackernews()
    assert_is_none(website_data)
