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
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    try:
        return SITE_MAPPING[pathname]
    except KeyError:
        return noPage
"""
def display_page(pathname):
    print(pathname)
    if pathname == '/' or pathname == '/khai-quat' or pathname == '/khai-quat-graph':
        return overview.graph_layout
    elif pathname == '/khai-quat-table':
        return overview.table_layout

    elif pathname == '/theo-mon' or pathname == '/theo-mon-graph':
        return by_subject.graph_layout
    elif pathname == '/theo-mon-table':
            return by_subject.table_layout

    elif pathname == '/theo-tinh-thanh':
        return by_province.layout
    elif pathname == '/theo-ban-khoi':
        return by_department.layout
    elif pathname == '/theo-vung-mien' or pathname == '/theo-vung-mien-graph':
        return by_region.graph_layout
    elif pathname == '/theo-vung-mien-table':
        return by_region.table_layout
    elif pathname == '/thu-nghiem':
        return testing.layout
    elif pathname == '/full-view':
        return overview.layout, by_subject.layout, by_province.layout, by_department.layout, by_region.layout, testing.layout
    else:
        return noPage
"""

#Add CSS custom files here
external_css = [#"https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
#                 "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
#                 "https://codepen.io/bcd/pen/KQrXdb.css",
#                 'https://codepen.io/chriddyp/pen/bWLwgP.css',
#                 "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
#                 "https://codepen.io/chriddyp/pen/bWLwgP.css",
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