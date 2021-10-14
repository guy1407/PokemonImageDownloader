import requests
from bs4 import BeautifulSoup
import os

url = "https://www.pokemon.com/us/pokedex/"

r = requests.get(url)

soup = BeautifulSoup(r.text,'html.parser')

images = soup.find_all('img')
print(images)

for image in images:
    print(image['src'])

