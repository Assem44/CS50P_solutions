import requests
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    API = "094a96a7427a4c37b9c0f6192fb0ad058dfe5853a7d68c08cb76bca610f63328"
    try:
        r = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API}")
        data = r.json()
        price = float(data["data"]["priceUsd"])
        total_amount = bitcoins * price
        print(f"${total_amount:,.4f}")
    except requests.RequestException:
        sys.exit("Error fetching data")

if __name__ == "__main__":
    main()

