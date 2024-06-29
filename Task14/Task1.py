import requests


class CountryData:
    def __init__(self, url):
        self.url = url
        self.data = []

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.data = response.json()
        else:
            print("Failed to fetch data.")

    def display_countries_and_currencies(self):
        for country in self.data:
            name = country.get('name', {}).get('common', 'N/A')
            currencies = country.get('currencies', {})
            for code, info in currencies.items():
                currency_name = info.get('name', 'N/A')
                symbol = info.get('symbol', 'N/A')
                print(f"Country: {name}, Currency: {currency_name}, Symbol: {symbol}")

    def countries_with_dollar(self):
        dollar_countries = []
        for country in self.data:
            currencies = country.get('currencies', {})
            for info in currencies.values():
                if 'Dollar' in info.get('name', ''):
                    dollar_countries.append(country.get('name', {}).get('common', 'N/A'))
                    break
        print("Countries using Dollar as currency:")
        print(", ".join(dollar_countries))

    def countries_with_euro(self):
        euro_countries = []
        for country in self.data:
            currencies = country.get('currencies', {})
            for info in currencies.values():
                if 'Euro' in info.get('name', ''):
                    euro_countries.append(country.get('name', {}).get('common', 'N/A'))
                    break
        print("Countries using Euro as currency:")
        print(", ".join(euro_countries))

url = "https://restcountries.com/v3.1/all"
country_data = CountryData(url)
country_data.fetch_data()
country_data.display_countries_and_currencies()
country_data.countries_with_dollar()
country_data.countries_with_euro()
