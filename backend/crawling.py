import requests
from bs4 import BeautifulSoup

url = "https://www.chosun.com/politics/election2025/2025/05/04/E4COEQT7RJACFGJQYUWW24C2VQ/?utm_source=bigkinds&utm_medium=original&utm_campaign=news"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.select('body > div#fusion-app')) 