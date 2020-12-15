#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *


AUTHOR = "Maclean Gaulin"
SITENAME = "Maclean Gaulin"

SITEURL = "//mgaulin.com"
GOOGLE_ANALYTICS = "G-97YF1Y9P10"
# GOOGLE_ANALYTICS = "UA-37522001-1" # old

# No TRAVISCI environmental variable defaults to github CI integration
if os.environ.get("TRAVISCI", False):
    SITEURL = "//gaulinmp.github.io"
    GOOGLE_ANALYTICS = "G-7JF9CCJ5BH"

RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = False

DEFAULT_PAGINATION = False
