import requests
from bs4 import BeautifulSoup
import time
import random
from lib.discordWebhookSender import DiscordWebhookSender

class ADAMonitor:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',

        }

    def getRandomProxy(self):
        with open("lib\proxies.txt","r") as proxies:
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
    
    def convertToInt(self,price):
        price = price.replace("$","").replace(",","")
        priceFloat = float(price)
        return priceFloat

    def getADAPrice(self):
        URL = "https://finance.yahoo.com/quote/ADA-USD/"
        response = requests.get(URL,headers=self.headers).text
        soup = BeautifulSoup(response, 'html.parser')
        priceValue = soup.find('span', {'class' :'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
        priceValueInt = self.convertToInt(priceValue)
        return priceValueInt


    def monitor(self):
        print("Awaiting set price")

        alertAmount = "1.6"
        alertAmountInt = self.convertToInt(alertAmount)

        while True:
            ADAPrice = self.getADAPrice()
            print(ADAPrice)
            if ADAPrice <= alertAmountInt:
                DiscordWebhookSender(ADAPrice).send()  
                print("Webhook sent")
                break
            time.sleep(120)
