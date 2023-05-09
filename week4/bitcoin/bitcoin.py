# დავალება #27 - Bitcoin Price Index
import sys
import requests
import json

# Expects the user to specify as a command-line argument the number of Bitcoins, n that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
try:
    number_of_bitcoin = float(sys.argv[1])
except IndexError:
        sys.exit("Missing command-line argument")
except ValueError:
        sys.exit("Command-line argument is not a number")


# Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. 
try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    print("RequestException")

# convert json response data to the python object
data = r.json()

# get the price of 1 bitcoin
price = float(data["bpi"]["USD"]["rate_float"])

# Outputs the current cost of n Bitcoins in USD to four decimal places, using , as a thousands separator.
total_price = number_of_bitcoin * price
print(f"${total_price:,.4f}")

