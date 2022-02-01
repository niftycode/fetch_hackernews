# fetch_hackernews

A simple Python program to fetch [Hackernews](https://news.ycombinator.com) from *news.ycombinator.com*.

After running this program, an index.html file is created locally. This file will be updated after 12 hours.

## Operating System

macOS only

## Requirements

* Python >= 3.10
* requests
* beautifulsoup4

## Install

    $ pip3 install fetch_hackernews  # Linux, macOS
    $ pip install fetch_hackernews   # Windows

## Usage

Start the program with:

    $ fetch hacker_news

This shows you the 30 most recent messages. The output looks similar to the one shown below:

    Found no local index.html file.
    Fetch data from https://news.ycombinator.com…

    ##############################
    #                            #
    #         Hackernews         #
    #                            #
    ##############################

    1 - Red Light Green Light
    Link: https://jamessevedge.com/articles/red-light-green-light/
    
    2 - You can now send replies from your Duck Addresses
    Link: https://duckduckgo.com/email/faq
    …

All hacker news are read from a local `index.html` file. So, this program will search for such a file. If no file has been created yet, it will be downloaded using `requests`. Then the content will be parsed using `BeautifulSoup`.

By default, the `index.html` file is only updated every six hours. On macOS it is stored in the following directory:

    ~/.config/hackernews

## Changelog

see [Changelog.md](#)
