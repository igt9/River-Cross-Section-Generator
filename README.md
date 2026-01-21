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

---

### PNG Files

- Distance vs Elevation cross-section plots

---



## Applications

This workflow can be applied to:

- River cross-section analysis  
- Flood modelling preprocessing (e.g., HEC-RAS)  
- Channel morphology and geomorphological studies  
- Urban flood risk assessment  
