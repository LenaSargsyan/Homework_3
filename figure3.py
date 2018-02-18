import dash
import dash_core_components as dcc
import dash_html_components as html
import quandl
import pandas as pd
import numpy as np


from plotly.offline import plot, iplot
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)


#figure3

my_data2 = quandl.get("WIKI/GOOGL", authtoken="g621vWh9j9bPtzWZYTDa")
my_data3 = quandl.get("BCHARTS/ABUCOINSUSD", authtoken="g621vWh9j9bPtzWZYTDa")

x1 = my_data2.Open.pct_change()
x2 = my_data3.Open.pct_change()

trace_1f3 = go.Box(x=x1, name = '<b>Google</b>')
trace_2f3 = go.Box(x=x2, name = '<b>Bitcoin</b>')

layout=dict(title = 'Distribution of Price')
data = [trace_1f3, trace_2f3]
figure3=dict(data=data, layout=layout)
