# app.py

# -*- coding: utf-8 -*-

import dash
from dash import html, dcc

import histogram
import preprocess

app = dash.Dash(__name__)
app.title = 'Pre-Release | INF8808'

app.layout = html.Div(children=[
    html.H1("Academic Factors Dashboard"),
    dcc.Graph(
        id='example-histogram',
        figure=histogram.get_histogram()
    )
])
