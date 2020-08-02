import requests

from bs4 import BeautifulSoup
url = input()
request = requests.get(url)
soup = BeautifulSoup(request.content, "html.parser")
print(soup.find_all("h1")[0].get_text())