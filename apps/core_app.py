import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

#CONSTANTS declaration
__file__ = "./dat/province_code.xlsx"
PAGES_HREF = {'Khái quát': '/khai-quat', 'Theo môn': '/theo-mon', 'Theo tỉnh/thành': '/theo-tinh-thanh', 'Theo ban/khối': '/theo-ban-khoi', 'Theo khu vực/vùng miền': '/theo-vung-mien', 'Nơi thử nghiệm': '/thu-nghiem' }
SUBTAB = {'graph':'Biểu đồ','table':"Bảng"} # Arrange like this to make graph as a primary tab
BASE_DIR_DATA = "./dat/{}.csv"
SUBJECTS_REQUIRED = ['TOÁN', 'VĂN', 'LÝ', 'HÓA', 'SINH', 'SỬ', 'ĐỊA', 'GDCD', 'ANH', 'KHTN', 'KHXH']
SUBJECTS = ['TOÁN', 'VĂN', 'LÝ', 'HÓA', 'SINH', 'SỬ', 'ĐỊA', 'GDCD', 'ANH']
UNI_DEPARTMENT = ['KHỐI A', 'KHỐI B', 'KHỐI C', 'KHỐI A1']
UNI_DEPARTMENT_WITH_D = ['KHỐI A', 'KHỐI B', 'KHỐI C', 'KHỐI A1', "KHỐI D"]
NO_RESULT = (0, 17)

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
df_all_provinces = pd.concat(data_wrapper.values()).reset_index().drop(columns=['index'])
df_all_provinces_description = df_all_provinces.describe().round(2)#Round to 2 decimal place


#Define reusable components
def make_dash_table(df):
    ''' Return a dash definition of an HTML table for a Pandas dataframe '''
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

def get_menu(landing_page, className = "ui red six item tabular menu"):
    menu_list = []
    for _page in PAGES_HREF:
        if landing_page == _page:
            menu_list.append(dcc.Link(_page, href = PAGES_HREF[_page] , className="active item"))
        else:
            menu_list.append(dcc.Link(_page, href = PAGES_HREF[_page] , className="item"))
    menu = html.Div(menu_list , className=className)
    return menu

#Sub meny consists of table and graph tab. landing_page is either "Graph" or "Table"
def get_sub_menu(landing_page, lading_sub_page, className = "ui purple two item tabular menu"):
    menu_list = []
    for tab in SUBTAB:
        tabLink = "{}-{}".format(PAGES_HREF[landing_page],tab)
        if tab == lading_sub_page:
            menu_list.append(dcc.Link(SUBTAB[tab], href = tabLink , className="active item"))
        else:
            menu_list.append(dcc.Link(SUBTAB[tab], href = tabLink , className="item"))
    menu = html.Div(menu_list , className=className)
    return menu