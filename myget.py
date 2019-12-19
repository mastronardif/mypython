#!/usr/bin/env python3
from bs4 import BeautifulSoup
from requests import get

import re
import sys
import os
import http.cookiejar
import json
import urllib.request, urllib.error, urllib.parse
import codecs
import yaml
import logging
import logging.config

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

def get_soup(url,header):
    #return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),
    # 'html.parser')
    return BeautifulSoup(urllib.request.urlopen(
        urllib.request.Request(url,headers=header)),
        'html.parser')

url = 'https://devops.com/the-top-six-cloud-computing-trends-of-2019/'
#url = 'https://www.bbc.com/news/world-europe-50824842'
#url = 'http://www.joeschedule.com'
url= "https://www.google.com/url?rct=j&sa=t&url=https://www.eventbrite.com/e/live-stream-tickets-icare4autism-international-conference-cannabinoids-medical-cannabis-tickets-86341484705&ct=ga&cd=CAEYXyoUMTQwNDA0MjQ5OTQxMjkyMjYxMTkyGjlkYTBhYzQxMTAwNzhiNzQ6Y29tOmVuOlVT&usg=AFQjCNH9XXLrYKpAGEB7mGcBW2jj87ExaA"
urlArticle = "http://boilerpipe-web.appspot.com/extract?url="+url
#url='http://boilerpipe-web.appspot.com/extract?url=https%3A%2F%2Fwww.bbc.com%2Fnews%2Fworld-europe-50824842&extractor=ArticleExtractor&output=text&extractImages='
#url=urlArticle

try :
    # r = requests.get(url)
    # r.url
    # print (r.content.decode())

    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    soup = get_soup(url,header)
    print (soup.encode('ascii', 'ignore').decode())
except Exception as err:
    logging.error(err)
    print("emailleri_al:error occured")
    print (Exception)
    pass
