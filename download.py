'''
Licence: GNU GPL v3
Author: Anandmoorthy

'''

from bs4 import BeautifulSoup
import requests
import re
import subprocess

def scrap_mp3(url):
	try:
		url_content = requests.get(url)
		soup = BeautifulSoup(url_content.text, "html.parser")
		for link in soup.find_all('a',href=re.compile('http.*\.mp3')):
			links = link['href']
			subprocess.call(["wget",links])
	except Exception as ex:
			print(ex)


print("Enter the Url: ")
url_input = input('>')

scrap_mp3(url_input)
