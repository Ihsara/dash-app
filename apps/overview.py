import os

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
import numpy as np

from app import app
from .core_app import get_menu, data_wrapper, print_button, get_sub_menu

#import DataFrame goes here
from .core_app import df_all_provinces_description, df_all_provinces

#import CONSTANTS goes here
from .core_app import SUBJECTS_REQUIRED, UNI_DEPARTMENT, UNI_DEPARTMENT_WITH_D, NO_RESULT, SUBJECTS

#Define constant of this page
page_id = 'Khái quát'



x_data = SUBJECTS

y_data = []
for subject in SUBJECTS:
    y_data.append(df_all_provinces[subject])

colors = ['rgba(93, 164, 214, 0.5)', 'rgba(255, 144, 14, 0.5)', 'rgba(44, 160, 101, 0.5)', 'rgba(255, 65, 54, 0.5)', 'rgba(207, 114, 255, 0.5)', 'rgba(127, 96, 0, 0.5)', 'rgba(255, 224, 156, 0.5)', 'khaki', 'lightsalmon']

traces = []

for xd, yd, cls in zip(x_data, y_data, colors):
        traces.append(go.Box(
            y=yd,
            name=xd,
            boxpoints=False,
            jitter=0.5,
            whiskerwidth=0.2,
            fillcolor=cls,
            marker=dict(
                size=2,
            ),
            line=dict(width=1),
        ))

layout = go.Layout(
    title='Phân bổ điểm của các môn thi tốt nghiệp THPT 2018',
    yaxis=dict(
        autorange=True,
        showgrid=True,
        zeroline=True,
        dtick=5,
        gridcolor='rgb(255, 255, 255)',
        gridwidth=1,
        zerolinecolor='rgb(255, 255, 255)',
        zerolinewidth=2,
    ),
    margin=dict(
        l=40,
        r=30,
        b=80,
        t=100,
    ),
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
    showlegend=False
)

fig = go.Figure(data=traces, layout=layout)

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
graph_layout = html.Div([

    #Header
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

    #sbd-output table
    html.Div([
        #Leaving this empty as it will be filled later with callback dependent function
    ],className="ui sbdTable vertical stripe segment", id="sbd-output"),

    get_sub_menu(page_id,'graph'),
    html.Div([
        html.H3("Tóm tắt tình hình kết quả thi tốt nghiệp THPT - tuyển sinh đại học 2018 qua biểu đồ", className="ui dividing header"),
        dcc.Graph(id='example-graph', figure=fig),
    ], className="ui mastcontent container"),


    get_menu (page_id, className="ui mastcontent red six item bottom attached tabular menu"),
    print_button(),

], className='ui autumn leaf container')

table_layout = html.Div([

    #Header
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

    #sbd-output table
    html.Div([
        #Leaving this empty as it will be filled later with callback dependent function
    ],className="ui sbdTable vertical stripe segment", id="sbd-output"),

    get_sub_menu(page_id,'table'),

    html.Div([
        html.H3("Tóm tắt tình hình kết quả thi tốt nghiệp THPT - tuyển sinh đại học 2018 qua dạng bảng", className="ui dividing header"),
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
        ], className="ui vertical mastcontent center aligned segment"),

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
        ], className="ui departmentTable mastcontent vertical stripe segment"),
    ], className="ui mastcontent container"),



    get_menu (page_id, className="ui red six item mastcontent bottom attached tabular menu"),
    print_button(),

], className='ui autumn leaf mastcontent container')

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
        ], className="ui mastcontent container")
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
        ], className="ui mastcontent container")
    except TypeError:
        sbd_output_layout = not_found_msg
    except ValueError:
        sbd_output_layout = not_found_msg

    if input_value is not  None :
        return sbd_output_layout
    else:
        sbd_output_layout = []
        return sbd_output_layout