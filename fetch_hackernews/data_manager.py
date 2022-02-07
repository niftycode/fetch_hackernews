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

from fetch_hackernews import constants

# logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

URL = constants.__URL__
INDEX_FILE_PATH = constants.__INDEX_FILE_PATH__


def get_hackernews():
    # Get hacker news' index.html file
    website_data = requests.get(URL)
    if website_data.ok:
        logger.debug(website_data.text)
        return website_data
    else:
        return None


def create_config_file(website_data):
    with open(INDEX_FILE_PATH, "w") as fh:
        fh.write(website_data.text)
