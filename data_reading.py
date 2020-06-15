# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 19:48:52 2020

Inspired by https://geekswipe.net/technology/computing/analyze-chromes-browsing-history-with-python/

@author: Mircea Davidescu
"""
import os
import sqlite3
import pandas as pd
import numpy as np
from collections import OrderedDict
import matplotlib.pyplot as plt


# Identify history file location for Brave
data_path = os.path.expanduser('~')+"/AppData/Local/BraveSoftware/Brave-Browser/User Data/Default"
files = os.listdir(data_path)
history_db = os.path.join(data_path, 'History')


c = sqlite3.connect(history_db)

c = sqlite3.connect(history_db)
cursor = c.cursor()

# urls.url, urls.visit_count
info_statement = 'pragma table_info(urls)'
cursor.execute(info_statement)
tableInfo = cursor.fetchall()


visits_statement = 'pragma table_info(urls)'
cursor.execute(visits_statement)
visitsInfo = cursor.fetchall()




select_statement = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
cursor.execute(select_statement)
results = cursor.fetchall()


url,visits = map(list,zip(*results))


results_dict = {'URL': url, 'Visits': visits}
myURLS = pd.DataFrame(data = results_dict)

myURLS.to_csv('myFile.csv')


def parse(url):
	try:
		parsed_url_components = url.split('//')
		sublevel_split = parsed_url_components[1].split('/', 1)
		domain = sublevel_split[0].replace("www.", "")
		return domain
	except IndexError:
		print("URL format error!")
        
        
        
sites_count = {} #dict makes iterations easier :D

for url, count in results:
	url = parse(url)
	if url in sites_count:
		sites_count[url] += 1
	else:
		sites_count[url] = 1
        
plt.bar(myURLS['URL'], myURLS['Visits'])
plt.show()