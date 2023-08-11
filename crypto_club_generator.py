from pycoingecko import CoinGeckoAPI
import math
cg = CoinGeckoAPI()


def create_synopsis(crypto, ticker, crypto_name):
    all_data = cg.get_price(ids=crypto, vs_currencies='usd', include_24hr_change=True)
    price = all_data[crypto]['usd']
    percent = all_data[crypto]['usd_24h_change']
    emoji = ''

    percent_string = str(round(percent,2))
    price_string = str(price)
    

    if int(percent) >= 0:
        emoji = '📈'
    else:   
     emoji = '📉'

    synopsis = crypto_name + ' (' + ticker + ') - $' + price_string + ' ' + emoji + ' (' + percent_string + '%)'

    return(synopsis)


print(create_synopsis('bitcoin', 'BTC', 'Bitcoin'))
print(create_synopsis('ethereum', 'ETH', 'Ethereum'))
print(create_synopsis('litecoin', 'LTC', 'Litecoin'))
print(create_synopsis('binancecoin', 'BNB', 'Binancecoin'))
print(create_synopsis('dogecoin', 'DOGE', 'Dogecoin'))
print(create_synopsis('solana', 'SOL', 'Solana'))
print(create_synopsis('basic-attention-token', 'BAT', 'Basic Attention Token'))
print(create_synopsis('shiba-inu', 'SHIB', 'Shiba Inu'))