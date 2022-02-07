#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Fetch Hacker News from news.ycombinator.com
Python 3.10+
Date created: February 5th, 2022
Date modified: -
"""

import os
import getpass
import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

URL = "https://news.ycombinator.com"


def get_hackernews():
    # Get hacker news' index.html file
    website_data = requests.get(URL)
    if website_data.ok:
        logger.debug(website_data.text)
        return website_data
    else:
        return None


def create_config_file(website_data):
    # Get path to the index.html file
    path = f"/Users/{getpass.getuser()}/.config/hackernews/"
    file_name = "index.html"
    index_file_path = os.path.join(path, file_name)

    # Save new index.html file
    with open(index_file_path, "w") as fh:
        fh.write(website_data.text)
