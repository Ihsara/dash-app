import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

from app import app, server, layout
from apps import app1, app2

#page layout
noPage = html.Div([  # 404

    html.P(["404 Page not found"])

    ], className="no-page")

#Base app layout:
app.layout = html.Div(children=[

    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),

])

#Add CSS custom files here
external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "https://codepen.io/bcd/pen/KQrXdb.css",
                'https://codepen.io/chriddyp/pen/bWLwgP.css',
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

for css in external_css:
    app.css.append_css({"external_url": css})

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/app1':
        return app1.layout
    elif pathname == '/apps/app2':
        return app2.layout
    elif pathname == '/':
        return layout
    else:
        return noPage

if __name__ == '__main__':
    app.run_server(debug=True)