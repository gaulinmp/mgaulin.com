#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *


AUTHOR = 'Maclean Gaulin'
SITENAME = 'Maclean Gaulin'
SITEURL = 'http://mgaulin.com'

GOOGLE_ANALYTICS = "UA-37522001-1"

RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = False


DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
LOCAL_RESOURCE = False
