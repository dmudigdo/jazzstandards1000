from bs4 import BeautifulSoup

# fhandle = open("Oct2016.xls")
# fhandle = open("jazzstandardsunix.html")
fhandle = open("jazzstandards.html")
# fhandle = open("jsutronly.html")

soup = BeautifulSoup(fhandle, 'html.parser')
trsongs = soup('tr','JSContentsLine')

# print trsongs

print 'First entry tr'
print trsongs[0]
print 'First entry tr contents'
print trsongs[0].contents

print '##'

print 'First entry tr, first td (rank)'
print trsongs[0].contents[0]
print 'Extracting tag contents... (first index)'
print trsongs[0].contents[0].contents[0]

print '##'

print 'First entry tr, second td (year)'
print trsongs[0].contents[1]
print 'Extracting tag contents...(first index)'
print trsongs[0].contents[1].contents[0]

print '##'

print 'First entry tr, third td (title) '
print trsongs[0].contents[2]
print 'Extracting tag contents... (first index of second index)'
print trsongs[0].contents[2].contents[1].contents[0]

for trsong in trsongs:
    rank = unicode(trsong.contents[0].contents[0])
    year = unicode(trsong.contents[1].contents[0])
    title = unicode(trsong.contents[2].contents[1].contents[0])
    print rank + ',' + year + ',' + title


# print soup.prettify()
