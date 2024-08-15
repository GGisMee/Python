import requests
from bs4 import BeautifulSoup

url = "https://example.com/kalender"  # Ersätt med den faktiska URL:en
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Exempel på hur man hämtar alla händelser som ligger i en viss HTML-klass
events = soup.find_all('div', class_='event-class')

for event in events:
    title = event.find('h2').text  # Antagande: titeln är i en h2-tag
    date = event.find('span', class_='date-class').text  # Antagande: datumet finns i en span-tag med en viss klass
    print(f"Title: {title}, Date: {date}")
