# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

'''
    Declaration of a Dash-app. Always right after import.
'''
app = dash.Dash(
    meta_tags=[
    {
        'name': 'description',
        'content': 'Điểm thi tốt nghiệp THPT qua góc nhìn của đồ thị - biểu đồ. Bằng cách sử dụng biểu đồ, trang web này hướng đến mục tiêu cung cấp một cách nhìn khách quan về điểm thi tốt nghiệp THPT 2018'
    },
    {
        'name': 'author',
        'content': 'Trần Long Châu'
    },
    {
        'charset': 'utf-8'
    }
], title="Điểm thi tốt nghiệp THPT qua góc nhìn của đồ thị"

)
server = app.server
app.config.suppress_callback_exceptions = True

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>

        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
        </footer>
            <div class="ui fixed inverted vertical footer segment">
                <div class="ui container">
                <div class="ui stackable inverted divided equal height stackable grid">
                    <div class="three wide column">
                    <h4 class="ui inverted header">Về trang</h4>
                    <div class="ui inverted link list">
                        <a href="#" class="item">Lý do</a>
                        <a href="#" class="item">Dữ liệu</a>
                        <a href="#" class="item">Sitemap</a>
                        <a href="#" class="item">Liên lạc</a>
                    </div>
                    </div>
                    <div class="three wide column">
                    <h4 class="ui inverted header">Dịch vụ</h4>
                    <div class="ui inverted link list">
                        <a href="#" class="item">Quyền sử dụng</a>
                        <a href="#" class="item">Trách nhiệm</a>
                        <a href="#" class="item">Làm sao để làm ra trang này</a>
                        <a href="#" class="item">Thi thử đề 2018</a>
                    </div>
                    </div>
                    <div class="seven wide column">
                    <h4 class="ui inverted header">Về tác giả</h4>
                    <p>Trang web được thiết lập bởi Trần Long Châu.</p>
                    </div>
                </div>
                </div>
            </div>
        </div>
    </body>
</html>
'''

