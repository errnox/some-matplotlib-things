import re
from datetime import datetime, date

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.finance as fin
from matplotlib.dates import date2num


data = []

with open('./data/table.csv') as in_file:
    next(in_file)
    for line in in_file:
        # A line looks like this:
        # [date, open, high, low, close, volume, adj close]
        line = str.split(line, ',')
        # data.append(line)

        # However, matplotlib requires a sequence of
        # (time, open, close, high, low, ...) sequences
        data.append([
                date2num(datetime.strptime(line[0], '%Y-%m-%d')),
                float(line[1]),
                float(line[4]),
                float(line[2]),
                float(line[3]),
                ])


fig = plt.figure()
ax = fig.add_subplot(111)

fin.candlestick(ax, data, colorup='g', colordown='r', width=.5, alpha=.5)

plt.show()
