import requests
from bs4 import BeautifulSoup
adresses = ["https://www.geeksforgeeks.org/python/response-text-python-requests/"]
html = requests.get(adresses[0])

soup = BeautifulSoup(html.text,features="html.parser")
print(soup.get_text())
