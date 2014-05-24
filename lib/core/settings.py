#!/usr/bin/env python

from lib.core.revision import getRevisionNumber

VERSION = "0.0.1-dev"
REVISION = getRevisionNumber()
VERSION_STRING = "cloudspider/%s%s" % (VERSION, "-%s" % REVISION if REVISION else "")
DESCRIPTION = "cloud spider in server"
