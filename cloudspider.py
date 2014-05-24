#!/usr/bin/env python
#
# Author: cgeek <cgeek.share@gmail.com>
#          http://cgeek.org
# Create on 2014-05-23 20:06

import sys
import os
import inspect
import logging

from lib.core.data import paths
from lib.core.common import banner
from lib.core.common import setPaths 
from lib.webserver.server import initServer 
 
def modulePath():
    try:
        _ = sys.executable if weAreFrozen() else __file__
    except NameError:
        _ = inspect.getsourcefile(modulePath)
    
    return os.path.dirname(os.path.realpath(_))
    
def main():
    """
	Main function of cloudspider when running from command line
	"""
    paths.ROOT_PATH = modulePath()
    setPaths()
    banner()
    initServer()

if __name__ == '__main__':
	main()
