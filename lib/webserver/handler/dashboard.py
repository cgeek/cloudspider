#!/us/bin/env python

import tornado.web

class DashboardHandler(tornado.web.RequestHandler):
	def get(self):
		#self.write("Hello, world")
		self.render("dashboard.html")
