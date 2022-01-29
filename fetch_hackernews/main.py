#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Fetch Hacker News from ycombinator.com
Version: 1.0
Python 3.10+
Date created: January 26th, 2022
Date modified: January 29th, 2022
"""

from bs4 import BeautifulSoup
import requests
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

URL = "https://news.ycombinator.com"


def check_data_file():
    pass


def main():
    # website_data = requests.get(URL)
    # print(website_data.text)

    # with open("index2.html", "w") as fh:
    #     fh.write(website_data.text)

    with open("index.html", "r") as f:
        doc = BeautifulSoup(f, "html.parser")
    # print(doc.prettify())
    # tag = doc.title
    # print(tag)  # <- Hacker News

    # tag = doc.table
    # tag = doc.find_all("td")[4]

    """
    title_1 = doc.find_all(class_="title")[5]
    print(title_1)

    title_2 = doc.find_all(class_="title")[7]
    print(title_2)

    title_3 = doc.find_all(class_="title")[9]
    print(title_3)
    """

    tag = doc.find_all(class_="titlelink", href=True)

    for t in tag:
        print(t["href"])
        # print(t.text)


if __name__ == '__main__':
    main()
