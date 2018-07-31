import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

from app import app
from .core_app import get_menu, print_button, get_sub_menu

#Define constant of this page
page_id = 'Nơi thử nghiệm'
def init():
    global graph_layout, table_layout
    graph_layout = table_layout =[]

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
], className='ui autumn leaf container')

graph_layout = html.Div([
    html.Div([
        get_menu (page_id),
        html.H3('Điểm thi tốt nghiệp THPT 2018 theo vùng tỉnh/thành'),
        html.Br([]),
        dcc.Dropdown(
            id='testing-dropdown',
            options=[
                {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
                    'NYC', 'MTL', 'LA'
                ]
            ]
        ),
        html.Div(id='testing-display-value'),
        html.Br([]),

        get_sub_menu(page_id,'graph'),
        html.Div([
            html.Div("This is graph tab!", className="ui text container")
        ],className= "ui byTestingGraph vertical stripe segment", id="theo-mon-graph"),
    ], className="ui byTesting container")

], className='ui autumn leaf container')

table_layout = html.Div([
    html.Div([
        get_menu (page_id),
        html.H3('Điểm thi tốt nghiệp THPT 2018 theo vùng tỉnh/ thành'),
        html.Br([]),
        dcc.Dropdown(
            id='testing-dropdown',
            options=[
                {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
                    'NYC', 'MTL', 'LA'
                ]
            ]
        ),
        html.Div(id='testing-display-value'),
        html.Br([]),

        get_sub_menu(page_id,'table'),
        html.Div([
            html.Div("This is table tab!", className="ui text container")
        ],className= "ui byTestingGraph vertical stripe segment", id="theo-mon-graph"),
    ], className="ui byTesting container")

], className='ui autumn leaf container')


@app.callback(
    Output('testing-display-value', 'children'),
    [Input('testing-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)