import requests
import time
import json

def get_places(api_key, location, radius, keyword):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    places = []
    next_page_token = None

    for _ in range(3):  # maximum of 3 pages
        params = {
            "key": api_key,
            "location": location,
            "radius": radius,
            "keyword": keyword,
        }
        if next_page_token:
            params["pagetoken"] = next_page_token

        response = requests.get(url, params=params)
        data = response.json()

        places.extend(data.get("results", []))

        next_page_token = data.get("next_page_token")
        if not next_page_token:
            break  # no more pages of results, exit loop

        time.sleep(2)  # short delay before requesting the next page

    return places


api_key = "AIzaSyAE1lOonmTMXswBvkNM2GufCC4-BpeYZMg"
location = "40.712776,-74.005974"  # coordinates for NYC
radius = "5000"  # adjust as needed to cover the area you're interested in
keyword = "Vietnamese restaurant"

places = get_places(api_key, location, radius, keyword)

# Save the results to a JSON file
with open('vietnamese_restaurants_nyc.json', 'w', encoding='utf-8') as f:
    json.dump(places, f, ensure_ascii=False, indent=4)

# For quick verification, you can print the number of places and the first place's details
print(f"Retrieved {len(places)} places")
if places:
    print(places[0])


