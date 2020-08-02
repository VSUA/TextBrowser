import requests

from bs4 import BeautifulSoup
position = int(input())
url = input()


request = requests.get(url)
soup = BeautifulSoup(request.content, "html.parser")
data = soup.find_all("h2")
print(data[position].get_text())
