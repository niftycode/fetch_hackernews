#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Fetch Hacker News from ycombinator.com
Version: 1.0
Python 3.10+
Date created: January 26th, 2022
Date modified: January 29th, 2022
"""

from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import requests
from pathlib import Path
import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def check_data_file():
    logger.debug(limit_datetime)
    logger.debug(os.getcwd())

    cwd = os.getcwd() + "/index.html"

    if Path(cwd).is_file():
        parse_data()
    else:
        logger.debug("Fetch data...")
        fetch_data()


def fetch_data():
    # Fetch index.html file
    website_data = requests.get(URL)
    logger.debug(website_data.text)

    # Save new index.html file
    with open("index.html", "w") as fh:
        fh.write(website_data.text)

    parse_data()


def parse_data():
    with open("index.html", "r") as f:
        doc = BeautifulSoup(f, "html.parser")

    tag = doc.find_all(class_="titlelink", href=True)

    for t in tag:
        print(t["href"])
        # print(t.text)


def main():
    check_data_file()


if __name__ == "__main__":
    limit_datetime = datetime.now() - timedelta(days=1)
    logger.debug(limit_datetime)
    URL = "https://news.ycombinator.com"
    main()
