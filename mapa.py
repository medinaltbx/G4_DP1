import folium

map = folium.Map(location=[39.45, -0.35], tiles="Stamen Terrain", zoom_start=13)

tooltip1='Usuario 1'
tooltip2='Usuario 2'

folium.Marker([39.45,-0.40], popup='Usuario 1', tooltip=tooltip1).add_to(map)
folium.Marker([39.45,-0.41], popup='Usuario 2', tooltip=tooltip2).add_to(map)

map
