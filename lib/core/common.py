#!/usr/bin/env python

import os
import sys 

from lib.core.settings import VERSION
from lib.core.settings import VERSION_STRING
from lib.core.settings import DESCRIPTION 

from lib.core.data import paths

def dataToStdout(data, forceOutput=True):
	messge = ""
	message = data
	sys.stdout.write(message)
	
def setPaths():
    paths.DATA_PATH = os.path.join(paths.ROOT_PATH, "data")

def banner():
	_ = """\n%s - %s\n""" %  (VERSION_STRING, DESCRIPTION)
	dataToStdout(_, forceOutput=True)
