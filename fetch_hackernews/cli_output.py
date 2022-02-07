#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Output fetched news
Python 3.10+
Date created: January 30th, 2022
Date modified: February 7th, 2022
"""


def cli_menu(headlines: list):
    print()
    print("##############################")
    print("#                            #")
    print("#        Hacker News         #")
    print("#                            #")
    print("##############################")
    print()

    for headline in headlines:
        print(headline)
