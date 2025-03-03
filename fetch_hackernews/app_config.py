#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Check if the .config directory exists
Python 3.12+
Date created: January 31st, 2022
Date modified: March 3rd, 2025
"""

# import getpass
import os

from os.path import expanduser

DIRECTORY = expanduser("~") + "/.config"


def check_config_dir():
    """
    Check for the existence of the .config directory.
    Create .config and hackernews directories if they
    doesn't exist.

    PATH: ~.config/hackernews
    """
    # config_directory = f"/Users/{getpass.getuser()}/.config"
    app_directory = "hackernews"
    # parent_path = config_directory
    hackernews_path = os.path.join(DIRECTORY, app_directory)
    mode = 0o755

    # Create .config and .config/hackernews directories if necessary
    if os.path.isdir(DIRECTORY):
        if not os.path.isdir(hackernews_path):
            os.mkdir(hackernews_path, mode)
    else:
        # config_dir_path = f"/Users/{getpass.getuser()}/.config"
        os.mkdir(DIRECTORY, mode)
        os.mkdir(hackernews_path, mode)
