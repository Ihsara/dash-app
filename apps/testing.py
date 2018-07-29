import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

from app import app
from .core_app import get_menu, data_wrapper, print_button

#Define constant of this page
page_id = 'Nơi thử nghiệm'

layout = html.Div([
    get_menu(page_id),
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
], className='page')


@app.callback(
    Output('testing-display-value', 'children'),
    [Input('testing-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)