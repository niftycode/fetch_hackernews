#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Output fetched news
Python 3.10+
Date created: January 30th, 2022
Date modified: -
"""


def cli_menu(headlines: list):

    print("##############################")
    print("#                            #")
    print("#         Hackernews         #")
    print("#                            #")
    print("##############################")

    for headline in headlines:
        print(headline)
