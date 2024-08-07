from bs4 import BeautifulSoup
import requests
import sys
f = open("IMDb.html","w") 
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text)
tr = soup.findChildren("tr")
tr = iter(tr)
next(tr)
 
for movie in tr:
	title = movie.find('td', {'class': 'titleColumn'} ).find('a').contents[0]
	year = movie.find('td', {'class': 'titleColumn'} ).find('span', {'class': 'secondaryInfo'}).contents[0]
	rating = movie.find('td', {'class': 'ratingColumn imdbRating'} ).find('strong').contents[0]
	row = title + ' - ' + year + ' ' + ' ' + rating
 
f.write(row)
f.close()
