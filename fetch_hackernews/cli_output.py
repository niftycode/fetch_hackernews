#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Output fetched news
Python 3.10+
Date created: January 30th, 2022
Date modified: February 9th, 2022
"""

from fetch_hackernews import constants


def cli_menu(headlines: list):
    """
    Show headline_ids, headlines and links in the console.
    Args:
        headlines: A list containing Headlines objects
        (headline_id, headline, link)
    """
    print()
    print("##############################")
    print("#                            #")
    print("#        Hacker News         #")
    print(f"#           {constants.__VERSION__}            #")
    print("#                            #")
    print("##############################")
    print()

    for headline in headlines:
        print(headline)
