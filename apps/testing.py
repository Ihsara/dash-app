import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

from app import app

layout = html.Div([
    html.H3('Trang thử nghiệm của ứng dụng'),
    dcc.Dropdown(
        id='testing-dropdown',
        options=[
            {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='testing-display-value'),
])


@app.callback(
    Output('testing-display-value', 'children'),
    [Input('testing-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)