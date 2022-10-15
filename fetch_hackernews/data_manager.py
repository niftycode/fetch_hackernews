#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Fetch Hacker News from news.ycombinator.com
Python 3.10+
Date created: February 5th, 2022
Date modified: October 15th, 2022
"""


import requests
import logging
import re

from bs4 import BeautifulSoup
from collections.abc import Iterable

from fetch_hackernews.data_container import Headlines
from fetch_hackernews import common


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

URL = common.__URL__
INDEX_FILE_PATH = common.platform_paths()


def get_hackernews():
    """
    Fetch website data from the given URL
    Returns:
        The fetched website data or None
    """
    website_data = requests.get(URL)
    if website_data.ok:
        return website_data.text
    else:
        return None


def create_config_file(file_path, content):
    """
    Save a file (in this case the index.html file)
    Args:
        file_path: The path to the directory in which to save the file.
        content: The content to be saved.
    """
    with open(file_path, "w") as fh:
        fh.write(content)


def parse_data() -> list:
    """
    Parse the index.html file.
    Returns:
        A list containing the Headline objects.
    """
    with open(INDEX_FILE_PATH, "r") as f:
        soup = BeautifulSoup(f, "html.parser")

    # logger.debug(soup.prettify())

    # title = soup.find_all('a')

    title = soup.find_all("td", "title")
    unfiltered_links = []
    filtered_links = []

    for i in soup.find_all("span", "titleline"):
        for j in i.find_all("a", href=True):
            unfiltered_links.append(j["href"])
            # print(j["href"])

    for ul in unfiltered_links:
        match = re.findall("^https:.*", ul) or re.findall("^item.*", ul)
        if not match:
            continue
        filtered_links.append(match)

    rank = []
    headlines = []

    rank_list = title[0::2]
    title_list = title[1::2]

    for i in rank_list:
        if i.text != "More":
            rank.append(i.text)

    for j in title_list:
        headlines.append(j.text)

    def flatten(a_list):
        """
        Flatten an irregular (arbitrarily nested) list of lists

        Args:
            a_list: The list to flatten
        """
        for x in a_list:
            if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
                yield from flatten(x)
            else:
                yield x

    # Flatten filtered_links
    links = list(flatten(filtered_links))

    # Handle the case where a link contains the string "item?id=".
    substring = "item?id="
    url = "https://news.ycombinator.com/"

    for index, link in enumerate(links):
        if link.find(substring) != -1:
            links[index] = url + link

    logger.debug(len(rank))
    logger.debug(len(headlines))
    logger.debug(len(filtered_links))

    hackernews_data = []

    # Append Headline objects containing headline_id, headlines and links.
    for i in range(0, 30):
        hackernews_data.append(Headlines(rank[i], headlines[i], links[i]))

    return hackernews_data
