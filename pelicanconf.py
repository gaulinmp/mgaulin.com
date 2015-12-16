#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Maclean Gaulin'
SITENAME = 'Maclean Gaulin'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pandas', 'http://pandas.pydata.org/pandas-docs/stable/'),
         ('Python', 'http://python.org/'),
        )

# Social widget
SOCIAL = (('',''),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME="./theme/cv/"

DEFAULT_METADATA = {
    'paperstatus': 'Working Paper',
    'ssrn': '',
}

# No need to link Authors.
AUTHOR_SAVE_AS = ""
