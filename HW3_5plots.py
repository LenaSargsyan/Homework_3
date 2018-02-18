import dash
import dash_core_components as dcc
import dash_html_components as html
import quandl
import pandas as pd
from plotly.offline import plot, iplot
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)
import figure1
import figure2
import figure3
import figure4
import figure5


figure_1 = dcc.Graph(id="fig1", figure=figure1.figure1)
figure_2 = dcc.Graph(id="fig2", figure=figure2.figure2)
figure_3 = dcc.Graph(id="fig3", figure=figure3.figure3)
figure_4 = dcc.Graph(id="fig4", figure=figure4.figure4)
figure_5 = dcc.Graph(id="fig5", figure=figure5.figure5)

app = dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

#Setting Titles
contentTitle = html.H2(children="Homework 3",style=['coloring:red'])

firstGraphTitle = html.H4(children="Graph 1")
secondGraphTitle = html.H4(children="Graph 2")
thirdAndForthGraphTitle = html.H4(children="Graph 3 and 4")
fifthGraphTitle = html.H4(children="Graph 5")
#sixthGraphTitle = html.H1(children="Graph 6")

#Setting Desciptions
introContent= html.P(children="Homework 3 assumes the development of this web application using Dash and Plotly in Python. You are required to develop 6 plots (including one table) with the given layout. Subtle differences related to styling (colors etc) are allowed, yet the general layout must be kept to perceive same information as this website does. Quandl is used as a data source for 4 plots among 6, while the other 2 are based on user provided data. Some of the Quandl based plots require minor analysis using pandas. You are encouraged to follow below mentioned steps to complete the HW:")
firstGraphContent = html.P(children="The graph on the right hand side is showing correlations of different variables (call them from x1 to x8) with employee churn. Data is artificial, manually inputted by the developer. Recreate the graph. Small coloring or corelation value differences will be neglected.")
secondGraphContent = html.P(children="One the right hand side we have US GDP graphed over time. The data is sourced from QUANDL API (FRED/GDP). Your task is to recreate exactly the same graph.")
thirdAndFourthGraphContent = html.P(children="The two graphs on this row are based on Google's stock (WIKI/GOOGL) and Bitcoin's (BCHARTS/ABUCOINSUSD) prices sourced from Quandl. First, percentage changes are calculated. Then the latter is plotted using Box plot to find the distribution and outliers. In the end the first 4 percentage changes (apart from the very first one, which is N/A) are plotted in a table. Recreate similar graphs with the same values (minor styling is neglected).")
fifthGraphContent= html.P(children="Last graph is based on manually inputted data. It shows the Roadmap developed by an artificial startup. Task 1 is assumed to take the whole Janduary, while Task 2 is starting from March and ending in mid April. Afterwards, Task 3 begins and ends in the end of September. Recreate a similar Roadmap")
#sixthGraphContent =

#Settinng each graph Description divs content
introDescDiv=html.Div([introContent],
    className='three columns')
firstGraphDescDiv = html.Div([firstGraphTitle, firstGraphContent],
    className='three columns')
secondGraphDescDiv = html.Div([secondGraphTitle, secondGraphContent],
    className='five columns')
thirdAndFourthGraphDescDiv = html.Div([thirdAndForthGraphTitle, thirdAndFourthGraphContent],
    className='four columns')
fifthGraphDescDiv = html.Div([fifthGraphTitle, fifthGraphContent],
    className='five columns')

#Constructing Graph and setting into each Div
firstGraphGraphDiv  = html.Div([figure_1],className='six columns')
secondGraphGraphDiv = html.Div([figure_2],className='seven columns')
thirdGraphGraphDiv  = html.Div([figure_3],className='five columns')
fourthGraphGraphDiv = html.Div([figure_4],className='three columns')
fifthGraphGraphDiv  = html.Div([figure_5],className='seven columns')

#Parent divs of each Graph

firstGraphParentDiv = html.Div([introDescDiv, firstGraphDescDiv, firstGraphGraphDiv],
    className='row')
secondGraphParentDiv = html.Div([secondGraphDescDiv, secondGraphGraphDiv],
    className='row')
thirdAndFourthGraphParentDiv = html.Div([thirdAndFourthGraphDescDiv, thirdGraphGraphDiv, fourthGraphGraphDiv],
    className='row')
fifthGraphParentDiv =html.Div([fifthGraphDescDiv, fifthGraphGraphDiv],
    className='row')

#Container of all divs
container = html.Div([
	contentTitle,
	firstGraphParentDiv,
	secondGraphParentDiv,
	thirdAndFourthGraphParentDiv,
	fifthGraphParentDiv
	], className='row')


app.layout = html.Div([container], className='row')

if __name__ == '__main__':
	app.run_server(debug=True)


