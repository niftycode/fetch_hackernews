# fetch-hackernews

![Static Badge](https://img.shields.io/badge/python-3.12-blue)
![Static Badge](https://img.shields.io/badge/python-3.13-blue)
![GitHub License](https://img.shields.io/github/license/niftycode/ai-chatbot)
![Github Issues](https://img.shields.io/github/issues/niftycode/fetch_hackernews.svg?style=flat)
![PyPi Version](https://img.shields.io/pypi/v/fetch_hackernews)
![GitHub last commit](https://img.shields.io/github/last-commit/niftycode/fetch_hackernews)

A simple program to fetch [Hackernews](https://news.ycombinator.com) from *news.ycombinator.com* written in Python.

I know, there are already some similar projects via [PyPi](https://pypi.org) available, but I said to myself, why not add one more app :wink: It gave me the opportunity to finally deal with the subject of web scraping (with [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)).

## Operating System

macOS, Linux and Windows

## Requirements

* Python >= 3.12
* `requests`
* `beautifulsoup4`

## Install

    $ pip3 install fetch_hackernews

## Usage

Start the program with following command:

    $ fetch_hackernews

This shows you the 30 most recent messages. The output looks similar to the one shown below:

    Found no local index.html file.
    Fetch data from https://news.ycombinator.com…

    ##############################
    #                            #
    #      Fetch Hacker News     #
    #       Version: 1.0.7       #
    #                            #
    ##############################

    1 - Red Light Green Light
    Link: https://jamessevedge.com/articles/red-light-green-light/
    
    2 - You can now send replies from your Duck Addresses
    Link: https://duckduckgo.com/email/faq
    …

After running this program, an index.html file is created locally. This reduces requests to the server from [news.ycombinator.com](https://news.ycombinator.com).

So, all news will be read from the local `index.html` file. This program will search for such a file. If no file has been created yet, it will create this file, download the content (using `requests`) and save it. After that, the content will be parsed using `BeautifulSoup`.

By default, the `index.html` file is only updated every six hours.

The `index.html` file is stored in the following directory (macOS):

    ~/.config/hackernews

## Changelog

see [Changelog.md](https://github.com/niftycode/fetch_hackernews/blob/main/Changelog.md)
