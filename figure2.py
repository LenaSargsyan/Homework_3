
from plotly.offline import plot, iplot
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)

import numpy as np

import pandas as pd

import quandl

#figure2

my_data1 = quandl.get("FRED/GDP", authtoken="g621vWh9j9bPtzWZYTDa")
data = [go.Scatter(x=my_data1.index,y=my_data1.Value,fill="tozeroy")]
layout=dict(title='<b>US GDP over time</b>')

figure2 = dict(data=data,layout=layout)
