import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

from app import app
from .core_app import get_menu, data_wrapper, print_button

#import DataFrame goes here
from .core_app import df_all_provinces_description, df_all_provinces

#import CONSTANTS goes here
from .core_app import SUBJECTS_REQUIRED, UNI_DEPARTMENT, UNI_DEPARTMENT_WITH_D, NO_RESULT

#Define constant of this page
page_id = 'Khái quát'

#Functions for this page:
def make_dash_table(df, use_index=True):
    ''' Return a dash definitio of an HTML table for a Pandas dataframe '''
    table = []
    if use_index:
        for index, row in df.iterrows():
            html_row = [html.Td([index])]
            for i in range(len(row)):
                html_row.append(html.Td([row[i]]))
            table.append(html.Tr(html_row))
    else:
        for index, row in df.iterrows():
            html_row = []
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
                html.Div("Tất cả dữ liệu trên đây đều được thu thập từ trên mạng và hoàn toàn không đáng tin cậy.\n Ứng dụng này chỉ nên để coi cho vui là chính."),
            ],className="ui warning icon message"),
            html.Br([]),
            html.Div([
                dcc.Input(id="sbd-input" , type="text", placeholder="Số báo danh..."),
                html.I(className="search icon"),
            ], className="ui center aligned transparent left icon input center"),
        ], className="ui text container"),

    ], className="ui vertical masthead center aligned segment"),

    html.Div([
        #Leaving this empty as it will be filled later with callback dependent function
    ],className="ui sbdTable vertical stripe segment", id="sbd-output"),


    #Subjects table:
    html.Div([
        html.Div([
            html.I(className="help circle icon"),
            html.Div("Tỉnh An Giang không có trong hệ thống dữ liệu của trang web."),
        ],className="ui top attached warning icon message"),
        html.Table([
            html.Thead([
                html.Tr([html.Th([])] + [html.Th([subject]) for subject in SUBJECTS_REQUIRED])
            ]),
            html.Tbody(
                make_dash_table(df_all_provinces_description[SUBJECTS_REQUIRED])
                ),
            ], className="ui attached table")
    ], className="ui subjectTable vertical stripe segment"),

    html.Br([]),

    #Department to enter uni
    html.Div([
        html.Div([
            html.I(className="help circle icon"),
            html.Div("Dữ liệu khối D hiện giờ chưa thể xử lý."),
        ],className="ui top attached warning icon message"),
        html.Table([
            html.Thead([
                html.Tr([html.Th([])] + [html.Th([subject]) for subject in UNI_DEPARTMENT])
            ]),
            html.Tbody(
                make_dash_table(df_all_provinces_description[UNI_DEPARTMENT ])
                ),
            ], className="ui attached table")
    ], className="ui departmentTable vertical stripe segment"),

    get_menu (page_id, className="ui bottom attached tabular menu"),
    print_button(),

], className='ui autumn leaf container')

@app.callback(
    Output(component_id='sbd-output', component_property='children'),
    [Input(component_id='sbd-input', component_property='value')]
)
def update_output_div(input_value):
    not_found_msg = sbd_output_layout = html.Div([
        html.Div([
            html.I(className="attention icon"),
            html.Div("Không tìm thấy SBD đã nhập. Xin vui lòng hãy kiểm tra lại."),
            ],className="ui warning icon message"),
        ], className="ui container")
    try:
        table = df_all_provinces[df_all_provinces["SBD"] == int(input_value)]
        if table.values.shape == NO_RESULT:
            sbd_output_layout = not_found_msg
        else:
            sbd_output_layout = html.Div([
            html.P("Số báo danh: {}".format(input_value), className="ui text cotainer"),
            html.Table([
                html.Thead([
                    html.Tr([html.Th([subject]) for subject in SUBJECTS_REQUIRED])
                ]),
                html.Tbody(
                    make_dash_table(table[SUBJECTS_REQUIRED], use_index=False)
                    ),
            ], className="ui attached table"),
            html.Table([
                html.Thead([
                    html.Tr( [html.Th([subject]) for subject in UNI_DEPARTMENT_WITH_D])
                ]),
                html.Tbody(
                    make_dash_table(table[UNI_DEPARTMENT_WITH_D], use_index=False)
                    ),
            ], className="ui attached table")
        ], className="ui container")
    except TypeError:
        sbd_output_layout = not_found_msg
    except ValueError:
        sbd_output_layout = not_found_msg

    if input_value is not  None :
        return sbd_output_layout
    else:
        sbd_output_layout = []
        return sbd_output_layout