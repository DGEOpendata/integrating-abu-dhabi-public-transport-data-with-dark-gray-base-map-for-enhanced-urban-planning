python
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load the Abu Dhabi Dark Gray Base Map
base_map = gpd.read_file('path/to/dark_gray_base_map.shp')

# Load the Public Transportation Routes Dataset
transit_routes = pd.read_csv('path/to/abu_dhabi_transit_routes.csv')

# Convert transit routes to a GeoDataFrame
transit_routes_gdf = gpd.GeoDataFrame(transit_routes, 
                                      geometry=gpd.points_from_xy(transit_routes.longitude, transit_routes.latitude))

# Plot the base map
fig, ax = plt.subplots(figsize=(10, 10))
base_map.plot(ax=ax, color='darkgray')

# Overlay the transit routes on the base map
transit_routes_gdf.plot(ax=ax, marker='o', color='red', markersize=5)

# Add title and labels
plt.title('Integration of Abu Dhabi Public Transport Data on Base Map')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.show()
