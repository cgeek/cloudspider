#!/us/bin/env python

import tornado.web

class WelcomeHandler(tornado.web.RequestHandler):
	def get(self):
		#self.write("Hello, world")
		self.render("welcome.html")
