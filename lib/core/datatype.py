#!/usr/bin/env python

import copy
import types

class AttribDict(dict):
	"""
	This class defines the object, inheriting from Python data
	type dictionary

	>>> foo = AttribDict()
	>>> foo.bar = 1
	>>> foo.bar
	>>> 1
	"""

	def __init__(self, indict = None, attribute=None):
		if indict is None:
			indict = {}

		self.attribute = attribute
		dict.__init__(self, indict)
		self.__initialised = True

	def __getattr__(self, item):
		try:
			return self.___getitem__(item)
		except KeyError:
			raise CloudspiderDataException("unable to access item %s" % item)
	
	def __setattr__(self, item, value):
		if "_AttriDict__initialised" not in self.__dict__:
			return dict.__setattr__(self, item, value)
		elif item in self.__dict__:
			dict.__setattr__(self, item, value)
		else:
			self.__setitem__(item, value)

	def __getstate__(self):
		return self.__dict__
		
	def __setstate__(self, dict):
		self.__dict__ = dict

