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
        <div>My Custom header</div>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
        </footer>
        <div>My Custom footer</div>
    </body>
</html>
'''

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
    printButton = html.A(['Print PDF'],className="button no-print print",style={'position': "absolute", 'top': '-40', 'right': '0'})
    return printButton

# includes page/full view
def get_logo():
    logo = html.Div([

        html.Div([
            html.Img(src='http://logonoid.com/images/vanguard-logo.png', height='40', width='160')
        ], className="ten columns padded"),

        html.Div([
            dcc.Link('Full View   ', href='/full-view')
        ], className="two columns page-view no-print")

    ], className="row gs-header")
    return logo


def get_header():
    header = html.Div([

        html.Div([
            html.H5(
                'Vanguard 500 Index Fund Investor Shares')
        ], className="twelve columns padded")

    ], className="row gs-header gs-text-header")
    return header


def get_menu():
    menu = html.Div([

        dcc.Link('Overview   ', href='/overview', className="tab first"),

        dcc.Link('Price Performance   ', href='/price-performance', className="tab"),

        dcc.Link('Portfolio & Management   ', href='/portfolio-management', className="tab"),

        dcc.Link('Fees & Minimums   ', href='/fees', className="tab"),

        dcc.Link('Distributions   ', href='/distributions', className="tab"),

        dcc.Link('News & Reviews   ', href='/news-and-reviews', className="tab")

    ], className="row ")
    return menu

layout = html.Div( [
    html.Div(
        className="app-header",
        children=[
            html.H1(className="app-header--title", children='Trang đồ họa đồ thị kết quả thi THPT 2018'),
        ]
    ),•FeKX(6*

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
    dcc.Link('Go to App 1', href='/apps/app1'),
    html.Br(),
    dcc.Link('Go to App 2', href='/apps/app2')
])