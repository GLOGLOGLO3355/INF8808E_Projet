# -*- coding: utf-8 -*-

import dash
from dash import html, dcc

import preprocess
import sunburst

app = dash.Dash(__name__)
app.title = 'Pre-Release | INF8808'

app.layout = html.Div(children=[
    html.H1("Academic Factors Dashboard"),
    dcc.Graph(
        id='example-sunburst',
        figure=sunburst.get_sunburst()
    )
])
