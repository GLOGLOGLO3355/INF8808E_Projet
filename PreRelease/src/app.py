
# -*- coding: utf-8 -*-

import json

import dash
from dash import html
from dash import dcc

import pandas as pd

import preprocess
import bubble

app = dash.Dash(__name__)
app.title = 'Pre-Release | INF8808'