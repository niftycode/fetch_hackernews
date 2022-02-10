#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Data model
Python 3.10+
Date created: January 30th, 2022
Date modified: February 7th, 2022
"""

from dataclasses import dataclass


@dataclass
class Headlines:
    """
    This dataclass is the hacker news data store.
    """

    headline_id: int
    headline: str
    link: str

    def __repr__(self):
        return (
            f"{self.__class__.__name__}({self.headline_id!r}, "
            f"{self.headline!r}, "
            f"{self.link!r})"
        )

    def __str__(self):
        """

        Returns: String representation of this object

        """
        return f"{self.headline_id} - {self.headline}\n" f"Link: {self.link}\n"
