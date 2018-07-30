import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

from app import app, server
from apps import overview, by_subject, by_province, by_department, by_region, testing



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