from plotly.offline import plot, iplot
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)

import numpy as np

import pandas as pd

import quandl


my_data2 = quandl.get("WIKI/GOOGL", authtoken="g621vWh9j9bPtzWZYTDa")
my_data3 = quandl.get("BCHARTS/ABUCOINSUSD", authtoken="g621vWh9j9bPtzWZYTDa")


#figure4
header = dict(values=['Google','Bitcoin'],
              align = ['left','center'],
              font = dict(color = 'white', size = 12),
              fill = dict(color='#119DFF')
             )


cells = dict(values=[round(my_data2.Open.pct_change().head()[1:],3),
                     round(my_data3.Open.pct_change().head()[1:],3)],
             align = ['left','center'],
             fill = dict(color=["yellow","white"])
            )

trace_f4 = go.Table(header=header, cells=cells)

data = [trace_f4]
layout = dict(width=500, height=300)
figure4 = dict(data=data, layout=layout)
