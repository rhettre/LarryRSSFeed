import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET 
from ElementTree_pretty import prettify

####scrapes page fresh - url removed to stop page from being scrape spammed###
url = ""
response = requests.get(url)
bs_content = BeautifulSoup(response.text, "html.parser")
links, titles, descriptions = [],[],[]

#Populate the links,titles,descriptions
stories = bs_content.find_all("promo-story-thumb-small")
stories.append(bs_content.find("promo-story-thumb-large"))
for story in stories:
    links.append(story.attrs['url'])
    titles.append(story.attrs['title'])
    descriptions.append(story.attrs['descripton'])
    for title in titles:
        print(title)

root = ET.Element('rss')
root.set('version', '2.0')
channel = ET.SubElement(root,'channel')
title = ET.SubElement(root,'title')
title.text = "Content from Larry Reisman"
link = ET.SubElement(root,'link')
description = ET.SubElement(root,'description')
description.text = "An RSS feed that delivers you piping hot content from journalist Larry Reisman."

for story in stories:
    # links.append(story.attrs['url'])
    # titles.append(story.attrs['title'])
    # descriptions.append(story.attrs['descripton'])
    item = ET.SubElement(root,'item',{
    'title': story.attrs['title'],
    'description': story.attrs['descripton'],
    'link': story.attrs['url'],
    })

#print prettify(root)    