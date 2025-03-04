import pytest

from unittest.mock import patch, mock_open
from fetch_hackernews import data_manager


@pytest.fixture()
def create_directory(tmpdir):
    directory = tmpdir.mkdir("sub/")
    yield directory


@patch("fetch_hackernews.data_manager.requests.get")
def test_response_is_ok(mock_get):
    """
    Test if the website data is returned.
    Args:
        mock_get: mock object
    """
    # Configure the mock to return a response with an OK status code.
    mock_get.return_value.ok = True
    mock_get.return_value.status_code = 200

    # Send a request to the server and store the response.
    website_data = data_manager.get_hackernews()

    # Confirm that the website data will be returned (and not None)
    assert website_data is not None


@patch("fetch_hackernews.data_manager.requests.get")
def test_response_is_not_ok(mock_get):
    """
    Test if the program exits when the response is not OK.
    Args:
        mock_get: mock object
    """
    mock_get.return_value.ok = False
    with pytest.raises(SystemExit) as exitinfo:
        data_manager.get_hackernews()
        assert exitinfo.value.code == 1


def test_write_index_file(create_directory):
    """
    Test if we can write the index file.
    Args:
    create_directory: fixture
    """
    fake_file_path = create_directory + "/sub"
    content = "Message to write on file to be written"
    open_mock = mock_open()
    with patch(
        "fetch_hackernews.data_manager.open", open_mock, create=True
    ) as mocked_file:
        data_manager.create_config_file(fake_file_path, content)
        # assert if opened file on write mode 'w'
        mocked_file.assert_called_once_with(fake_file_path, "w")
        open_mock.return_value.write.assert_called_once_with(content)


# def test_read_index_file():
#     # TODO: Add test
#     pass
