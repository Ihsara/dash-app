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
app = dash.Dash()
server = app.server
app.config.suppress_callback_exceptions = True

#CONSTANTS declaration
__file__ = "dat/province_code.xlsx"
BASE_DIR_DATA = "dat/{}.csv"

#Other functions
def get_data(ref_province):
    data_wrapper = {}
    for province_id in range(64):
        try:
            data_wrapper[ref_province[ref_province["SỐ TT CỤM THI"] == province_id]["ĐIẠ PHƯƠNG"].values[0]] = pd.read_csv(BASE_DIR_DATA.format(province_id))
        except FileNotFoundError:
            pass
    return data_wrapper

province_ref = pd.read_excel(__file__)
data_wrapper = get_data(province_ref)

layout = html.Div( [
    html.H1(children='Trang đồ họa đồ thị kết quả thi THPT 2018'),

    html.P(children='''
        Chào mừng bạn đã đến với trang chủ của trang
    '''),

    html.Div(children='''
        Trang này dùng dữ liệu có sẵn từ kết quả thi tốt nghiệp THPT 2018 để vẽ vài biểu đồ
    '''),

    dcc.Graph(
        id='histogram-graph-hcmc-physics',
        figure={
            'data': [
                        go.Histogram(x=data_wrapper["TP.HCM"]['LÝ'],  histnorm='probability')
            ],
            'layout': {
                'title': 'Điểm thi Toán THPT của TP.HCM 2018'
            }
        }
    ),
    dcc.Link('Go to App 1', href='/apps/app1'),
    html.Br(),
    dcc.Link('Go to App 2', href='/apps/app2')
])