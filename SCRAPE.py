import requests # connection with url
from bs4 import BeautifulSoup   #works with scrubing
import time  # well TIME

    #well there is a scrap protection that i need to overcome, results are changing, but once a century!(5 mins) >~<

class Scraper:
    """gets 5 min interval values from coinmarketcap web site"""
    # deafult atributes
    URL = "NON"
    name = "NON"

    # constructor
    def __init__(self, name,url):
        self.url = url
        self.name = name

    # methods
    def scrape(self):
        """ Based on BeautifulSoup Lib gets reguests from URL than searches the text for Price value. """

        r = requests.get(self.url)

        web_content = BeautifulSoup(r.text, "html.parser")
        web_content = web_content.find("div", {"class": "priceValue___11gHJ"})

        return web_content.text[1:].replace(",","")

DOGE = Scraper("DOGE","https://coinmarketcap.com/ru/currencies/dogecoin/")
ETH = Scraper("ETH","https://coinmarketcap.com/ru/currencies/ethereum/")
SHIB = Scraper("SHIB","https://coinmarketcap.com/ru/currencies/shiba-inu/")


while True:
    """Endless loop to append new data to csv file with 5 min intervals"""
    t = time.strftime("%d/%m/%Y,%H:%M", time.gmtime())
    with open("CoinScraper.csv", "a", encoding="utf-8") as f:
        f.write(f"{t},{DOGE.scrape()},{ETH.scrape()},{SHIB.scrape()}\n")
    print(t)

    time.sleep(60*5)
