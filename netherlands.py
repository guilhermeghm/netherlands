import requests
from bs4 import BeautifulSoup

base_url = "https://www.netherlandsandyou.nl/travel-and-residence/visas-for-the-netherlands"

def scrape_info():
    res = requests.get(base_url)
    soup = BeautifulSoup(res.text, "html.parser")
    info = soup.find(class_="intro").get_text()
    return info

print(scrape_info())
