# import pytest
# import requests

import os
import getpass

from unittest.mock import patch, mock_open

from nose.tools import assert_is_not_none, assert_is_none

from fetch_hackernews.data_manager import get_hackernews
from fetch_hackernews.data_manager import create_config_file


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


def test_create_file():
    open_mock = mock_open()
    with patch("fetch_hackernews.data_manager.open", open_mock, create=True):
        create_config_file("website-data")

    path = f"/Users/{getpass.getuser()}/.config/hackernews/"
    file_name = "index.html"
    index_file_path = os.path.join(path, file_name)

    open_mock.assert_called_with(index_file_path, "w")
    open_mock.return_value.write.assert_called_once_with("website-data")
