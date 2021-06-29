#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'QianPeili'
SITENAME = u'爪了个子'
SITETITLE = u"爪了个子(QianPeili)"
SITESUBTITLE = u'我所见，我所想'
# SITEURL = 'http://localhost:8000/'
SITEURL = 'https://qianpeili.github.io'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'cn'
SITELOGO = '/images/profile.png'
MAIN_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
HOME_HIDE_TAGS =True

# Blogroll
LINKS = (
         ('About', '/about-me.html'),
         ('Email', 'mailto:qianperry@outlook.com'),
        )

# Social widget
SOCIAL = (('github', 'https://github.com/QianPeili'),
          ('qq', '394511725'),
    )
DEFAULT_PAGINATION = 10
INDEX_SAVE_AS = 'index.html'

# 自定义
THEME = "./themes/Flex"

MENUITEMS = (
             ('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Authors', '/authors.html'),
             ('Tags', '/tags.html'),)

GOOGLE_ANALYTICS  = "UA-100449520-1"

COPYRIGHT_NAME = "QianPeili"


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
