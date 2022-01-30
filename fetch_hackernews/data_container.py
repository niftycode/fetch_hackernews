#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Data model
Python 3.10+
Date created: January 30th, 2022
Date modified: -
"""

from dataclasses import dataclass


@dataclass
class Headlines:
    """
    This dataclass is the store for the hackernews.
    """
    headline_id: int
    headline: str
    link: str

    def __repr__(self):
        return f'{self.__class__.__name__}({self.headline_id!r}, ' \
               f'{self.headline!r}, ' \
               f'{self.link!r})'

    def __str__(self):
        """
        :rtype: String representation of this object
        """
        return f"No: {self.headline_id}\n" \
               f"Headline: {self.headline}\n" \
               f"Link: {self.link}\n"
