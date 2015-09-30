'''
Licence: GNU GPL v3
Author: Anandmoorthy

'''

from bs4 import BeautifulSoup
import urllib2
import re
import subprocess

def scrap_mp3(url):
	try:
		url = urllib2.urlopen(url)
		url_read = url.read()
		url.close()
		soup = BeautifulSoup(url_read,"lxml")
		for link in soup.find_all('a',href=re.compile('http.*\.mp3')):
			links = link['href']
			subprocess.call(["wget",links])
	except Exception as e:
			print e


print "Enter the Url:"
url_input = raw_input('>')

scrap_mp3(url_input)
