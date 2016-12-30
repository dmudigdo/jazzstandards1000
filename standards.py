from bs4 import BeautifulSoup
import requests

# The base url
baseurl = 'http://www.jazzstandards.com/compositions/'

# This is the url for the first 100 songs
url = baseurl + 'index.htm'

while True:
    # Open the url for the first 100 songs, and soupize
    fhandle = requests.get(url)
    fhandle.raise_for_status()
    soup = BeautifulSoup(fhandle.text, 'html.parser')

    # Songs are in a <tr class='JSContentsLine'> tag, so extract these tags
    trsongs = soup('tr','JSContentsLine')

    # For each song, extract the rank, year and title as a tab-separated line
    # Note that the title sits in an <a> tag, so we need to go in deeper to extract
    for trsong in trsongs:
        rank = unicode(trsong.contents[0].contents[0])
        year = unicode(trsong.contents[1].contents[0])
        title = unicode(trsong.contents[2].contents[1].contents[0])
        print rank + '\t' + year + '\t' + title

    # The 'next' url to load the next page of 100 standards (if exists)
    # is in a solitary <p align="right"> so find this
    nextlinkp = soup.find('p',align="right")

    # Test for existence of 'next' url, break if invalid (i.e. tag has no name),
    # reset url if valid
    if nextlinkp.contents[2].name == None:
        break
    else:
        url = baseurl + unicode(nextlinkp.contents[2]['href'])

print 'Done here'
