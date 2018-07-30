import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

from app import app
from .core_app import get_menu, data_wrapper, print_button

#Define constant of this page
page_id = 'Theo môn'

layout = html.Div([
    get_menu (page_id),
    html.H3('Điểm thi tốt nghiệp THPT 2018 theo môn thi'),
    html.Br([]),
    dcc.Dropdown(
        id='by-subject-dropdown',
        options=[
            {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='by-subject-display-value'),

], className='ui autumn leaf container')


@app.callback(
    Output('by-subject-display-value', 'children'),
    [Input('by-subject-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)