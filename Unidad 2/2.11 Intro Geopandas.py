#python -m pip install geopandas
# Importar las bibliotecas necesarias
import geopandas as gpd
import matplotlib.pyplot as plt

# URL del conjunto de datos de ejemplo (archivos shapefile)
url = "https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_admin_0_countries.zip"

# Cargar el conjunto de datos usando GeoPandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Visualizar la tabla de datos (primeras filas)
print(world.head())

# Graficar el mapa mundial
world.plot()
plt.title('Mapa Mundial')
plt.show()

# Filtrar un país específico (por ejemplo, España)
spain = world[world['name'] == 'Spain']
spain.plot()
plt.title('España')
plt.show()


colombia = world[world['name'] == 'Colombia']
colombia.plot()
plt.title('Colombia')
plt.show()

# Lectura de datos
path_to_data = gpd.datasets.get_path("nybb")
gdf = gpd.read_file(path_to_data)
gdf.to_file("my_file.geojson", driver="GeoJSON")

gdf = gdf.set_index("BoroName")
gdf["area"] = gdf.area
print(gdf['area'])

gdf['centroid'] = gdf.centroid
print(gdf['centroid'])

first_point = gdf['centroid'].iloc[0]
gdf['distance'] = gdf['centroid'].distance(first_point)
print(gdf['distance'])

gdf.plot("area", legend=True)
plt.show()

