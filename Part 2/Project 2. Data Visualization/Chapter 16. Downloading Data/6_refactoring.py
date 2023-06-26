from pathlib import Path
import json
import plotly.express as px

path    = Path('eq_data/eq_data_last_30_days.geojson') # Retrieved 2023.06.25.
txt     = path.read_text()
eq_data = json.loads(txt)

hover_texts, mags, lons, lats = [], [], [], []
for eq_dict in eq_data['features']:
    hover_texts.append(eq_dict['properties']['title'])
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])

fig = px.scatter_geo(projection = 'natural earth',
                     title = eq_data['metadata']['title'],
                     hover_name = hover_texts, size = mags,
                     color = mags, color_continuous_scale = 'YlOrRd',
                     lat = lats, lon = lons,
                     labels = {'size' : 'Magnitude', 'color' : 'Magnitude',
                             'lat' : 'Latitude', 'lon' : 'Longitude'})

fig.show()