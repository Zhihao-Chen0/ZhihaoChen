import requests
from bs4 import BeautifulSoup
url = 'https://commeventshub.onrender.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find_all('div', class_='Upcoming Events')
for quote in quotes:
    print(quote.text)
