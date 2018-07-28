import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

from app import app

layout = html.Div([
    html.H3('Điểm thi tốt nghiệp THPT 2018 theo khối/phân ban'),
    dcc.Dropdown(
        id='by-department-dropdown',
        options=[
            {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='by-department-display-value'),
])


@app.callback(
    Output('by-department-display-value', 'children'),
    [Input('by-department-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)