## Integration of Abu Dhabi Public Transport Data with Base Map

### Overview
This project demonstrates how to integrate public transportation data of Abu Dhabi with a dark gray base map using Python. By visualizing transit routes over the base map, users can gain insights into the city's transit infrastructure and urban layout.

### Prerequisites
- Python 3.x
- Geopandas
- Pandas
- Matplotlib

### Setup
1. Ensure Python and the required libraries are installed. You can install them using pip:
   bash
   pip install geopandas pandas matplotlib
   

2. Download the necessary datasets:
   - Abu Dhabi Dark Gray Base Map (in shapefile format)
   - Abu Dhabi Public Transportation Routes (in CSV format)

### Running the Example
1. Replace the file paths in the script with the correct paths to your datasets.
2. Run the script using a Python interpreter:
   bash
   python integrate_transit_with_basemap.py
   
3. The script will generate a plot showing the transit routes overlaid on the dark gray base map.

### Customization
- You can adjust the marker size and color in the `transit_routes_gdf.plot` function to suit your visualization needs.
- Additional geographic features can be added by loading more datasets and plotting them similarly.

### Troubleshooting
- Ensure the file paths are correct and the data files are accessible.
- If you encounter issues with Geopandas, verify that all dependencies are correctly installed.

This integration provides a powerful tool for urban planners, residents, and tourists to understand and navigate the public transit system in Abu Dhabi more effectively.