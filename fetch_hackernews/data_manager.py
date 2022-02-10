#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Fetch Hacker News from news.ycombinator.com
Python 3.10+
Date created: February 5th, 2022
Date modified: February 10th, 2022
"""


import requests
import logging

from bs4 import BeautifulSoup

from fetch_hackernews.data_container import Headlines
from fetch_hackernews import constants


logger = logging.getLogger()

URL = constants.__URL__
INDEX_FILE_PATH = constants.__INDEX_FILE_PATH__


class FileManager:
    """
    This class includes static methods for
    fetching data, parsing the fetched data
    and creating the local index.html file.
    """

    @staticmethod
    def get_hackernews():
        """
        Fetch website data from the given URL
        Returns: The fetched website data or None
        """
        website_data = requests.get(URL)
        if website_data.ok:
            logger.debug(website_data.text)
            return website_data.text
        else:
            return None

    @staticmethod
    def create_config_file(file_path, content):
        """
        Save a file (in this case the index.html file)
        Args:
            file_path: The path to the directory in which to save the file.
            content: The content to be saved.
        """
        with open(file_path, "w") as fh:
            fh.write(content)

    @staticmethod
    def parse_data():
        """
        Parse the index.html file.
        Returns: A list containing the Headline objects.
        """
        with open(INDEX_FILE_PATH, "r") as f:
            doc = BeautifulSoup(f, "html.parser")

        titlelink = doc.find_all(class_="titlelink", href=True)
        # score = doc.find_all(class_="score")
        # TODO: add points

        headline_id = []
        headlines = []
        links = []
        # points = []

        for i in range(1, 31):
            headline_id.append(i)

        for t in titlelink:
            headlines.append(t.text)
            links.append(t["href"])

        # for s in score:
        #     points.append(s.text)

        # print(len(points))
        # for j in points:
        #     print(j)

        # Handle the case where a link contains the string "item?id=".
        substring = "item?id="
        url = "https://news.ycombinator.com/"

        for index, link in enumerate(links):
            if link.find(substring) != -1:
                links[index] = url + link

        hackernews_data = []

        # Append Headline objects containing headline_id, headlines and links.
        for i in range(0, 30):
            hackernews_data.append(Headlines(headline_id[i], headlines[i], links[i]))

        return hackernews_data
