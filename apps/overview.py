import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

from app import app
from .core_app import get_menu, data_wrapper, print_button

#import DataFrame goes here
from .core_app import df_all_provnces_description

#import CONSTANTS goes here
from .core_app import SUBJECTS_REQUIRED, UNI_DEPARTMENT

#Define constant of this page
page_id = 'Khái quát'

#Functions for this page:
def make_dash_table(df):
    ''' Return a dash definitio of an HTML table for a Pandas dataframe '''
    table = []
    for index, row in df.iterrows():
        html_row = [html.Td([index])]
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table

tmp = [html.Th([subject]) for subject in SUBJECTS_REQUIRED]
tmp.insert(0, html.Th([]))
#Layour of Overview aka Main page
layout = html.Div([

    html.Div([
        html.Div([
            html.H1('Trang đồ họa đồ thị - biểu đồ về điểm thi tốt nghiệp THPT 2018',
            className = "ui dividing header"),
            html.Br([]),
            html.Div([
                html.I(className="attention icon"),
                html.Div("Tất cả dữ liệu trên đây đều được thu thập từ trên mạng và hoàn toàn không đáng tin vậy.\n Ứng dụng này chỉ nên để coi cho vui là chính."),
            ],className="ui warning icon message"),
            html.Br([]),
            html.Div([
                dcc.Input(type="text", placeholder="Số báo danh..."),
                html.I(className="search icon"),
            ], className="ui center aligned transparent left icon input center"),
        ], className="ui text container"),

    ], className="ui vertical masthead center aligned segment"),

    #Subjects table:
    html.Div([
        html.Div([
            html.I(className="help circle icon"),
            html.Div("Dữ liệu khối D hiện giờ chưa thể xử lý."),
        ],className="ui top attached warning icon message"),
        html.Table([
            html.Thead([
                html.Tr([html.Th([])] + [html.Th([subject]) for subject in SUBJECTS_REQUIRED])
            ]),
            html.Tbody(
                make_dash_table(df_all_provnces_description[SUBJECTS_REQUIRED])
                ),
            ], className="ui attached table")
    ], className="ui vertical stipe segment"),

    html.Br([]),

    # #Departments table:
    # html.Div([
    #     html.Div([
    #         html.I(className="attention icon"),
    #         html.Div("Khối D có vấn đề trong dữ liệu. Tạm thời không thể tính ra dữ liệu của khối D.")
    #     ],className="ui top attached warning icon message"),
    #     html.Table([
    #         html.Thead(),
    #         make_dash_table(df_all_provnces_description),
    #         ], className="ui attached table")
    # ], className="ui vertical stipe segment"),
    get_menu (page_id, className="ui bottom attached tabular menu"),
    print_button(),

], className='ui container')