import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

from app import app, server, layout
from apps import app1, app2


#Add CSS custom files here
app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

#Base app layout:
app.layout = html.Div(children=[

    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),

])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/app1':
        return app1.layout
    elif pathname == '/apps/app2':
        return app2.layout
    else:
        return layout

if __name__ == '__main__':
    app.run_server(debug=True)