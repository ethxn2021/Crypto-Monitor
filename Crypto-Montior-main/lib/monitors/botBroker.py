import requests
from bs4 import BeautifulSoup
import time
import random

class BotBroker:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',

        }

        self.priceMontior = self.getPrice()

    def getRandomProxy(self):
        with open("proxies.txt","r") as proxies:
            proxyList = proxies.readlines()

            return random.choice(proxyList).replace("\n","").replace(" ","")
        
    def setProxy(self):
        proxy = str(self.getRandomProxy())
        proxySplit = str(proxy).split(":")

        ip = str(proxySplit[0])
        port = str(proxySplit[1])
        username = str(proxySplit[2])
        password = str(proxySplit[3])

        proxyFormatHttp = 'http://{}:{}@{}:{}'.format(username,password,ip,port)

        proxiesParam = { 
            'https' : proxyFormatHttp 
            } 

        return proxiesParam 

    def getPrice(self):
        try:
            url = "https://botbroker.io/products/cyberaio"
            response = requests.get(url,headers=self.headers,proxies=self.setProxy(),timeout=6).text
        except requests.exceptions.Timeout as e:
            print("Proxy timeout. Moving on..")
            self.getPrice()

        soup = BeautifulSoup(response, 'html.parser')
        priceValue = soup.find_all("a","d-flex flex-wrap justify-content-between text-dark asks-bids-card__row asks-bids-card__row--linked asks-bids-card__row--best")[1].find("span","price").text
        botPrice = ""
        for line in priceValue.splitlines():
            line = line.replace(" ","")
            if line.startswith("$"):
                botPrice = line

        return botPrice

    def monitor(self):
        print("Current price: " + self.priceMontior)
        print("Awaiting change in price")
        time.sleep(60)
        while True:
            cyberSolePrice = self.getPrice()
            if (cyberSolePrice != self.priceMontior):
                self.priceMontior = cyberSolePrice
                print(self.priceMontior)

            time.sleep(120)
            print("No price change. Moving on...")

            
        

BotBroker().monitor()