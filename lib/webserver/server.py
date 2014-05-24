#!/usr/bin/env python

import os.path
import tornado.ioloop
import tornado.web
import tornado.autoreload

from lib.webserver.handler.welcome import WelcomeHandler
from lib.webserver.handler.api import ApiHandler
from lib.webserver.handler.dashboard import DashboardHandler

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r"/", WelcomeHandler),
			(r"/dashboard", DashboardHandler),
			(r"/api", ApiHandler)
		]
		settings = {
				"template_path" : os.path.join(os.path.dirname(__file__), "templates"),
				"static_path" : os.path.join(os.path.dirname(__file__), "static"),
				"debug" : True
				}
		super(Application, self).__init__(handlers, **settings)

def initServer():
	print "Server is started , listing in :8888 \n"
	Application().listen("8888")
	tornado.ioloop.IOLoop.instance().start()
	 
