#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Fetch Hacker News from news.ycombinator.com
Python 3.10+
Date created: January 26th, 2022
Date modified: February 17th, 2022
"""

import logging
import os
from datetime import datetime, timedelta
from pathlib import Path

from fetch_hackernews import common
from fetch_hackernews.app_config import check_config_dir
from fetch_hackernews.cli_output import cli_menu
from fetch_hackernews import data_manager

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

URL = common.__URL__
INDEX_FILE_PATH = common.platform_paths()

limit_datetime = datetime.now() - timedelta(hours=6)


def check_data_file() -> bool:
    """
    Check if the index.html file exist.

    Returns:
        True if the file exist, False if the file doesn't exist.
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
            fetched_news = data_manager.get_hackernews()
            data_manager.create_config_file(INDEX_FILE_PATH, fetched_news)

        hackernews = data_manager.parse_data()
        cli_menu(hackernews)
    else:
        logger.debug("Found no local index.html file.")
        fetched_news = data_manager.get_hackernews()
        data_manager.create_config_file(INDEX_FILE_PATH, fetched_news)
        hackernews = data_manager.parse_data()
        cli_menu(hackernews)


if __name__ == "__main__":
    main()
