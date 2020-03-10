# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from tools import load_stock
from tools import generate_table

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
df = load_stock('fxi')
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4(children='fxi'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)