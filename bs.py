from bs4 import BeautifulSoup
import urlparse
import urllib

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href ="http://example.com/elsie" class=sister" id="link1">Elsie</a>
<a href ="http://example.com/lacie" class="sister" id="link2">lacie</a>and
<a href = "http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
url = "http://www.aryacollege.in/our-star-placements.php"
htmltext = urllib.urlopen(url)
soup = BeautifulSoup('<li class="hallabol">bol bhai kya haal</li>')
tag = soup.li
print (tag.name)
print (tag)
tag.name = "anarkali"
print (tag.name)
print (tag)
print (tag['class'])
print(tag.string)
#for link in soup.find_all('a'):
#	print(link.get('href'))

