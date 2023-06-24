from pathlib import Path
import csv
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates  as mdates
import matplotlib.ticker as ticker

# Preparation.
path                  = Path('weather_data/sitka_weather_2021_full.csv')
lines                 = path.read_text().splitlines()
reader                = csv.reader(lines)
header_row            = next(reader)
dates, precipitations = [], []

# Data processing.
for row in reader:
    dates.append(datetime.datetime.strptime(row[2], '%Y-%m-%d'))
    precipitations.append(float(row[5]))
#
first_day, last_day = dates[0], dates[-1]
last_day           += datetime.timedelta(days=1)

# Creating plot.
plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(dates, precipitations)

# Styling.
ax.set_title('Daily Precipitation\nSitka, 2021', fontsize=24)
#
fig.set_figwidth(15)
#
ax.xaxis.set_major_locator(mdates.MonthLocator()) # Creates al majors.
ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonthday=16)) # Creates minors
                                                               # in the middle
                                                               # of majors.
ax.xaxis.set_major_formatter(ticker.NullFormatter()) # Removes majors' labels.
ax.xaxis.set_minor_formatter(mdates.DateFormatter('%b')) # Set minors' labels.
#
for tick in ax.xaxis.get_minor_ticks(): # Hides minors' ticks.
    tick.tick1line.set_markersize(0)
    tick.tick2line.set_markersize(0)
plt.xlim(first_day, last_day) # To avoid showing extra months.
#
ax.set_ylabel('Precipitation', fontsize=14)
fig.set_figheight(8)

plt.show()

# CREDITS.
# https://stackoverflow.com/a/71097997/21197451 with
# https://matplotlib.org/3.4.3/gallery/ticks_and_spines/centered_ticklabels.html