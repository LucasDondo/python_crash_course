from   pathlib import Path
import csv
import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates  as mdates

class Place:
    ''' That place's plot. '''

    def __init__(self, _CSV_FILE):
        ''' Initialize main attributes. '''

        _PATH       = Path(_CSV_FILE)
        _READER     = csv.reader(_PATH.read_text().splitlines())
        _HEADER_ROW = next(_READER)

        _DATE_INDEX = _HEADER_ROW.index('DATE')
        _AVG_INDEX  = _HEADER_ROW.index('TAVG')

        self.dates, self.avgs = [], []
        for _row in _READER:
            try:
                _date = datetime.datetime.strptime(_row[_DATE_INDEX], '%Y-%m-%d')
                _avg  = float(_row[_AVG_INDEX])
            except ValueError:
                print(f'Missing data for {_date} at {_CSV_FILE}.')
            else:
                self.dates.append(_date)
                self.avgs.append(_avg)

        self.FIRST_DAY, self.last_day = self.dates[0], self.dates[-1]
        self.last_day                += datetime.timedelta(days=1)

_salta   = Place('weather_data/Salta.csv')
_ushuaia = Place('weather_data/Ushuaia.csv')

_fig, _ax = plt.subplots()
_ax.plot(_salta.dates,   _salta.avgs,   label='Salta',   c='red',  alpha=0.5)
_ax.plot(_ushuaia.dates, _ushuaia.avgs, label='Ushuaia', c='blue', alpha=0.5)
_ax.fill_between(_salta.dates, _salta.avgs, _ushuaia.avgs, facecolor='green', alpha=0.1)

_ax.set_title('Daily average temperatures in Salta and Ushuaia, 2022')
_fig.canvas.manager.set_window_title('Daily average temperatures in Salta and Ushuaia, 2022')
_ax.set_ylabel('Temperature (C)')
_ax.legend()
_fig.set_figheight(8)
_fig.set_figwidth(15)

_ax.xaxis.set_major_locator(mdates.MonthLocator())
_ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonthday=16))
_ax.xaxis.set_major_formatter(ticker.NullFormatter())
_ax.xaxis.set_minor_formatter(mdates.DateFormatter('%b'))
#
for tick in _ax.xaxis.get_minor_ticks():
    tick.tick1line.set_markersize(0)
    tick.tick2line.set_markersize(0)
plt.xlim(_salta.FIRST_DAY, _salta.last_day)

_ax.set_yticks(range(int(min(_ushuaia.avgs)), int(max(_salta.avgs)) + 1, 2))

plt.show()