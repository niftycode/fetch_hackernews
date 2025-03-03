#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Common methods + constants
Python 3.12+
Date created: February 7th, 2022
Date modified: May 30th, 2023
"""

import getpass
import platform


__VERSION__ = "1.0.8"
__URL__ = "https://news.ycombinator.com"


def platform_paths() -> str:
    """
    Check which operating system is running and return the corresponding path.

    Returns:
        Path to the index.html file.

    """
    installed_os = platform.system()

    if installed_os == "Darwin" or installed_os == "Windows":
        config_path = f"/Users/{getpass.getuser()}/.config/hackernews/index.html"
    elif installed_os == "Linux":
        config_path = f"/home/{getpass.getuser()}/.config/hackernews/index.html"
    else:
        config_path = "Unknown"

    return config_path
