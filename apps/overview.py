import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

from app import app
from index import get_menu, get_header, data_wrapper

#Layour of Overview aka Main page
layout = html.Div([
    get_menu (),
    print_button()

], className='page')