#Firstly, we import the CoinGecko library and set the client up.
from pycoingecko import CoinGeckoAPI
a = CoinGeckoAPI()

#create the function and retriev current market information for a set of coins
def coinGecko(coins):
    print(coins['symbol'], "--- current price:  ", coins['current_price'], "$")

#there are we make the capacity and get the current market cap position of a coins
def get_the_current_cap_rank(c):
    return c['market_cap_rank']


while True:
    #input the numbers
    n = int(input("Write numbers for filtering into currency: "))
    #In order to list all the supported coins prices, volume, market_cap_ranks and related data for a specific currency (USD), we write the following:
    list_of_coins = a.get_coins_markets(vs_currency='usd')[:n]
    #sort by current_cap_rank
    list_of_coins.sort(key=get_the_current_cap_rank)
    #for loop
    for coins in list_of_coins:
        coinGecko(coins)