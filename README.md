# nyc-viet-resturants-interactive-map
Vietnamese Restaurant Map NYC

**Description:**

The nyc-vietnamese-restaurants-interactive-map repository contains a Python-based application designed to visualize the distribution and detailed information of Vietnamese restaurants across New York City (NYC) using geospatial data analysis and interactive web mapping techniques. The core functionality of this application lies in parsing, analyzing, and visualizing complex JSON data, which comprises various attributes of restaurants, and presenting them on an interactive map.

**Technical Specifications:**

Language & Libraries: The project is entirely scripted in Python, leveraging several key libraries for data handling and visualization:
folium: Used for creating an interactive Leaflet map. It enables the design and rendering of complex, feature-rich maps.
json: Facilitates parsing and manipulation of JSON data files which contain the restaurant data.
Data: The primary dataset is a JSON file containing detailed information on Vietnamese restaurants in NYC. Each record includes:
Geographic coordinates (latitude, longitude)
Restaurant metadata (name, rating, price level, address)
Mapping Features:
Custom Markers: Each restaurant is represented with a marker, and the map's zoom level is initially set to encompass all of NYC. Clicking on a marker reveals a popup displaying the restaurant's name, rating (represented visually through star imagery), price level (denoted by dollar signs), and address.
Custom Tiles: The map uses a minimalistic tile layer, focusing the user's attention on the restaurant markers. It eschews unnecessary geographical details.
Responsive Popups: The popups are designed with HTML and CSS to ensure they are not only informative but also visually appealing. They are vertically elongated for better readability and content organization.
Utility Functions: The script includes custom functions to convert numerical ratings into star icons and price levels into corresponding dollar signs. This feature enhances the visual intuitiveness of the restaurant data.
Export: The final output is an HTML file that can be opened in any web browser, allowing for easy sharing and accessibility. This interactive map is self-contained within the HTML file, requiring no further setup or internet connection for functionality.

**Instructions for Cloning, Installation & Usage:**

Clone the repository using git clone followed by the repository's URL.
Navigate to the project's root directory in the command line.
Ensure Python is installed and use pip to install the folium library if not already installed.
Run the script using a Python interpreter. The map gets saved as an HTML file in the project's root directory and can be viewed in any web browser.
