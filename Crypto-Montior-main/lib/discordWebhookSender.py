from discord_webhook import DiscordWebhook, DiscordEmbed

class DiscordWebhookSender:
    def __init__(self,price):
        self.price = str(price)

        self.webhook = DiscordWebhook(url='https://discord.com/api/webhooks/703124896259244042/Jp3mrwTHHQi9SgaExuoynIK_2m2vCjYr14zFH-5UT5p30E52k1uRjR99mj_KF33cG8Hb')
        self.embed = DiscordEmbed(title = "ADA-USD", description='**Price has passed the target of {}**'.format(self.price),color="4287f5")

    def setAuthor(self):
        self.embed.set_author(name="",icon_url="")

    def setImage(self):
        self.embed.set_image(url='')

    def setThumbnail(self):
        self.embed.set_thumbnail(url='https://etoro-cdn.etorostatic.com/market-avatars/100017/150x150.png')

    def setFooter(self):
        self.embed.set_footer(text='Powered by Kemzo') 

    def setTimeStamp(self):
        self.embed.set_timestamp()

    def setField(self):
        self.embed.add_embed_field(name='Current price', value='{}'.format(self.price))

    def setCryptoLinks(self):
        theLinks = "[ETORO](https://www.etoro.com/markets/ada)\
            [BINANCE](https://www.binance.com/en/trade/ADA_USDT?type=spot)\
                [KRAKEN](https://www.kraken.com/en-gb/prices/ada-cardano-price-chart/usd-us-dollar)"
        

        self.embed.add_embed_field(name='Links', value=theLinks,inline=False)


    def send(self):
        self.setImage()
        self.setThumbnail()
        self.setTimeStamp()
        self.setFooter()
        self.setField()
        self.setCryptoLinks()
        
        self.webhook.add_embed(self.embed)
        response = self.webhook.execute()

