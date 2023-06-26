from pathlib import Path
import csv
import datetime
import numpy as np
import plotly.express as px

path       = Path("fire_data/argentina_2022.csv")
lines      = path.read_text().splitlines()
reader     = csv.reader(lines)
header_row = next(reader)

dates, daynights, lats, lons = [], [], [], []
hover_txts, brightnesses     = [], []
for row in reader:
    date = datetime.datetime.strptime(row[5], '%Y-%m-%d').date()
    daynight = 'Day' if row[-2] == 'D' else 'Night'
    #
    dates.append(date)
    daynights.append(daynight)
    lats.append(float(row[0]))
    lons.append(float(row[1]))
    hover_txts.append(f"{date} - {daynight}")
    brightnesses.append(float(row[2]))

# Show top in map.
top = 100
a   = np.array(brightnesses)
ind = np.argpartition(a, -top)[-top:]
#
top_hover_txts   = [hover_txts[i] for i in ind]
top_brightnesses = [brightnesses[i] for i in ind]
top_lats         = [lats[i] for i in ind]
top_lons         = [lons[i] for i in ind]
#
fig = px.scatter_geo(projection = 'natural earth', scope = 'south america',
                     title = f'🔥 Top {top} Fires in Argentina, 2022 👨🏼‍🚒',
                     hover_name = top_hover_txts, size = top_brightnesses,
                     color = top_brightnesses,
                     color_continuous_scale = 'YlOrRd',
                     lat = top_lats, lon = top_lons,
                     labels = {'size': 'Brightness', 'color': 'Brightness',
                               'lat': 'Latitude', 'lon': 'Longitude'})
fig.show()

# Show daily brightness.
unique_dates          = sorted([*set(dates)])
brightnesses_per_days = []
for date in unique_dates:
    brightness_per_day = 0
    for i in range(len(dates)):
        if dates[i] == date:
            brightness_per_day += brightnesses[i]
    brightnesses_per_days.append(brightness_per_day)

fig = px.line(title = '🔥 Daily Fire Brightness in Argentina, 2022 👨🏼‍🚒',
              x = unique_dates, y = brightnesses_per_days,
              labels = {'x': 'Date', 'y': 'Brightness'})
fig.update_traces(line_color = '#ea594e')
fig.show()

# Show day/night fires.
q_days   = daynights.count('Day')
q_nights = daynights.count('Night')
fig = px.pie(title = '🔥 Day/Night Fires in Argentina, 2022 👨🏼‍🚒',
             values = [q_days, q_nights], names = ['Day', 'Night'],
             color_discrete_sequence = [px.colors.qualitative.Safe[0],
                                        px.colors.qualitative.Safe[4]])
fig.update_traces(hovertemplate = '%{value} fires')
fig.show()