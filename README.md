# Cross-Section Elevation Extraction from DEM using Python

This repository contains a Python workflow to generate river cross-section elevation profiles by interpolating points along cross-section lines, extracting elevation values from a projected DEM, and exporting both CSV data and PNG plots.

The workflow is suitable for urban flood modelling, river hydraulics, and geomorphological analysis.

---

## Overview

For each cross-section polyline, the script:
1. Reads cross-section geometry from a shapefile
2. Generates evenly spaced intermediate points along the cross-section
3. Converts points to a projected coordinate system (UTM)
4. Calculates horizontal distance from the start of the cross-section
5. Extracts elevation values from a DEM raster
6. Exports distance–elevation data and profile plots

---

## Input Data

### Cross-Section Shapefile
- Geometry type: `LineString`
- Must contain a unique identifier field


Required attribute:
- `HydroID` – unique ID for each cross-section

---

### Digital Elevation Model (DEM)
- Format: GeoTIFF (`.tif`)
- Projected coordinate system


---

## Output

For each cross-section (`HydroID`):

### CSV Files

Contains:
- `h_distance` – horizontal distance from cross-section start (m)
- `Elevation` – elevation extracted from DEM (m)

Sample CSV:

<img width="354" height="556" alt="image" src="https://github.com/user-attachments/assets/1713a28a-b1bb-4ea3-b2cf-dd640ae6b3ea" />


---

### PNG Files

- Distance vs Elevation cross-section plots

Sample PNG:

<img width="640" height="480" alt="803" src="https://github.com/user-attachments/assets/1204c0d3-2d69-4ba3-8508-89fcbc038949" />


---



## Applications

This workflow can be applied to:

- River cross-section analysis  
- Flood modelling preprocessing (e.g., HEC-RAS)  
- Channel morphology and geomorphological studies  
- Flood risk assessment  
