#!/usr/bin/env python
import sys
import sqlite3

import lxml.html
import urllib2

def getPoiDetail(url = '', rules = None):
	#url = 'http://place.qyer.com/poi/53917/'
	response = urllib2.urlopen(url);
	html = response.read()

	dom = lxml.html.fromstring(html);

	for rule in rules:
		v = dom.xpath(rule[3])
		for item in v:
			print item.text_content();

def getPoiList(url = '', rules = None):
	#url = 'http://place.qyer.com/chiang-mai/sight/'
	response = urllib2.urlopen(url);
	html = response.read()

	dom = lxml.html.fromstring(html);

	poi_links = dom.xpath("/html/body/div[@class='pla_wrap mb60']/div[@class='pla_main2']/div[2]/ul[@class='pla_listpage_poilist clearfix']/li/div[@class='infos']/h3[@class='titcn']/a")
	for item in poi_links:
		url = item.get('href')
		getPoiDetail(url, rules)

def getPages(url = '', rules=None):
	response = urllib2.urlopen(url);
	html = response.read()

	dom = lxml.html.fromstring(html);

	poi_links = dom.xpath("/html/body/div[@class='pla_wrap mb60']/div[@class='pla_main2']/div[2]/div[@class='clearfix']/div[@class='ui_page']/a")
	for item in poi_links:
		url = item.get('href')
		print url
		getPoiList("http://place.qyer.com" + url, rules)


if __name__ == '__main__':
	site_name = raw_input("Enter site name: ");

	conn = None
	try:
		conn = sqlite3.connect('./data/database.db')
		cur = conn.cursor()
		#find site info
		cur.execute("SELECT * FROM site WHERE `name`='%s';" % site_name)
		row = cur.fetchone()
		if row == None:
			print "no site find !"
			sys.exit(1)
			
		site_id = row[0]
	
		# find jobs
		cur.execute("SELECT id, start_url FROM job WHERE `site_id`='%s';" % site_id)
		rows = cur.fetchall()
		for row in rows:
			cur.execute("SELECT * FROM rule WHERE `job_id`='%d' AND status=1" % row[0])
			rules = cur.fetchall();

			getPages(row[1], rules)
			#print row[1]
			#print rules
	except sqlite3.Error, e:
		print "Error %s:" % e.args[0]
		sys.exit(1)
	finally:
		if conn:
			conn.close()

