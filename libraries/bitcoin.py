import requests
import sys

        
def cotation():
    URL = "https://economia.awesomeapi.com.br/last/BTC-USD"
    try:
        r=requests.get(f"{URL}")
        r.raise_for_status()

        data = r.json()

        quota = float(data['BTCUSD']['bid'])
        return quota
       

    except (requests.RequestException,requests.RequestException, KeyError, ValueError):
        print("Falha ao obter a cotação da API.")
        return None
        

def price():
    if len(sys.argv) == 2:

        try:
            price = float(sys.argv[1])*cotation()
            print(f"Preço: {price:,.4f}")

        except (ValueError, TypeError):
            print("Command-line argument is not a number")
            sys.exit(1)
    elif len(sys.argv) < 2:
        print("Missing command-line argument")

if __name__ == "__main__":
    price()
