import requests
from bs4 import BeautifulSoup
import json

def poemgen():
# Fetch the web page
    url = "https://v1.jinrishici.com/all"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    data = json.loads(soup.text)
    return data

if __name__ == "__main__":
    poem = poemgen()
    print(poem)
