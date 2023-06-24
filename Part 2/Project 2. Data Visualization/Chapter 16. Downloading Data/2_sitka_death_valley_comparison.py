from   pathlib import Path
import csv
import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates  as mdates

class Place:
    ''' That place's plot. '''

    def __init__(self, _CSV_FILE, _NAME):
        ''' Initialize main attributes. '''

        _PATH       = Path(_CSV_FILE)
        _READER     = csv.reader(_PATH.read_text().splitlines())
        _HEADER_ROW = next(_READER)

        _DATES_INDEX = _HEADER_ROW.index('DATE')
        _HIGHS_INDEX = _HEADER_ROW.index('TMAX')
        _LOWS_INDEX  = _HEADER_ROW.index('TMIN')

        _dates, self.highs, self.lows = [], [], []
        for _row in _READER:
            try:
                _date = datetime.datetime.strptime(_row[_DATES_INDEX], '%Y-%m-%d')
                _high = int(_row[_HIGHS_INDEX])
                _low  = int(_row[_LOWS_INDEX])
            except ValueError:
                print(f'Missing data for {_date} at {_NAME}.')
            else:
                _dates.append(_date)
                self.highs.append(_high)
                self.lows.append(_low)
        _FIRST_DAY, _last_day = _dates[0], _dates[-1]
        _last_day            += datetime.timedelta(days=1)

        _fig, self._ax = plt.subplots()
        _fig.canvas.manager.set_window_title(f'{_NAME}, 2021')
        self._ax.plot(_dates, self.highs, c='red', alpha=0.5)
        self._ax.plot(_dates, self.lows, c='blue', alpha=0.5)
        self._ax.fill_between(_dates, self.highs, self.lows, facecolor='blue', alpha=0.1)

        self._ax.set_title('Daily high and low temperatures')
        self._ax.set_ylabel('Temperature (F)')
        _fig.set_figheight(8)
        _fig.set_figwidth(15)

        self._ax.xaxis.set_major_locator(mdates.MonthLocator())
        self._ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonthday=16))
        self._ax.xaxis.set_major_formatter(ticker.NullFormatter())
        self._ax.xaxis.set_minor_formatter(mdates.DateFormatter('%b'))
        #
        for tick in self._ax.xaxis.get_minor_ticks():
            tick.tick1line.set_markersize(0)
            tick.tick2line.set_markersize(0)
        plt.xlim(_FIRST_DAY, _last_day)

    def set_ylims(self, MIN, MAX):
        self._ax.set_ylim(MIN, MAX)
        
    def show(self):
        plt.show()

_sitka        = Place('weather_data/sitka_weather_2021_simple.csv', 'Sitka')
_death_valley = Place('weather_data/death_valley_2021_simple.csv',
                     'Death Valley')

MIN = min(min(_sitka.lows),  min(_death_valley.lows))
MAX = max(max(_sitka.highs), max(_death_valley.highs))

_sitka.set_ylims(MIN, MAX)
_death_valley.set_ylims(MIN, MAX)

plt.show()