#!/usr/bin/env python

import tornado.web
import sqlite3

import tornado.escape

def _execute(query):
	dbPath = "./data/database.db"
	conn = sqlite3.connect(dbPath)
	cur = conn.cursor()
	try:
		cur.execute(query)
		result = cur.fetchall()
		conn.commit()
	except Exception:
		raise
	conn.close()
	return result

class ApiHandler(tornado.web.RequestHandler):
	def get(self):
		action = self.get_argument('action')
		name = self.get_argument('name')
		if (action == 'project') :
			query = """select * from site where name='%s' """ % name
			rows = _execute(query)
	
			row_json = tornado.escape.json_encode(rows);
			self.write(row_json)
		elif action == "ruleList":
			job_id = self.get_argument('job_id')
			query = """select * from rule where job_id='%s' """ % job_id 
			rows = _execute(query)
	
			row_json = tornado.escape.json_encode(rows);
			self.write(row_json)
		else:
			print 'noaction'

