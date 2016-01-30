#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Maclean Gaulin'
SITENAME = 'Maclean Gaulin'
SITEURL = '//mgaulin.com'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_DATE = 'fs'

JINJA_EXTENSIONS = ['jinja2.ext.with_', ]


# Blogroll
LINKS = (('Pandas', 'http://pandas.pydata.org/pandas-docs/stable/'),
         ('Python', 'http://python.org/'),
        )

# Social widget
# GITHUB_URL = 'https://github.com/gaulinmp'
TWITTER_URL = 'https://twitter.com/mg_was_taken'
SOCIAL = (('@mg_was_taken', 'http://twitter.com/mg_was_taken'),
          ('LinkedIn', 'https://www.linkedin.com/in/maclean-gaulin-a7a2b97'),
          ('Github', 'http://github.com/gaulinmp'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME="./theme/cv/"

DEFAULT_METADATA = {
    'paperstatus': '',
    'ssrn': '',
}

STATIC_PATHS = ['static', ]
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
CATEGORY_URL = '{slug}'
CATEGORY_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'

# No need to link Authors.
AUTHOR_SAVE_AS = ""
TAG_SAVE_AS = ""


# Individual configuration
LOCAL_RESOURCE = True
