#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Data model
Python 3.10+
Date created: January 30th, 2022
Date modified: August 7th, 2022
"""

from dataclasses import dataclass

REVERSE = "\033[;7m"  # inverts the terminal background and foreground colors
RESET = "\033[0m"


@dataclass
class Headlines:
    """
    This dataclass is the hacker news data store.
    """

    headline_id: str
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
        String representation

        Returns:
            String representation of this object

        """
        return f"{REVERSE}{self.headline_id}{RESET} - {self.headline}\n" f"Link: {self.link}\n"
