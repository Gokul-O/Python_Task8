import requests
from collections import defaultdict


class BreweryData:
    def __init__(self):
        self.base_url = "https://api.openbrewerydb.org/breweries"
        self.states = ["Alaska", "Maine", "New York"]
        self.data = []

    def fetch_data(self):
        for state in self.states:
            response = requests.get(f"{self.base_url}?by_state={state}&per_page=50")
            if response.status_code == 200:
                self.data.extend(response.json())

    def list_breweries(self):
        brewery_names = defaultdict(list)
        for brewery in self.data:
            state = brewery.get('state')
            if state in self.states:
                brewery_names[state].append(brewery.get('name'))

        for state, names in brewery_names.items():
            print(f"\nBreweries in {state}:")
            print("\n".join(names))

    def count_breweries(self):
        brewery_count = defaultdict(int)
        for brewery in self.data:
            state = brewery.get('state')
            if state in self.states:
                brewery_count[state] += 1

        print("\nCount of breweries in each state:")
        for state, count in brewery_count.items():
            print(f"{state}: {count}")

    def count_types_in_cities(self):
        city_brewery_types = defaultdict(lambda: defaultdict(int))
        for brewery in self.data:
            state = brewery.get('state')
            city = brewery.get('city')
            brewery_type = brewery.get('brewery_type')
            if state in self.states:
                city_brewery_types[state][(city, brewery_type)] += 1

        print("\nTypes of breweries in each city:")
        for state, cities in city_brewery_types.items():
            print(f"\nState: {state}")
            for (city, brewery_type), count in cities.items():
                print(f"City: {city}, Type: {brewery_type}, Count: {count}")

    def count_breweries_with_websites(self):
        website_count = defaultdict(int)
        for brewery in self.data:
            state = brewery.get('state')
            if state in self.states and brewery.get('website_url'):
                website_count[state] += 1

        print("\nCount of breweries with websites in each state:")
        for state, count in website_count.items():
            print(f"{state}: {count}")


brewery_data = BreweryData()
brewery_data.fetch_data()
brewery_data.list_breweries()
brewery_data.count_breweries()
brewery_data.count_types_in_cities()
brewery_data.count_breweries_with_websites()
