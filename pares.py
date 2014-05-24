#!/usr/bin/env python

import lxml.html
import urllib2
import sqlite3

def getPoiDetail(url = ''):
	#url = 'http://place.qyer.com/poi/53917/'
	response = urllib2.urlopen(url);
	html = response.read()

	dom = lxml.html.fromstring(html);

	title = dom.xpath("/html/body/div[@class='pla_topbars']/div[@class='pla_topbar clearfix']/div[@class='clearfix']/div[@class='pla_topbar_names']/p[@id='pl_topbox_en']/a")
	for item in title:
		print item.text_content()
	title = dom.xpath("/html/body/div[@class='pla_topbars']/div[@class='pla_topbar clearfix']/div[@class='clearfix']/div[@class='pla_topbar_names']/div[@class='clearfix']/p[@class='pl_topbox_cn fontYaHei']/a");
	for item in title:
		print item.text_content()

	desc = dom.xpath("/html/body/div[@class='pla_wrap mb60']/div[@class='pla_main']/div[@id='summary_fixbox']/div[@id='summary_box']");
	for item in desc:
		print item.text_content()

	tips = dom.xpath("/html/body/div[@class='pla_wrap mb60']/div[@class='pla_main']/div[@class='pla_textpage_tips']/div[@class='texts']");
	for item in tips:
		print item.text_content();

	info = dom.xpath("/html/body/div[@class='pla_wrap mb60']/div[@class='pla_main']/div[@class='pla_textpage_summary'][2]/ul[@class='pla_textdetail_list']/li")
	for item in info:
		print item.text_content();

	dianpings = dom.xpath("/html/body/div[@class='pla_wrap mb60']/div[@class='pla_main']/div[@id='poicommentlist']/div[@class='pl_yelp']/div[@class='pl_yelp_main clearfix']/div[@class='pl_yelp_cnt']/p[@class='text']");
	for item in dianpings:
		print item.text_content();



def getPoiList(url = ''):
	#url = 'http://place.qyer.com/chiang-mai/sight/'
	response = urllib2.urlopen(url);
	html = response.read()

	dom = lxml.html.fromstring(html);

	poi_links = dom.xpath("/html/body/div[@class='pla_wrap mb60']/div[@class='pla_main2']/div[2]/ul[@class='pla_listpage_poilist clearfix']/li/div[@class='infos']/h3[@class='titcn']/a")
	for item in poi_links:
		url = item.get('href')
		getPoiDetail(url)

def getPages(url = ''):
	#url = 'http://place.qyer.com/chiang-mai/sight/'
	response = urllib2.urlopen(url);
	html = response.read()

	dom = lxml.html.fromstring(html);

	poi_links = dom.xpath("/html/body/div[@class='pla_wrap mb60']/div[@class='pla_main2']/div[2]/div[@class='clearfix']/div[@class='ui_page']/a")
	for item in poi_links:
		url = item.get('href')

