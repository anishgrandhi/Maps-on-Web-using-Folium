import pandas as pd
import folium

df = pd.read_csv("Volcanoes-USA.txt")

map_1 = folium.Map(location=[df['LAT'].mean(), df['LON'].mean()], zoom_start=5)

def color(elev):
    if elev<1000:
        return 'green'
    elif elev>=1000 and elev<3000:
        return 'orange'
    if elev>3000:
        return 'red'

fg=folium.FeatureGroup(name="Volcano Locations")

for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    folium.Marker(location=[lat,lon],popup=(folium.Popup(name)),icon=folium.Icon(color=color(elev))).add_to(fg)

fg.add_to(map_1)

folium.LayerControl().add_to(map_1)                 
map_1.save('Volcanoes on World Map.html')