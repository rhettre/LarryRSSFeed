# LarryRSSFeed
A proof of concept RSS Feed Generator using the HTML from Larry's TCPALM posts

Files:

Larry.rss - The final output of scraper.py/tester.py

scraper.py - A version that scrapes the code from website and manipulates the HTML to create the rss feed XML code

tester.py - A version used for testing that doesn't scrape the website but instead uses the local tcpalm.xml. Use this so you don't make a bunch of needless spam http requests to the real site. 

tcpalm.xml - A local version of the scraped HTML for testing purposes. 