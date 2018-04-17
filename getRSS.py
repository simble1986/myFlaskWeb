#!/usr/bin/env python
# encoding: utf-8
import urllib2
from lxml import etree
import PyRSS2Gen
import datetime

url = "http://blog.51cto.com/cloudman"

response = urllib2.urlopen(url)
html = response.read()

selector = etree.HTML(html)
title = selector.xpath('//li/a[@class="tit"]/text()')
link = selector.xpath('//li/a[@class="tit"]/@href')
description = selector.xpath('//li/a[@class="tit"]/../a[@class="con"]/text()')

items = []
print len(title)
print len(link)
print len(description)
if len(title) == len(link) == len(description):
    for i in range(len(title)):
        item = {}
        item["title"] = title[i].strip()
        item["link"] = link[i].strip()
        item["desc"] = description[i].strip()
        items.append(item)
print items
rss_items = []
for i in items:
    t = i["title"]
    l = i["link"]
    d = i["desc"]
    rss_items.append(PyRSS2Gen.RSSItem(title=t, link=l, description=d, guid=PyRSS2Gen.Guid(l)))
print rss_items
rss = PyRSS2Gen.RSS2(
    title="CloudMan的blog",
    link="http://blog.51cto.com/cloudman",
    description="",
    lastBuildDate=datetime.datetime.now(),
    items=rss_items
)

rss.write_xml(open("cloudman.xml", "w"))