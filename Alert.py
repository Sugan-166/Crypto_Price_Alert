import requests
import time

def get_crypto_price(coin):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data[coin]['usd']

def alert(coin, target_price):
    current_price = get_crypto_price(coin)
    if current_price >= target_price:
        print(f"Alert: {coin} has reached the target price of ${target_price} (Current Price: ${current_price})")
    else:
        print(f"{coin} price is below the target price (Current Price: ${current_price})")

# Define the coins you want to monitor and their target prices
coins = {
    'bitcoin': 10000,  # Example target price for Bitcoin
    'ethereum': 10000,   # Example target price for Ethereum
}

# Polling interval in seconds
polling_interval = 30 # Every seconds

while True:
    for coin, target_price in coins.items():
        alert(coin, target_price)
    time.sleep(polling_interval)
