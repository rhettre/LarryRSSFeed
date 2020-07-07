import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET 
from xml.dom import minidom


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

content, stories, links, titles, descriptions = [],[],[],[],[]
# Read the XML file
with open("tcpalm.xml", "r") as file:
    # Read each line in the file, readlines() returns a list of lines
    content = file.readlines()
    # Combine the lines in the list into a string
    content = "".join(content)
    bs_content = BeautifulSoup(content, "lxml")
#Populate the links,titles,descriptions
stories = bs_content.find_all("promo-story-thumb-small")
stories.append(bs_content.find("promo-story-thumb-large"))

root = ET.Element('rss')
root.set('version', '2.0')
channel = ET.SubElement(root,'channel')
title = ET.SubElement(channel,'title')
title.text = "Content from Larry Reisman"
link = ET.SubElement(channel,'link')
link.text = "rhett.blog/Dad/rss"
description = ET.SubElement(channel,'description')
description.text = "An RSS feed that delivers you piping hot content from journalist Larry Reisman."

for story in stories:
    # links.append(story.attrs['url']=-00=-0)
    # titles.append(story.attrs['title'])
    # descriptions.append(story.attrs['descripton'])
    item = ET.SubElement(channel,'item')
    item_title = ET.SubElement(item, 'title')
    item_title.text = story.attrs['title']
    item_descripton = ET.SubElement(item, 'description')
    item_descripton.text = story.attrs['descripton']
    item_url = ET.SubElement(item, 'link')
    item_url.text = story.attrs['url']

with open('Larry_Reisman.rss', 'w') as file:
    file.write(prettify(root))
