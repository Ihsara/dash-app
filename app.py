# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

'''
    Declaration of a Dash-app. Always right after import.
'''
app = dash.Dash(
    meta_tags=[
    {
        'name': 'description',
        'content': 'Điểm thi THPT qua góc nhìn của đồ thị - biểu đồ. Bằng cách sử dụng biểu đồ, trang web này hướng đến mục tiêu cung cấp một cách nhìn khách quan về điểm thi tốt nghiệp THPT 2018'
    },
    {
        'name': 'author',
        'content': 'Trần Long Châu'
    },
    {
        'charset': 'utf-8'
    }
]
)
server = app.server
app.config.suppress_callback_exceptions = True

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>

        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
        </footer>
        <div class='footer-cred'>Trang web được làm bởi Trần Long Châu</div>
    </body>
</html>
'''

