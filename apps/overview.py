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
    get_menu (page_id),
    print_button(),
    html.H3('Khai quát điểm thi tốt nghiệp 2018')

], className='page')