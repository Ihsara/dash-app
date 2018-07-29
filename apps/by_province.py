import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

from app import app

layout = html.Div([
    html.H3('Điểm thi tốt nghiệp THPT 2018 theo tỉnh/ thành'),
    dcc.Dropdown(
        id='by-province-dropdown',
        options=[
            {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='by-province-display-value'),

], className='page')


@app.callback(
    Output('by-province-display-value', 'children'),
    [Input('by-province-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)