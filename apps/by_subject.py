import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

from app import app
from .core_app import get_menu, print_button, get_sub_menu

#Define constant of this page
page_id = 'Theo môn'
def init():
    global graph_layout, table_layout
    graph_layout = table_layout =[]

table_layout = html.Div([
    html.Div([
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
        html.Br([]),

        get_sub_menu(page_id,'table'),
        html.Div([
            html.Div("This is table tab!", className="ui text container")
        ],className= "ui bySubjectTable vertical stripe segment", id="theo-mon-table"),
    ], className="ui bySubject container")
], className='ui autumn leaf container')

graph_layout = html.Div([
    html.Div([
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
        html.Br([]),

        get_sub_menu(page_id,'graph'),
        html.Div([
            html.Div("This is graph tab!", className="ui text container")
        ],className= "ui bySubjectGraph vertical stripe segment", id="theo-mon-graph"),
    ], className="ui bySubject container")

], className='ui autumn leaf container')


@app.callback(
    Output('by-subject-display-value', 'children'),
    [Input('by-subject-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)