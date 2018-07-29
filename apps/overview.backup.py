import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

from app import app

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

# reusable componenets
def make_dash_table(df):
    ''' Return a dash definitio of an HTML table for a Pandas dataframe '''
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table


def print_button():
    printButton = html.A(['In ra PDF'],className="button no-print print",style={'position': "absolute", 'top': '-40', 'right': '0'})
    return printButton

# includes page/full view
def get_logo():
    logo = html.Div([

        html.Div([
            html.Img(src='http://logonoid.com/images/vanguard-logo.png', height='40', width='160')
        ], className="ten columns padded"),

        html.Div([
            dcc.Link('Tổng hợp tất cả   ', href='/full-view')
        ], className="two columns page-view no-print")

    ], className="row gs-header")
    return logo


def get_header():
    header = html.Div([

        html.Div([
            html.H5(
                'Trang đồ họa đồ thị kết quả thi THPT 2018')
        ], className="twelve columns padded")

    ], className="row gs-header gs-text-header")
    return header


def get_menu():
    menu = html.Div([

        dcc.Link('Khái quát   ', href='/khai-quat', className="tab first"),

        dcc.Link('Theo môn   ', href='/theo-mon', className="tab"),

        dcc.Link('Theo tỉnh/thành   ', href='/theo-tinh-thanh', className="tab"),

        dcc.Link('Theo ban/ khối   ', href='/theo-ban-khoi', className="tab"),

        dcc.Link('Theo khu vực/ vùng miền   ', href='/theo-vung-mien', className="tab"),

        dcc.Link('Nơi thử nghiệm   ', href='/thu-nghiem', className="tab")

    ], className="row ")
    return menu

layout = html.Div( [

    print_button(),

    html.Div([
        get_logo(),
        get_header(),
        html.Br([]),
        get_menu(),
    ]
    ),

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

])


@app.callback(
    Output('overview-display-value', 'children'),
    [Input('overview-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)