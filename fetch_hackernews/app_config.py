#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Check for the existence of the .config directory
Python 3.10+
Date created: January 31st, 2022
Date modified: -
"""

import getpass
import os


def check_config_dir():
    """
    Check for the existence of the .config directory.
    Create .config and hackernwes directories if they
    doesn't exist.
    """
    config_directory = f"/Users/{getpass.getuser()}/.config"
    directory = "hackernews"
    parent_path = config_directory
    hackernews_path = os.path.join(parent_path, directory)
    mode = 0o755

    # Create .config and .config/hackernews directories
    # if necessary
    if os.path.isdir(config_directory):
        if not os.path.isdir(hackernews_path):
            os.mkdir(hackernews_path, mode)
    else:
        config_dir_path = f"/Users/{getpass.getuser()}/.config"
        os.mkdir(config_dir_path, mode)
        os.mkdir(hackernews_path, mode)
