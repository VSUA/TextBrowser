import requests

from bs4 import BeautifulSoup
import re
word = input().strip()
url = input()

request = requests.get(url)
soup = BeautifulSoup(request.content, "html.parser")
print(soup.find_all("p", string=re.compile(word))[0].get_text())
