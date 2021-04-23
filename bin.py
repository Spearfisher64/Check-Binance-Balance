from binance.client import Client
import config
client = Client(config.api_key, config.api_secret)
print("logged in")

info = client.get_account()



#for i in info:
 #   print(i)

bal= info['balances']
for b in bal:
    if float(b['free']) > 0:
        print(b)