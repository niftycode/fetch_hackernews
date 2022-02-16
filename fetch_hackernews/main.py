#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Fetch Hacker News from news.ycombinator.com
Python 3.10+
Date created: January 26th, 2022
Date modified: February 16th, 2022
"""

import os
import logging

from datetime import datetime, timedelta
from pathlib import Path

from fetch_hackernews import constants
from fetch_hackernews.app_config import check_config_dir
from fetch_hackernews.data_manager import FileManager
from fetch_hackernews.cli_output import cli_menu


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

URL = constants.__URL__
INDEX_FILE_PATH = constants.__INDEX_FILE_PATH__

limit_datetime = datetime.now() - timedelta(hours=6)


def check_data_file() -> bool:
    """
    Check if the index.html file exist.

    Returns: True if the file exist, False if the File doesn't exist.

    """
    if Path(INDEX_FILE_PATH).is_file():
        return True
    else:
        return False


def main():
    """
    Entry point of this application.
    """
    check_config_dir()
    rval = check_data_file()

    if rval:
        last_modified = datetime.fromtimestamp(os.path.getmtime(INDEX_FILE_PATH))

        logger.debug(f"last modified: {last_modified}")
        logger.debug(f"limit_datetime: {limit_datetime}")

        if last_modified < limit_datetime:
            logger.debug("Fetch data...")
            fetched_news = FileManager.get_hackernews()
            FileManager.create_config_file(INDEX_FILE_PATH, fetched_news)
        hackernews = FileManager.parse_data()
        cli_menu(hackernews)
    else:
        logger.debug("Found no local index.html file.")
        fetched_news = FileManager.get_hackernews()
        FileManager.create_config_file(INDEX_FILE_PATH, fetched_news)
        hackernews = FileManager.parse_data()
        cli_menu(hackernews)


if __name__ == "__main__":
    main()
