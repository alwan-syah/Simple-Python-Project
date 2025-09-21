import requests

def convert_currency(from_currency, to_currency, amount):
    url = "https://api.exchangerate.host/convert"
    params = {
        "from": from_currency,
        "to": to_currency,
        "amount": amount
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        print("🔍 Full API response:", data)  # Debugging, biar keliatan semua
        if data.get("success"):
            converted = data["result"]
            print(f"💱 {amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}")
        else:
            print("⚠️ Error in API response (no result).")
    else:
        print("❌ Error fetching exchange rates.")

# Example usage
convert_currency("usd", "inr", 10)


# - Add input() for interactive CLI  
# - Support batch conversions  
# - Build a GUI using Tkinter