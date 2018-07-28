# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
from pathlib import Path

'''
    Declaration of a Dash-app. Always right after import.
'''
app = dash.Dash()
server = app.server
app.config.suppress_callback_exceptions = True
