from bs4 import BeautifulSoup
import requests

# Opening from the web using requests module
fhandle = requests.get('http://www.jazzstandards.com/compositions/index4.htm')
fhandle.raise_for_status()
soup = BeautifulSoup(fhandle.text, 'html.parser')


# Extract the <tr class='JSontentsLine'> tags
trsongs = soup('tr','JSContentsLine')

# Loop through these <tr>s and extract the rank, year and title
# Note that title text is trickier to extract, because it sits inside a <a> tag
for trsong in trsongs:
    rank = unicode(trsong.contents[0].contents[0])
    year = unicode(trsong.contents[1].contents[0])
    title = unicode(trsong.contents[2].contents[1].contents[0])
    print rank + ',' + year + ',' + title


