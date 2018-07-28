import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

from app import app

layout = html.Div([
    html.H3('Điểm thi tốt nghiệp THPT 2018 theo môn thi'),
    dcc.Dropdown(
        id='by-subject-dropdown',
        options=[
            {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='by-subject-display-value'),

])


@app.callback(
    Output('by-subject-display-value', 'children'),
    [Input('by-subject-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)