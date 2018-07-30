import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

from app import app, server
from apps import overview, by_subject, by_province, by_department, by_region, testing

#Define constant:
SITE_MAPPING = {'/'         : overview.graph_layout,
    '/khai-quat'            : overview.graph_layout,
    '/khai-quat-graph'      : overview.graph_layout,
    '/khai-quat-table'      : overview.table_layout,
    '/theo-mon'             : by_subject.graph_layout,
    '/theo-mon-graph'       : by_subject.graph_layout,
    '/theo-mon-table'       : by_subject.table_layout,
    '/theo-tinh-thanh'      : by_province.graph_layout,
    '/theo-tinh-thanh-graph': by_province.graph_layout,
    '/theo-tinh-thanh-table': by_province.table_layout,
    '/theo-ban-khoi'        : by_department.graph_layout,
    '/theo-ban-khoi-graph'  : by_department.graph_layout,
    '/theo-ban-khoi-table'  : by_department.table_layout,
    '/theo-vung-mien'       : by_region.graph_layout,
    '/theo-vung-mien-graph' : by_region.graph_layout,
    '/theo-vung-mien-table' : by_region.table_layout,
    '/thu-nghiem'           : testing.graph_layout,
    '/thu-nghiem-graph'     : testing.graph_layout,
    '/thu-nghiem-table'     : testing.table_layout,
    '/full-view-graph'      : [overview.graph_layout, by_subject.graph_layout , by_department.graph_layout , by_province.graph_layout , by_region.graph_layout] }


#page layout
noPage = html.Div([  # 404

    html.P(["404 Trang không tồn tại"])

    ], className="no-page")

#Base app layout:
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(className="ui container", id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    try:
        return SITE_MAPPING[pathname]
    except KeyError:
        return noPage

#Add CSS custom files here
external_css = [ "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "https://cdn.jsdelivr.net/npm/semantic-ui@2.3.3/dist/semantic.min.css",
                "https://codepen.io/ihsara/pen/gjXdRd.css"]

for css in external_css:
    app.css.append_css({"external_url": css})

#Add js custom fiels here
external_js = [ "https://code.jquery.com/jquery-3.2.1.min.js",
                "https://codepen.io/bcd/pen/YaXojL.js",
               "https://cdn.jsdelivr.net/npm/semantic-ui@2.3.3/dist/semantic.min.js"]

for js in external_js:
    app.scripts.append_script({"external_url": js})

if __name__ == '__main__':
    app.run_server(debug=True)