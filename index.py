import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

from app import app, server
from apps import overview, by_subject, by_province, by_department, by_region, testing

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

"""
    Core variable for data in this app. This is the container of examination result of 62/63 provinces in Vietnam.
    province_ref : contains (id, geophraphical_name) E.g: (1, "TP.HCM")
    data_wraper  : dictionary of { id: DataFrame} which DataFrame contains examination result
"""
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

    ], className="ui tabular menu")
    return menu


#page layout
noPage = html.Div([  # 404

    html.P(["404 Trang không tồn tại"])

    ], className="no-page")

#Base app layout:
app.layout = html.Div(children=[

    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),

])

#Add CSS custom files here
external_css = [#"https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
#                 "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
#                 "//fonts.googleapis.com/css?family=Raleway:400,300,600",
#                 "https://codepen.io/bcd/pen/KQrXdb.css",
#                 'https://codepen.io/chriddyp/pen/bWLwgP.css',
#                 "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
#                 "https://codepen.io/chriddyp/pen/bWLwgP.css",
                "https://cdn.jsdelivr.net/npm/semantic-ui@2.3.3/dist/semantic.min.css"]

for css in external_css:
    app.css.append_css({"external_url": css})

#Add js custom fiels here
external_js = [# "https://code.jquery.com/jquery-3.2.1.min.js",
#                "https://codepen.io/bcd/pen/YaXojL.js",
               "https://cdn.jsdelivr.net/npm/semantic-ui@2.3.3/dist/semantic.min.js"]

for js in external_js:
    app.scripts.append_script({"external_url": js})

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/' or pathname == '/khai-quat':
        return overview.layout
    elif pathname == '/theo-mon':
        return by_subject.layout
    elif pathname == '/theo-tinh-thanh':
        return by_province.layout
    elif pathname == '/theo-ban-khoi':
        return by_department.layout
    elif pathname == '/theo-vung-mien':
        return by_region.layout
    elif pathname == '/thu-nghiem':
        return testing.layout
    elif pathname == '/full-view':
        return overview.layout, by_subject.layout, by_province.layout, by_department.layout, by_region.layout, testing.layout
    else:
        return noPage

if __name__ == '__main__':
    app.run_server(debug=True)