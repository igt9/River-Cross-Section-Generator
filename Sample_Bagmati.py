import numpy as np
import pandas as pd
import geopandas as gpd
import rasterio
import matplotlib.pyplot as plt

cross_sections = gpd.read_file('C:/Users/imejg/Desktop/All Folders/7th Sem/Project1/Urban Flood Modelling/Project/Shapefiles/XS_Bagmati.shp')

# Assuming cross_sections is your GeoDataFrame
for ind, row in cross_sections.iterrows():
    XS_ID = str(row['HydroID'])  # Convert to string
    
    # Start and end coordinates
    start_coords = list(row.geometry.coords)[0]
    end_coords = list(row.geometry.coords)[1]
    
    # Initialize lists to store coordinates
    lon = [start_coords[0]]
    lat = [start_coords[1]]
    
    # Number of intermediate points
    n_points = 5
    
    # Calculate the distances
    x_dist = end_coords[0] - start_coords[0]
    y_dist = end_coords[1] - start_coords[1]
    
    # Loop to calculate intermediate points
    for i in np.arange(1, n_points + 1):
        point = [
            start_coords[0] + (x_dist / (n_points + 1)) * i,
            start_coords[1] + (y_dist / (n_points + 1)) * i,
        ]
        lon.append(point[0])
        lat.append(point[1])
    
    # Append the end coordinates
    lon.append(end_coords[0])
    lat.append(end_coords[1])
    
    # Create a DataFrame
    df = pd.DataFrame({'Latitude': lat, 'Longitude': lon})
    
    # Convert to GeoDataFrame
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
    gdf.crs = {'init': 'epsg:32645'}  # Updated CRS initialization
    
    gdf_pcs = gdf.to_crs(epsg=32645)
    
    # Calculate horizontal distance
    gdf_pcs['h_distance'] = 0
    for index, row in gdf_pcs.iterrows():
        gdf_pcs.at[index, 'h_distance'] = gdf_pcs.geometry[0].distance(gdf_pcs.geometry[index])
    
    # Extracting the elevations from the DEM
    gdf_pcs['Elevation'] = 0
    dem = rasterio.open(r'C:/Users/imejg/Desktop/All Folders/7th Sem/Flood Modelling/Project/projected.tif', mode='r')
    
    for index, row in gdf_pcs.iterrows():
        row_num, col_num = dem.index(row['Longitude'], row['Latitude'])
        dem_data = dem.read(1)
        gdf_pcs.at[index, 'Elevation'] = dem_data[row_num, col_num]
    
    # Extract h_distance and Elevation columns into a DataFrame
    x_y_data = gdf_pcs[['h_distance', 'Elevation']]
    
    # Save to CSV
    x_y_data.to_csv(r'C:/Users/imejg/Desktop/All Folders/7th Sem/Flood Modelling/Cross Sections/Bagmati/CSV/' + XS_ID + '.csv')
    
    # Creating plots for each cross-sectional profile
    plt.plot(gdf_pcs['h_distance'], gdf_pcs['Elevation'])
    plt.xlabel('Distance (m)')
    plt.ylabel('Elevation (m)')
    plt.grid(True)
    plt.title(XS_ID)
    
    # Save plot to PNG and close the plot to avoid overlapping
    plt.savefig(r'C:/Users/imejg/Desktop/All Folders/7th Sem/Flood Modelling/Cross Sections/Bagmati/PNG/' + XS_ID + '.png')
    plt.close()  # Close the plot figure