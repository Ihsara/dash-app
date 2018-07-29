import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

from app import app
from .core_app import get_menu, data_wrapper, print_button

#Define constant of this page
page_id = 'Khái quát'

#Layour of Overview aka Main page
layout = html.Div([

    html.Div([
        html.Div([
            html.H1('Trang đồ họa đồ thị - biểu đồ về điểm thi tốt nghiệp THPT 2018',
            className = "ui dividing header"),
            html.Br([]),
            html.Div([
                dcc.Input(type="text", placeholder="Số báo danh..."),
                html.I(className="search icon"),
            ], className="ui center aligned transparent left icon input center"),
        ], className="ui text container"),

    ], className="ui vertical masthead center aligned segment"),

    get_menu (page_id),
    print_button(),

], className='ui container')