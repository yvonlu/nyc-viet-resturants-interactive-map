import folium
import json

# Load data
with open('vietnamese_restaurants_nyc.json', 'r') as file:
    data = json.load(file)

# Create a map centered around NYC
m = folium.Map(location=[40.712776, -74.005974], zoom_start=12)


# Function to convert rating to star images
def rating_to_stars(rating):
    stars_html = ""
    full_star_url = "/Users/yvonlu/Desktop/Vietnamese 2/download.png"  # replace with your actual image URL
    half_star_url = "/Users/yvonlu/Desktop/Vietnamese 2/1088450-200.png"  # replace with your actual image URL
    empty_star_url = "/Users/yvonlu/Desktop/Vietnamese 2/126155384-full-single-star.jpg"  # replace with your actual image URL

    for i in range(1, 6):
        if rating >= i:
            stars_html += f'<img src="{full_star_url}" width="15" height="15" style="background: transparent;"/>'
        elif rating >= i - 0.5:
            stars_html += f'<img src="{half_star_url}" width="15" height="15" style="background: transparent;"/>'
        else:
            stars_html += f'<img src="{empty_star_url}" width="15" height="15" style="background: transparent;"/>'

    return stars_html

def price_level_to_dollars(price_level):
    if price_level is None:
        return "N/A"  # or return an empty string, or whatever you prefer for missing data
    else:
        return '$' * int(price_level)  # Convert the integer price level to a string of dollar signs

popup_css = """
<style>
    .leaflet-popup-content {
        width: auto !important;  /* adjust as necessary */
        height: 110px !important;  /* adjust as necessary */
    }
</style>
"""

# Add points to the map
for item in data:
    lat = item['geometry']['location']['lat']
    lng = item['geometry']['location']['lng']
    name = item['name']
    address = item.get('vicinity', '')
    rating = item.get('rating', None)

    stars_html = rating_to_stars(rating) if rating else "N/A"
    price_level = item.get('price_level')
    dollars = price_level_to_dollars(price_level)
    
    popup_text = f"{popup_css}<div style='width: auto; min-width: 120px;'><strong>{name}</strong><br>Rating: {stars_html}<br>Price: {dollars}<br>{address}</div>"
    folium.Marker(
        location=[lat, lng],
        popup=folium.Popup(folium.Html(popup_text, script=True), parse_html=True),  # Using folium.Html to handle more complex HTML
    ).add_to(m)

# Save the map to an HTML file
m.save('nyc_vietnamese_restaurants.html')

