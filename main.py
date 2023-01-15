import time
import requests
from bs4 import BeautifulSoup


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36"}

url = "https://saltmag.ru/lifestyle/fun/6373-luchshie-memy-s-kotami/"


def main():
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find_all("figure", class_="widget-image mobile-full-width")
    for i in data:
        img_url = url + i.find("img").get("src")
        download(img_url)


def download(url):
    time.sleep(2)
    response = requests.get(url, headers=headers, stream=True)
    with open("memi/" + url.split("/")[-1], "wb") as r:
        for v in response.iter_content(1024*1024):
            r.write(v)


if __name__ == "__main__":
    main()
