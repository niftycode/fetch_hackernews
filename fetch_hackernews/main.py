#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Fetch Hacker News from news.ycombinator.com
Python 3.10+
Date created: January 26th, 2022
Date modified: January 29th, 2022
"""

from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import requests
from pathlib import Path
import os
import getpass
import logging

from fetch_hackernews.data_container import Headlines
from fetch_hackernews.cli_output import cli_menu
from fetch_hackernews.app_config import check_config_dir


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def check_data_file():
    logger.debug(limit_datetime)
    logger.debug(os.getcwd())

    index_path_file = f"/Users/{getpass.getuser()}/.config/hackernews/index.html"

    if Path(index_path_file).is_file():
        last_modified = datetime.fromtimestamp(os.path.getmtime(index_path_file))
        logger.debug(f"last modified: {last_modified}")
        logger.debug(f"limit_datetime: {limit_datetime}")
        if last_modified < limit_datetime:
            logger.debug("Fetch data...")
            fetch_data()
        parse_data()
    else:
        print("Found no local index.html file.")
        print("Fetch data from Hackernews...")
        fetch_data()


def fetch_data():
    # Fetch index.html file
    website_data = requests.get(URL)
    logger.debug(website_data.text)

    # Get path to the index.html file
    path = f"/Users/{getpass.getuser()}/.config/hackernews/"
    file_name = "index.html"
    index_file_path = os.path.join(path, file_name)

    # Save new index.html file
    with open(index_file_path, "w") as fh:
        fh.write(website_data.text)

    parse_data()


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

    # Remove the last items
    # headlines.pop()
    # links.pop()

    # Create empty list
    hackernews_data = []

    # Append Headline objects containing
    # headline_id, headlines and links.
    for i in range(0, 30):
        hackernews_data.append(Headlines(headline_id[i],
                                         headlines[i],
                                         links[i]))

    cli_menu(hackernews_data)


def main():
    check_config_dir()
    check_data_file()


if __name__ == "__main__":
    limit_datetime = datetime.now() - timedelta(hours=6)
    URL = "https://news.ycombinator.com"
    main()
