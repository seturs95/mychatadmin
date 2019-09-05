#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = "pelican-themes/pelican-bootstrap3"
PLUGIN_PATHS = ['pelican-plugins']
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
TYPOGRIFY = True
PLUGINS = ['filetime_from_git','assets', 'sitemap', 'i18n_subsites']
FIRST_NAME = 'MyChatAdmin'
AUTHOR = 'Admin'
SITENAME = 'MyChatAdmin - A Ragebot alternative'
SITETITLE = 'MyChatAdmin - Make groupchats fun again'
SITESUBTITLE = 'The fun and fre group admin bot'
SITEDESCRIPTION = 'We aim to be an superior alternative to Ragebot. For free. For ever.'
COPYRIGHT_YEAR = 2019
ROBOTS = 'index, follow'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
GOOGLE_ANALYTICS = 'UA-147241774-1'
SHARIFF = True
SITEMAP = {'format': 'xml'}
SITEURL = 'https://mychatadm.in'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()
         

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
