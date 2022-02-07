#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Fetch Hacker News from news.ycombinator.com
Python 3.10+
Date created: January 26th, 2022
Date modified: February 7th, 2022
"""

import os
import getpass
import logging

from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from pathlib import Path

from fetch_hackernews import constants
from fetch_hackernews.data_container import Headlines
from fetch_hackernews.cli_output import cli_menu
from fetch_hackernews.app_config import check_config_dir
from fetch_hackernews.data_manager import get_hackernews
from fetch_hackernews.data_manager import create_config_file


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def check_data_file() -> bool:
    logger.debug(limit_datetime)
    logger.debug(os.getcwd())

    if Path(INDEX_FILE_PATH).is_file():
        return True
    else:
        return False


def parse_data():
    path = f"/Users/{getpass.getuser()}/.config/hackernews/"
    file_name = "index.html"
    index_file_path = os.path.join(path, file_name)

    with open(index_file_path, "r") as f:
        doc = BeautifulSoup(f, "html.parser")

    tag = doc.find_all(class_="titlelink", href=True)

    for t in tag:
        logger.debug(t["href"])
        logger.debug(t.text)

    headline_id = []
    headlines = []
    links = []

    for i in range(1, 31):
        headline_id.append(i)

    for t in tag:
        headlines.append(t.text)
        links.append(t["href"])

    hackernews_data = []

    # Append Headline objects containing headline_id, headlines and links.
    for i in range(0, 30):
        hackernews_data.append(Headlines(headline_id[i],
                                         headlines[i],
                                         links[i]))

    cli_menu(hackernews_data)


def main():
    check_config_dir()
    rval = check_data_file()

    if rval:
        last_modified = datetime.fromtimestamp(os.path.getmtime(INDEX_FILE_PATH))

        logger.debug(f"last modified: {last_modified}")
        logger.debug(f"limit_datetime: {limit_datetime}")

        if last_modified < limit_datetime:
            logger.debug("Fetch data...")
            fetched_news = get_hackernews()
            create_config_file(fetched_news)
        parse_data()

    else:
        logger.debug("Found no local index.html file.")
        fetched_news = get_hackernews()
        create_config_file(fetched_news)
        parse_data()


if __name__ == "__main__":
    URL = constants.__URL__
    INDEX_FILE_PATH = constants.__INDEX_FILE_PATH__
    limit_datetime = datetime.now() - timedelta(hours=6)
    main()
