# Write a Python program that gets census data on median household income in Connecticut using cenpy and then visualizes it as a chloropleth with folium. 

import cenpy
import folium
import pandas as pd

conn = cenpy.connect('ACS5')

data = conn.query('B19013_001E', geo_unit='tract:*', geo_filter={'state': '09', 'county': '001'})
df = pd.DataFrame(data)

m = folium.Map([41.62, -72.73], zoom_start=9)

m.choropleth(
    geo_data=df,
    name='choropleth',
    data=df,
    columns=['tract', 'B19013_001E'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Median Household Income in Connecticut'
)

folium.LayerControl().add_to(m)

m
