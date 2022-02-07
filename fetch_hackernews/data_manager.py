#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Fetch Hacker News from news.ycombinator.com
Python 3.10+
Date created: February 5th, 2022
Date modified: -
"""


import requests
import logging

from bs4 import BeautifulSoup

from fetch_hackernews.data_container import Headlines
from fetch_hackernews import constants

# logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

URL = constants.__URL__
INDEX_FILE_PATH = constants.__INDEX_FILE_PATH__


class FileManager:
    @staticmethod
    def get_hackernews():
        # Get hacker news' index.html file
        website_data = requests.get(URL)
        if website_data.ok:
            logger.debug(website_data.text)
            return website_data.text
        else:
            return None

    @staticmethod
    def create_config_file(file_path, content):
        with open(file_path, "w") as fh:
            fh.write(content)

    @staticmethod
    def parse_data():
        with open(INDEX_FILE_PATH, "r") as f:
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

        return hackernews_data
