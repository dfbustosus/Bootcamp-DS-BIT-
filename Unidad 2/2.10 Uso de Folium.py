import folium
import requests
import pandas

# 1. Basico
m = folium.Map(location=(45.5236, -122.6750))
print(folium.Map.__str__)
m.save("index.html")
m = folium.Map(location=(10.1023, -75.67))
m.save("colombia.html")

# 2. Mapa de contornos
m = folium.Map(tiles="cartodbpositron")
geojson_data = requests.get(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/world_countries.json"
).json()

folium.GeoJson(geojson_data, name="Hola mundo").add_to(m)
folium.LayerControl().add_to(m)
m.save("geojson_1.html")

# 3. Cloropeth
state_geo = requests.get(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json"
).json()
print(state_geo)
state_data = pandas.read_csv(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_unemployment_oct_2012.csv"
)
print(state_data)
m = folium.Map(location=[48, -102], zoom_start=3)
folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_data,
    columns=["State", "Unemployment"],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Unemployment Rate (%)",
).add_to(m)

folium.LayerControl().add_to(m)
m.save("cloropeth.html")
