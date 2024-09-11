"""
Scrape the price from a desktop.bg item
"""
import requests
from bs4 import BeautifulSoup


def get_price(url: str) -> float:
    page = requests.get(url)
    html_doc = page.content

    soup = BeautifulSoup(html_doc, "html.parser")

    # for item in soup.find_all("span", {"class": "price"}):
    #     print(item)
    
    return 0.0
