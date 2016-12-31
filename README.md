#Jazz Standards Extractor

This `standards.py` Python script is a simple web scraper that goes to [jazzstandards.com](http://jazzstandards.com) and extracts the rank, title and year of the 1000 most popular jazz standards (as calculated by the website author's [methodology](http://www.jazzstandards.com/overview.ranking.htm)).

[This](http://www.jazzstandards.com/compositions/index.htm) is the first page (of 10) of the site that contains the information we wish to extract. As you can see, the data is in a straightforward HTML table. This script uses [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/), make sure it is installed before you run it.

##Usage

    python standards.py

Or if you prefer to save the output to a file (which is most likely the case):

    python standards.py > output.txt

