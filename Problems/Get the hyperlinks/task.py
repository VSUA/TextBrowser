import requests

from bs4 import BeautifulSoup

position = int(input())
url = input()
request = requests.get(url)
soup = BeautifulSoup(request.content, "html.parser")

print(soup.find_all("a")[position].get("href"))